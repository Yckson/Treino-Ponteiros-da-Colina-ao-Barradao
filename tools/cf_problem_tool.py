#!/usr/bin/env python3
"""Ferramenta de curadoria/download de problemas do Codeforces.

Recursos:
- consulta metadados pela API publica do Codeforces;
- baixa enunciado em Markdown a partir da pagina publica do problema;
- extrai exemplos para src/<PROB>/input e src/<PROB>/output;
- organiza o enunciado em problems/<dificuldade>/<rating>/<categoria>/<PROB>/;
- oferece menu interativo com autocomplete via readline.

A API oficial nao fornece enunciados nem samples. Por isso, a ferramenta usa a
API para rating/tags e a pagina HTML publica para statement/examples.
"""

from __future__ import annotations

import argparse
import html
import json
import random
import re
import shutil
import textwrap
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = REPO_ROOT / "problems"
SRC_DIR = REPO_ROOT / "src"
TEMPLATE = REPO_ROOT / "templates" / "main.cpp"
CACHE_DIR = REPO_ROOT / ".cache" / "codeforces"
CACHE_FILE = CACHE_DIR / "problemset.json"
HTML_CACHE_DIR = CACHE_DIR / "statements"
CODEFORCES_API = "https://codeforces.com/api/problemset.problems"

CATEGORIES = [
    "implementation",
    "strings",
    "math",
    "greedy",
    "sorting",
    "binary-search",
    "two-pointers",
    "data-structures",
    "graphs",
    "dp",
    "geometry",
    "combinatorics",
]

DIFFICULTY_RANGES = [
    ("iniciante", 0, 999),
    ("facil", 1000, 1299),
    ("medio", 1300, 1699),
    ("dificil", 1700, 2099),
    ("avancado", 2100, 10**9),
]

TAG_TO_CATEGORY = {
    "implementation": "implementation",
    "strings": "strings",
    "string suffix structures": "strings",
    "math": "math",
    "number theory": "math",
    "greedy": "greedy",
    "sortings": "sorting",
    "binary search": "binary-search",
    "two pointers": "two-pointers",
    "data structures": "data-structures",
    "dsu": "data-structures",
    "trees": "graphs",
    "graphs": "graphs",
    "dfs and similar": "graphs",
    "shortest paths": "graphs",
    "graph matchings": "graphs",
    "dp": "dp",
    "geometry": "geometry",
    "combinatorics": "combinatorics",
    "probabilities": "combinatorics",
}

CATEGORY_TO_TAGS = {
    category: sorted(tag for tag, mapped in TAG_TO_CATEGORY.items() if mapped == category)
    for category in CATEGORIES
}

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

API_HEADERS = {
    "User-Agent": HTTP_HEADERS["User-Agent"],
    "Accept": "application/json",
}


@dataclass(frozen=True)
class Problem:
    contest_id: int
    index: str
    name: str
    rating: int | None
    tags: tuple[str, ...]
    solved_count: int

    @property
    def raw_code(self) -> str:
        return f"{self.contest_id}{self.index}"

    @property
    def repo_code(self) -> str:
        return f"CF_{self.raw_code}"

    @property
    def url(self) -> str:
        return f"https://codeforces.com/problemset/problem/{self.contest_id}/{self.index}"


def request_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers=API_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def request_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers=HTTP_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def load_problemset(force_refresh: bool = False) -> list[Problem]:
    if CACHE_FILE.exists() and not force_refresh:
        age = time.time() - CACHE_FILE.stat().st_mtime
        if age < 24 * 60 * 60:
            return parse_problemset(json.loads(CACHE_FILE.read_text(encoding="utf-8")))

    data = request_json(CODEFORCES_API)
    if data.get("status") != "OK":
        raise RuntimeError(f"Codeforces API falhou: {data.get('comment', 'erro desconhecido')}")

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(data["result"], ensure_ascii=False), encoding="utf-8")
    return parse_problemset(data["result"])


