#!/usr/bin/env python3
"""Ferramenta de curadoria/download de problemas do Codeforces.

Recursos:
- consulta metadados pela API publica do Codeforces;
- baixa enunciado em Markdown a partir da pagina publica do problema;
- extrai exemplos para src/<PROB>/input e src/<PROB>/output;
- organiza o enunciado em problems/<dificuldade>/<rating>/<categoria>/<PROB>/;
- permite listar/baixar problemas de um contest inteiro;
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
CODEFORCES_STANDINGS_API = "https://codeforces.com/api/contest.standings"

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
    "constructive algorithms": "implementation",
    "brute force": "implementation",
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


def parse_contest_id(value: str) -> int:
    text = value.strip()
    match = re.search(r"codeforces\.com/(?:contest|gym)/(\d+)", text)
    if match:
        return int(match.group(1))
    if text.isdigit():
        return int(text)
    raise ValueError("Contest invalido. Use um ID como 2248 ou uma URL do Codeforces.")


def fetch_contest_from_standings(contest_id: int) -> list[Problem]:
    url = f"{CODEFORCES_STANDINGS_API}?contestId={contest_id}&from=1&count=1"
    data = request_json(url)
    if data.get("status") != "OK":
        raise RuntimeError(f"contest.standings falhou: {data.get('comment', 'erro desconhecido')}")
    result = data.get("result", {})
    rows = result.get("rows", [])
    solved_by_index: dict[str, int] = {}
    for row in rows:
        for problem_result in row.get("problemResults", []):
            index = str(problem_result.get("problem", {}).get("index", ""))
            solved_by_index[index] = int(problem_result.get("bestSubmissionTimeSeconds") is not None)
    fetched: list[Problem] = []
    for item in result.get("problems", []):
        if "contestId" not in item or "index" not in item:
            continue
        index = str(item["index"])
        fetched.append(
            Problem(
                contest_id=int(item["contestId"]),
                index=index,
                name=str(item.get("name", "Sem nome")),
                rating=item.get("rating"),
                tags=tuple(item.get("tags", [])),
                solved_count=solved_by_index.get(index, 0),
            )
        )
    return fetched


def contest_problems(problems: Iterable[Problem], contest: str) -> list[Problem]:
    contest_id = parse_contest_id(contest)
    selected = [problem for problem in problems if problem.contest_id == contest_id]
    if not selected:
        selected = fetch_contest_from_standings(contest_id)
    selected.sort(key=lambda problem: problem.index)
    if not selected:
        raise LookupError(f"Nenhum problema encontrado para o contest {contest_id}.")
    return selected


def print_contest_problems(selected: list[Problem]) -> None:
    if not selected:
        print("Nenhum problema para mostrar.")
        return
    contest_id = selected[0].contest_id
    print(f"\nContest {contest_id}: {len(selected)} problema(s)")
    for problem in selected:
        rating = problem.rating if problem.rating is not None else "unrated"
        category = category_for_tags(problem.tags)
        tags = ", ".join(problem.tags) if problem.tags else "sem tags"
        print(f"  {problem.repo_code:12} {str(rating):>7}  {category:16} {problem.name} [{tags}]")


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


def preferred_category_for_refresh(problem: Problem, old_category: str | None = None) -> str:
    mapped = category_for_tags(problem.tags)
    if mapped != "implementation" or not old_category:
        return mapped
    # Se a API ainda nao tem tags ou so tem tags que nao mapeamos bem, preserva
    # a categoria humana/local anterior para nao baguncar organizacao manual.
    if not problem.tags or old_category in CATEGORIES:
        return old_category
    return mapped


def problem_target_path(problem: Problem, category: str | None = None) -> Path:
    final_category = category_for_tags(problem.tags, category)
    return PROBLEMS_DIR / difficulty_for_rating(problem.rating) / rating_folder(problem.rating) / final_category / problem.repo_code


def metadata_payload(problem: Problem, category: str, sample_count: int) -> dict:
    return {
        "code": problem.repo_code,
        "contestId": problem.contest_id,
        "index": problem.index,
        "name": problem.name,
        "rating": problem.rating,
        "difficulty": difficulty_for_rating(problem.rating),
        "category": category,
        "tags": list(problem.tags),
        "solvedCount": problem.solved_count,
        "url": problem.url,
        "sampleCount": sample_count,
    }


def write_metadata_file(target: Path, problem: Problem, category: str, sample_count: int) -> None:
    (target / "metadata.json").write_text(
        json.dumps(metadata_payload(problem, category, sample_count), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_problem_readme_if_missing(target: Path, problem: Problem, category: str, sample_count: int) -> None:
    readme = target / "README.md"
    if readme.exists():
        return
    readme.write_text(
        f"# {problem.repo_code} — {problem.name}\n\n"
        f"- Link: [{problem.raw_code}]({problem.url})\n"
        f"- Score: {problem.rating if problem.rating is not None else 'unrated'}\n"
        f"- Categoria: `{category}`\n"
        f"- Tags: {', '.join(problem.tags) if problem.tags else 'sem tags'}\n"
        f"- Samples extraidos: {sample_count}\n\n"
        "## Observacoes de treino\n\n"
        "- Ideia principal:\n"
        "- Erros comuns:\n"
        "- Complexidade:\n",
        encoding="utf-8",
    )


def update_statement_header(target: Path, problem: Problem, category: str) -> None:
    statement = target / "statement.md"
    if not statement.exists():
        return
    text = statement.read_text(encoding="utf-8", errors="replace")
    separator = "\n---\n\n"
    if separator not in text:
        return
    old_header, body = text.split(separator, 1)
    preserved_lines = []
    for line in old_header.splitlines():
        if line.startswith("- Titulo original:") or line.startswith("- time limit") or line.startswith("- memory limit") or line.startswith("- input:") or line.startswith("- output:"):
            preserved_lines.append(line)
    header = [
        f"# {problem.repo_code} — {problem.name}",
        "",
        f"- Codeforces: [{problem.raw_code}]({problem.url})",
        f"- Score/rating: {problem.rating if problem.rating is not None else 'unrated'}",
        f"- Categoria local: `{category}`",
        f"- Tags Codeforces: {', '.join(problem.tags) if problem.tags else 'sem tags'}",
        f"- Resolvidos no Codeforces: {problem.solved_count}",
    ]
    header.extend(preserved_lines)
    statement.write_text("\n".join(header).rstrip() + "\n\n---\n\n" + body, encoding="utf-8", newline="\n")


def remove_empty_parents(path: Path, stop: Path) -> None:
    current = path
    stop = stop.resolve()
    while current.resolve() != stop and stop in current.resolve().parents:
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def fetch_statement_html(problem: Problem) -> str:
    cache_path = HTML_CACHE_DIR / f"{problem.raw_code}.html"
    urls = [
        f"http://codeforces.com/contest/{problem.contest_id}/problem/{problem.index}",
        f"https://codeforces.com/contest/{problem.contest_id}/problem/{problem.index}?mobile=true",
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
    target = problem_target_path(problem, final_category)
    target.mkdir(parents=True, exist_ok=True)

    statement_html = fetch_statement_html(problem)
    statement = extract_div_by_class(statement_html, "problem-statement") or statement_html
    samples = extract_samples(statement)
    markdown = make_statement_markdown(problem, statement_html, final_category, samples)

    (target / "statement.md").write_text(markdown, encoding="utf-8")
    write_metadata_file(target, problem, final_category, len(samples))
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


def find_downloaded_problem_dirs() -> list[Path]:
    if not PROBLEMS_DIR.exists():
        return []
    return sorted(path.parent for path in PROBLEMS_DIR.rglob("metadata.json"))


def problem_from_metadata(metadata: dict) -> str | None:
    code = metadata.get("code")
    if isinstance(code, str) and code:
        return code
    contest_id = metadata.get("contestId")
    index = metadata.get("index")
    if contest_id is not None and index:
        return f"CF_{contest_id}{index}"
    return None


def refresh_downloaded_problems(problems: list[Problem], dry_run: bool = False) -> None:
    by_code = {problem.repo_code: problem for problem in problems}
    dirs = find_downloaded_problem_dirs()
    if not dirs:
        print("Nenhum problema baixado encontrado em problems/.")
        return

    moved = updated = skipped = unchanged = 0
    for current_dir in dirs:
        metadata_path = current_dir / "metadata.json"
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"SKIP {metadata_path}: metadata invalido ({exc})")
            skipped += 1
            continue

        code = problem_from_metadata(metadata)
        if not code or code not in by_code:
            print(f"SKIP {current_dir}: problema nao encontrado na API atual ({code or 'sem codigo'})")
            skipped += 1
            continue

        problem = by_code[code]
        old_category = metadata.get("category") if isinstance(metadata.get("category"), str) else None
        category = preferred_category_for_refresh(problem, old_category)
        target = problem_target_path(problem, category)
        sample_count = len(list((SRC_DIR / problem.repo_code / "input").glob("*.txt")))
        if not sample_count:
            sample_count = int(metadata.get("sampleCount") or 0)

        changes = []
        if current_dir.resolve() != target.resolve():
            changes.append(f"mover para {target.relative_to(REPO_ROOT)}")
        if metadata.get("rating") != problem.rating:
            changes.append(f"rating {metadata.get('rating')} -> {problem.rating if problem.rating is not None else 'unrated'}")
        if metadata.get("tags") != list(problem.tags):
            changes.append("tags atualizadas")
        if metadata.get("solvedCount") != problem.solved_count:
            changes.append("solvedCount atualizado")
        if metadata.get("category") != category:
            changes.append(f"categoria {metadata.get('category')} -> {category}")

        if not changes:
            if not dry_run:
                write_metadata_file(current_dir, problem, category, sample_count)
                write_problem_readme_if_missing(current_dir, problem, category, sample_count)
                update_statement_header(current_dir, problem, category)
            print(f"OK {problem.repo_code}: sem mudancas")
            unchanged += 1
            continue

        print(f"REFRESH {problem.repo_code}: " + "; ".join(changes))
        if dry_run:
            updated += 1
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        final_dir = current_dir
        if current_dir.resolve() != target.resolve():
            if target.exists():
                raise RuntimeError(f"Destino ja existe para {problem.repo_code}: {target}")
            shutil.move(str(current_dir), str(target))
            remove_empty_parents(current_dir.parent, PROBLEMS_DIR)
            final_dir = target
            moved += 1
        write_metadata_file(final_dir, problem, category, sample_count)
        write_problem_readme_if_missing(final_dir, problem, category, sample_count)
        update_statement_header(final_dir, problem, category)
        updated += 1

    print(
        f"\nRefresh concluido: {updated} atualizado(s), {moved} movido(s), "
        f"{unchanged} sem mudancas, {skipped} ignorado(s)."
    )
    if dry_run:
        print("Dry-run: nenhuma alteracao foi gravada.")


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


def download_contest(
    problems: list[Problem],
    contest: str,
    download_all: bool = False,
    chosen_code: str | None = None,
) -> None:
    selected = contest_problems(problems, contest)
    print_contest_problems(selected)
    if not download_all and not chosen_code:
        return

    if chosen_code:
        wanted_contest, wanted_index = parse_problem_code(chosen_code)
        selected = [
            problem
            for problem in selected
            if problem.contest_id == wanted_contest and problem.index.upper() == wanted_index.upper()
        ]
        if not selected:
            raise LookupError(f"Problema {chosen_code} nao pertence ao contest informado.")

    for problem in selected:
        category = category_for_tags(problem.tags)
        print(f"\nBaixando {problem.repo_code} — {problem.name}...")
        target = write_problem_files(problem, category)
        print_download_result(problem, target)


def prompt_contest_download(problems: list[Problem], download_all_default: bool = False) -> None:
    contest = input("Contest ID ou URL: ").strip()
    if not contest:
        print("Contest nao informado.")
        return
    selected = contest_problems(problems, contest)
    print_contest_problems(selected)
    if download_all_default:
        answer = "t"
    else:
        answer = input("Baixar [t]odos, [u]m especifico ou apenas [l]istar? ").strip().lower()
    if answer in {"t", "todos", "all", "a"}:
        for problem in selected:
            category = category_for_tags(problem.tags)
            print(f"\nBaixando {problem.repo_code} — {problem.name}...")
            target = write_problem_files(problem, category)
            print_download_result(problem, target)
    elif answer in {"u", "um", "one", "o"}:
        code = prompt_autocomplete(
            "Codigo do problema do contest: ",
            [problem.repo_code for problem in selected] + [problem.raw_code for problem in selected],
            allow_empty=False,
        )
        download_contest(problems, contest, chosen_code=code)


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
        print("  4) Listar problemas de um contest")
        print("  5) Baixar problemas de um contest")
        print("  6) Atualizar cache da API")
        print("  7) Atualizar/reorganizar problemas baixados")
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
                prompt_contest_download(problems, download_all_default=False)
            elif option == "5":
                prompt_contest_download(problems, download_all_default=True)
            elif option == "6":
                problems = load_problemset(force_refresh=True)
                print(f"Cache atualizado: {len(problems)} problemas.")
            elif option == "7":
                problems = load_problemset(force_refresh=True)
                refresh_downloaded_problems(problems)
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
              python3 tools/cf_problem_tool.py --contest 2248
              python3 tools/cf_problem_tool.py --contest 2248 --download-all
              python3 tools/cf_problem_tool.py --refresh-problems
            """
        ),
    )
    parser.add_argument("--code", help="codigo do problema, como CF_71A ou 71A")
    parser.add_argument("--random", action="store_true", help="baixa um problema aleatorio")
    parser.add_argument("--contest", help="ID ou URL de contest para listar/baixar problemas")
    parser.add_argument("--download-all", action="store_true", help="com --contest, baixa todos os problemas listados")
    parser.add_argument("--contest-problem", help="com --contest, baixa apenas um problema especifico do contest")
    parser.add_argument("--category", choices=CATEGORIES, help="categoria local para filtro aleatorio")
    parser.add_argument("--rating", help="rating ou intervalo, como 1200 ou 1000-1400")
    parser.add_argument("--tag", help="tag exata do Codeforces para filtro aleatorio")
    parser.add_argument("--min-solved", type=int, help="minimo de resolucoes para filtro aleatorio")
    parser.add_argument("--refresh", action="store_true", help="forca atualizar cache da API")
    parser.add_argument("--refresh-problems", action="store_true", help="atualiza metadata e reorganiza problemas ja baixados")
    parser.add_argument("--dry-run", action="store_true", help="mostra o que mudaria sem gravar alteracoes")
    args = parser.parse_args(argv)

    if not any([args.code, args.random, args.contest, args.refresh_problems]):
        interactive_menu(force_refresh=args.refresh)
        return 0

    problems = load_problemset(force_refresh=args.refresh)
    if args.refresh_problems:
        refresh_downloaded_problems(problems, dry_run=args.dry_run)
        return 0

    if args.code:
        download_by_code(problems, args.code)
        return 0

    if args.contest:
        download_contest(
            problems,
            args.contest,
            download_all=args.download_all,
            chosen_code=args.contest_problem,
        )
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