def parse_problemset(result: dict) -> list[Problem]:
    stats = {
        (entry["contestId"], entry["index"]): int(entry.get("solvedCount", 0))
        for entry in result.get("problemStatistics", [])
    }
    problems: list[Problem] = []
    for item in result.get("problems", []):
        if item.get("type") != "PROGRAMMING":
            continue
        if "contestId" not in item or "index" not in item:
            continue
        key = (item["contestId"], item["index"])
        problems.append(
            Problem(
                contest_id=int(item["contestId"]),
                index=str(item["index"]),
                name=str(item.get("name", "Sem nome")),
                rating=item.get("rating"),
                tags=tuple(item.get("tags", [])),
                solved_count=stats.get(key, 0),
            )
        )
    return problems


def parse_problem_code(code: str) -> tuple[int, str]:
    normalized = code.strip().upper().replace("-", "_")
    if normalized.startswith("CF_"):
        normalized = normalized[3:]
    match = re.fullmatch(r"(\d+)([A-Z][A-Z0-9]*)", normalized)
    if not match:
        raise ValueError("Codigo invalido. Use algo como CF_71A, 71A, CF_1526C2.")
    return int(match.group(1)), match.group(2)


def find_problem(problems: Iterable[Problem], code: str) -> Problem:
    contest_id, index = parse_problem_code(code)
    for problem in problems:
        if problem.contest_id == contest_id and problem.index.upper() == index.upper():
            return problem
    raise LookupError(f"Problema {code} nao encontrado na API do Codeforces.")


def difficulty_for_rating(rating: int | None) -> str:
    if rating is None:
        return "sem-rating"
    for name, start, end in DIFFICULTY_RANGES:
        if start <= rating <= end:
            return name
    return "avancado"


def rating_folder(rating: int | None) -> str:
    if rating is None:
        return "unrated"
    if rating >= 2500:
        return "2500+"
    return str(rating)


def category_for_tags(tags: Iterable[str], preferred: str | None = None) -> str:
    if preferred:
        return preferred
    for tag in tags:
        category = TAG_TO_CATEGORY.get(tag)
        if category:
            return category
    return "implementation"


def fetch_statement_html(problem: Problem) -> str:
    cache_path = HTML_CACHE_DIR / f"{problem.raw_code}.html"
    urls = [
        f"http://codeforces.com/problemset/problem/{problem.contest_id}/{problem.index}",
        f"https://codeforces.com/problemset/problem/{problem.contest_id}/{problem.index}?mobile=true",
        f"https://codeforces.com/problemset/problem/{problem.contest_id}/{problem.index}",
        f"https://mirror.codeforces.com/problemset/problem/{problem.contest_id}/{problem.index}",
    ]
    errors: list[str] = []
    for attempt in range(2):
        for url in urls:
            try:
                text = request_text(url)
                if "problem-statement" in text:
                    HTML_CACHE_DIR.mkdir(parents=True, exist_ok=True)
                    cache_path.write_text(text, encoding="utf-8")
                    return text
                errors.append(f"{url}: pagina sem problem-statement")
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
                errors.append(f"{url}: {exc}")
        if attempt == 0:
            time.sleep(2)
    if cache_path.exists():
        print("Aviso: Codeforces indisponivel agora; usando HTML em cache.")
        return cache_path.read_text(encoding="utf-8")
    raise RuntimeError("Nao consegui baixar o enunciado HTML. Tentativas:\n" + "\n".join(errors))


def extract_div_by_class(source: str, class_name: str) -> str | None:
    marker = f'class="{class_name}"'
    marker_pos = source.find(marker)
    if marker_pos == -1:
        return None
    start = source.rfind("<div", 0, marker_pos)
    if start == -1:
        return None
    pos = start
    depth = 0
    while True:
        next_open = source.find("<div", pos)
        next_close = source.find("</div", pos)
        if next_close == -1:
            return source[start:]
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            close_end = source.find(">", next_close)
            if close_end == -1:
                return source[start:]
            pos = close_end + 1
            if depth == 0:
                return source[start:pos]


def normalize_tex_math(text: str) -> str:
    replacements = {
        r"\leq": "<=",
        r"\geq": ">=",
        r"\le": "<=",
        r"\ge": ">=",
        r"\cdot": "*",
        r"\times": "*",
        r"\ldots": "...",
        r"\dots": "...",
        r"\infty": "infinity",
        r"\neq": "!=",
        r"\ne": "!=",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\\[;,! ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def protect_codeforces_math(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        content = normalize_tex_math(match.group(1))
        return f"`{content}`" if content else ""

    text = re.sub(r"\${3}(.*?)\${3}", repl, text, flags=re.S)
    text = re.sub(r"(?<!\\)\$(.*?)(?<!\\)\$", repl, text, flags=re.S)
    return text


def strip_tags(fragment: str) -> str:
    fragment = re.sub(r"<\s*br\s*/?\s*>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"</\s*p\s*>", "\n\n", fragment, flags=re.I)
    fragment = re.sub(r"</\s*li\s*>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<\s*li[^>]*>", "- ", fragment, flags=re.I)
    fragment = re.sub(r"</\s*div\s*>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    text = html.unescape(fragment)
    text = protect_codeforces_math(text)
    text = text.replace("\xa0", " ").replace("\r", "")
    lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(lines)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def html_to_markdown(fragment: str) -> str:
    body = fragment
    for removable_class in ("header", "sample-tests", "sample-test"):
        removable = extract_div_by_class(body, removable_class)
        if removable:
            body = body.replace(removable, "")
    body = re.sub(
        r"<div class=\"section-title\">(.*?)</div>",
        lambda m: "\n\n## " + strip_tags(m.group(1)) + "\n\n",
        body,
        flags=re.S,
    )
    body = re.sub(
        r"<pre>(.*?)</pre>",
        lambda m: "\n\n```text\n" + strip_tags(m.group(1)) + "\n```\n\n",
        body,
        flags=re.S,
    )
    markdown = strip_tags(body)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()


def extract_first(pattern: str, source: str) -> str | None:
    match = re.search(pattern, source, re.S | re.I)
    if not match:
        return None
    return strip_tags(match.group(1))


def extract_class_text(source: str, class_name: str) -> str | None:
    fragment = extract_div_by_class(source, class_name)
    if not fragment:
        return None
    return strip_tags(fragment)


def format_property(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    for prefix in ("time limit per test", "memory limit per test", "input", "output"):
        if text.startswith(prefix) and text != prefix:
            return f"{prefix}: {text[len(prefix):].strip()}"
    return text


def extract_samples(statement_html: str) -> list[tuple[str, str]]:
    sample = extract_div_by_class(statement_html, "sample-test") or extract_div_by_class(statement_html, "sample-tests")
    if not sample:
        return []
    blocks: list[tuple[str, str]] = []
    for kind, content in re.findall(r"<div class=\"(input|output)\">.*?<pre>(.*?)</pre>", sample, re.S):
        blocks.append((kind, strip_tags(content)))
    pairs: list[tuple[str, str]] = []
    pending_input: str | None = None
    for kind, text in blocks:
        if kind == "input":
            pending_input = text
        elif kind == "output" and pending_input is not None:
            pairs.append((pending_input, text))
            pending_input = None
    return pairs


def samples_to_markdown(samples: list[tuple[str, str]]) -> str:
    if not samples:
        return ""
    parts = ["## Examples"]
    for index, (sample_input, sample_output) in enumerate(samples, start=1):
        suffix = f" {index}" if len(samples) > 1 else ""
        parts.extend(
            [
                "",
                f"### Input{suffix}",
                "",
                "```text",
                sample_input.rstrip(),
                "```",
                "",
                f"### Output{suffix}",
                "",
                "```text",
                sample_output.rstrip(),
                "```",
            ]
        )
    return "\n".join(parts).rstrip()


def make_statement_markdown(problem: Problem, statement_html: str, category: str, samples: list[tuple[str, str]]) -> str:
    statement = extract_div_by_class(statement_html, "problem-statement") or statement_html
    title = extract_first(r"<div class=\"title\">(.*?)</div>", statement) or problem.name
    time_limit = extract_class_text(statement, "time-limit")
    memory_limit = extract_class_text(statement, "memory-limit")
    input_file = extract_class_text(statement, "input-file input-standard") or extract_class_text(statement, "input-file")
    output_file = extract_class_text(statement, "output-file output-standard") or extract_class_text(statement, "output-file")
    body = html_to_markdown(statement)

    metadata = [
        f"# {problem.repo_code} — {problem.name}",
        "",
        f"- Codeforces: [{problem.raw_code}]({problem.url})",
        f"- Score/rating: {problem.rating if problem.rating is not None else 'unrated'}",
        f"- Categoria local: `{category}`",
        f"- Tags Codeforces: {', '.join(problem.tags) if problem.tags else 'sem tags'}",
        f"- Resolvidos no Codeforces: {problem.solved_count}",
    ]
    if title:
        metadata.append(f"- Titulo original: {title}")
    if time_limit:
        metadata.append(f"- {format_property(time_limit)}")
    if memory_limit:
        metadata.append(f"- {format_property(memory_limit)}")
    if input_file:
        metadata.append(f"- {format_property(input_file)}")
    if output_file:
        metadata.append(f"- {format_property(output_file)}")

    examples = samples_to_markdown(samples)
    if examples:
        note_marker = "\n## Note"
        if note_marker in body:
            body = body.replace(note_marker, "\n\n" + examples + "\n" + note_marker, 1)
        else:
            body = body.rstrip() + "\n\n" + examples
    return "\n".join(metadata) + "\n\n---\n\n" + body.rstrip() + "\n"


def ensure_solution_skeleton(problem: Problem, samples: list[tuple[str, str]]) -> None:
    code = problem.repo_code
    prob_src = SRC_DIR / code
    input_dir = prob_src / "input"
    output_dir = prob_src / "output"
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    main_cpp = prob_src / "main.cpp"
    if not main_cpp.exists():
        if TEMPLATE.exists():
            shutil.copyfile(TEMPLATE, main_cpp)
        else:
            main_cpp.write_text(
                "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n"
                "    ios::sync_with_stdio(false);\n    cin.tie(nullptr);\n    return 0;\n}\n",
                encoding="utf-8",
            )
    for i, (sample_in, sample_out) in enumerate(samples, start=1):
        (input_dir / f"sample{i}.txt").write_text(sample_in.replace("\r\n", "\n").replace("\r", "\n").rstrip() + "\n", encoding="utf-8", newline="\n")
        (output_dir / f"sample{i}.txt").write_text(sample_out.replace("\r\n", "\n").replace("\r", "\n").rstrip() + "\n", encoding="utf-8", newline="\n")


def write_problem_files(problem: Problem, category: str | None = None) -> Path:
    final_category = category_for_tags(problem.tags, category)
    difficulty = difficulty_for_rating(problem.rating)
    rating = rating_folder(problem.rating)
    target = PROBLEMS_DIR / difficulty / rating / final_category / problem.repo_code
    target.mkdir(parents=True, exist_ok=True)

    statement_html = fetch_statement_html(problem)
    statement = extract_div_by_class(statement_html, "problem-statement") or statement_html
    samples = extract_samples(statement)
    markdown = make_statement_markdown(problem, statement_html, final_category, samples)

    (target / "statement.md").write_text(markdown, encoding="utf-8")
    (target / "metadata.json").write_text(
        json.dumps(
            {
                "code": problem.repo_code,
                "contestId": problem.contest_id,
                "index": problem.index,
                "name": problem.name,
                "rating": problem.rating,
                "difficulty": difficulty,
                "category": final_category,
                "tags": list(problem.tags),
                "solvedCount": problem.solved_count,
                "url": problem.url,
                "sampleCount": len(samples),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (target / "README.md").write_text(
        f"# {problem.repo_code} — {problem.name}\n\n"
        f"- Link: [{problem.raw_code}]({problem.url})\n"
        f"- Score: {problem.rating if problem.rating is not None else 'unrated'}\n"
        f"- Categoria: `{final_category}`\n"
        f"- Tags: {', '.join(problem.tags) if problem.tags else 'sem tags'}\n"
        f"- Samples extraidos: {len(samples)}\n\n"
        "## Observacoes de treino\n\n"
        "- Ideia principal:\n"
        "- Erros comuns:\n"
        "- Complexidade:\n",
        encoding="utf-8",
    )
    ensure_solution_skeleton(problem, samples)
    return target


def all_tags(problems: Iterable[Problem]) -> list[str]:
    tags = {tag for problem in problems for tag in problem.tags}
    return sorted(tags)


def make_completer(options: Iterable[str]) -> Callable[[str, int], str | None]:
    values = sorted(set(str(option) for option in options))

    def completer(text: str, state: int) -> str | None:
        matches = [value for value in values if value.lower().startswith(text.lower())]
        if state < len(matches):
            return matches[state]
        return None

    return completer


def prompt_autocomplete(prompt: str, options: Iterable[str], allow_empty: bool = True) -> str:
    try:
        import readline  # type: ignore
    except ImportError:
        return input(prompt).strip()

    old_completer = readline.get_completer()
    old_delims = readline.get_completer_delims()
    readline.set_completer(make_completer(options))
    readline.set_completer_delims(" \t\n")
    readline.parse_and_bind("tab: complete")
    try:
        while True:
            value = input(prompt).strip()
            if value or allow_empty:
                return value
            print("Digite um valor ou pressione Ctrl+C para sair.")
    finally:
        readline.set_completer(old_completer)
        readline.set_completer_delims(old_delims)


def prompt_rating() -> tuple[int | None, int | None]:
    value = prompt_autocomplete(
        "Rating ou intervalo (ex.: 1200, 1000-1400; vazio = qualquer): ",
        [str(x) for x in range(800, 2600, 100)] + ["800-1200", "1200-1600", "1600-2000", "2000-2500"],
    )
    if not value:
        return None, None
    match = re.fullmatch(r"(\d+)(?:\s*-\s*(\d+))?", value)
    if not match:
        print("Rating invalido; usando qualquer rating.")
        return None, None
    start = int(match.group(1))
    end = int(match.group(2) or match.group(1))
    if start > end:
        start, end = end, start
    return start, end


def filter_problems(
    problems: Iterable[Problem],
    category: str | None = None,
    rating_min: int | None = None,
    rating_max: int | None = None,
    required_tag: str | None = None,
    min_solved: int | None = None,
) -> list[Problem]:
    filtered: list[Problem] = []
    for problem in problems:
        if problem.rating is None:
            continue
        if rating_min is not None and problem.rating < rating_min:
            continue
        if rating_max is not None and problem.rating > rating_max:
            continue
        if required_tag and required_tag not in problem.tags:
            continue
        if category and category_for_tags(problem.tags) != category and not any(
            tag in CATEGORY_TO_TAGS.get(category, []) for tag in problem.tags
        ):
            continue
        if min_solved is not None and problem.solved_count < min_solved:
            continue
        filtered.append(problem)
    filtered.sort(key=lambda p: (p.rating or 0, -p.solved_count, p.raw_code))
    return filtered


def choose_random_problem(problems: list[Problem]) -> tuple[Problem, str | None]:
    category = prompt_autocomplete(
        "Categoria (tab autocompleta; vazio = qualquer): ", CATEGORIES
    )
    category = category or None
    rating_min, rating_max = prompt_rating()
    tag = prompt_autocomplete(
        "Tag Codeforces especifica (tab autocompleta; vazio = qualquer): ", all_tags(problems)
    )
    tag = tag or None
    min_solved_raw = input("Minimo de resolucoes (vazio = 0): ").strip()
    min_solved = int(min_solved_raw) if min_solved_raw.isdigit() else None

    candidates = filter_problems(problems, category, rating_min, rating_max, tag, min_solved)
    if not candidates:
        raise LookupError("Nenhum problema encontrado com essas caracteristicas.")

    preview = candidates[:10]
    print(f"\n{len(candidates)} candidatos encontrados. Alguns exemplos:")
    for problem in preview:
        print(
            f"  - {problem.repo_code} | {problem.rating} | {problem.name} "
            f"({problem.solved_count} resolucoes)"
        )

    # Peso leve por popularidade para reduzir chance de cair em problema muito obscuro.
    weights = [max(1, min(problem.solved_count, 100000)) for problem in candidates]
    chosen = random.choices(candidates, weights=weights, k=1)[0]
    print(f"\nEscolhido: {chosen.repo_code} — {chosen.name} [{chosen.rating}]")
    return chosen, category


def download_by_code(problems: list[Problem], code: str | None = None) -> None:
    if not code:
        code = prompt_autocomplete(
            "Codigo do problema (ex.: CF_71A, 71A): ",
            [problem.repo_code for problem in problems] + [problem.raw_code for problem in problems],
            allow_empty=False,
        )
    problem = find_problem(problems, code)
    category = category_for_tags(problem.tags)
    print(f"Baixando {problem.repo_code} — {problem.name}...")
    target = write_problem_files(problem, category)
    print_download_result(problem, target)


def print_download_result(problem: Problem, target: Path) -> None:
    src = SRC_DIR / problem.repo_code
    print("\nDownload concluido.")
    print(f"Problema: {target.relative_to(REPO_ROOT)}")
    print(f"Statement: {(target / 'statement.md').relative_to(REPO_ROOT)}")
    print(f"Fonte/testes: {src.relative_to(REPO_ROOT)}")
    print(f"Comando sugerido: make run PROB={problem.repo_code}")


def interactive_menu(force_refresh: bool = False) -> None:
    print("Carregando problemset do Codeforces...")
    problems = load_problemset(force_refresh=force_refresh)
    print(f"{len(problems)} problemas carregados.\n")

    while True:
        print("Menu")
        print("  1) Baixar problema pelo codigo")
        print("  2) Escolher e baixar problema aleatorio por caracteristicas")
        print("  3) Listar candidatos por filtros")
        print("  4) Atualizar cache da API")
        print("  0) Sair")
        option = input("Opcao: ").strip()
        try:
            if option == "1":
                download_by_code(problems)
            elif option == "2":
                problem, category = choose_random_problem(problems)
                target = write_problem_files(problem, category)
                print_download_result(problem, target)
            elif option == "3":
                category = prompt_autocomplete("Categoria (vazio = qualquer): ", CATEGORIES) or None
                rating_min, rating_max = prompt_rating()
                tag = prompt_autocomplete("Tag especifica (vazio = qualquer): ", all_tags(problems)) or None
                candidates = filter_problems(problems, category, rating_min, rating_max, tag)[:30]
                for problem in candidates:
                    print(f"{problem.repo_code:12} {str(problem.rating):>5}  {problem.name}  [{', '.join(problem.tags[:4])}]")
                print(f"Mostrando {len(candidates)} candidato(s).")
            elif option == "4":
                problems = load_problemset(force_refresh=True)
                print(f"Cache atualizado: {len(problems)} problemas.")
            elif option == "0":
                return
            else:
                print("Opcao invalida.")
        except KeyboardInterrupt:
            print("\nOperacao cancelada.")
        except Exception as exc:  # noqa: BLE001 - CLI deve sobreviver a falhas pontuais.
            print(f"Erro: {exc}")
        print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Baixa problemas do Codeforces para a estrutura do repositorio.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """
            Exemplos:
              python3 tools/cf_problem_tool.py
              python3 tools/cf_problem_tool.py --code CF_71A
              python3 tools/cf_problem_tool.py --random --category dp --rating 1300-1600
            """
        ),
    )
    parser.add_argument("--code", help="codigo do problema, como CF_71A ou 71A")
    parser.add_argument("--random", action="store_true", help="baixa um problema aleatorio")
    parser.add_argument("--category", choices=CATEGORIES, help="categoria local para filtro aleatorio")
    parser.add_argument("--rating", help="rating ou intervalo, como 1200 ou 1000-1400")
    parser.add_argument("--tag", help="tag exata do Codeforces para filtro aleatorio")
    parser.add_argument("--min-solved", type=int, help="minimo de resolucoes para filtro aleatorio")
    parser.add_argument("--refresh", action="store_true", help="forca atualizar cache da API")
    args = parser.parse_args(argv)

    if not any([args.code, args.random]):
        interactive_menu(force_refresh=args.refresh)
        return 0

    problems = load_problemset(force_refresh=args.refresh)
    if args.code:
        download_by_code(problems, args.code)
        return 0

    rating_min = rating_max = None
    if args.rating:
        match = re.fullmatch(r"(\d+)(?:\s*-\s*(\d+))?", args.rating)
        if not match:
            raise SystemExit("--rating invalido. Use 1200 ou 1000-1400.")
        rating_min = int(match.group(1))
        rating_max = int(match.group(2) or match.group(1))
        if rating_min > rating_max:
            rating_min, rating_max = rating_max, rating_min

    candidates = filter_problems(
        problems,
        category=args.category,
        rating_min=rating_min,
        rating_max=rating_max,
        required_tag=args.tag,
        min_solved=args.min_solved,
    )
    if not candidates:
        raise SystemExit("Nenhum problema encontrado com os filtros informados.")
    weights = [max(1, min(problem.solved_count, 100000)) for problem in candidates]
    problem = random.choices(candidates, weights=weights, k=1)[0]
    print(f"Escolhido: {problem.repo_code} — {problem.name} [{problem.rating}]")
    target = write_problem_files(problem, args.category)
    print_download_result(problem, target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
