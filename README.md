# Ponteiros da Colina ao Barradão

<p align="center">
  <img src="docs/Ponteiros%20-%20da%20colina%20ao%20barradao.png" alt="Ponteiros: da Colina ao Barradão" width="420">
</p>

Repositório para organizar treinos de maratona de programação no padrão SBC, usando problemas do Codeforces como base.

A ideia é separar os problemas por dificuldade, rating e tema, mantendo também uma área de código-fonte com entradas e saídas esperadas para testar soluções rapidamente.

## Estrutura

```text
.
├── problems/
│   ├── iniciante/
│   │   ├── 800/
│   │   │   ├── strings/
│   │   │   ├── math/
│   │   │   └── implementation/
│   │   └── 900/
│   ├── facil/
│   │   ├── 1000/
│   │   ├── 1100/
│   │   └── 1200/
│   ├── medio/
│   │   ├── 1300/
│   │   ├── 1400/
│   │   ├── 1500/
│   │   └── 1600/
│   ├── dificil/
│   │   ├── 1700/
│   │   ├── 1800/
│   │   ├── 1900/
│   │   └── 2000/
│   └── avancado/
│       ├── 2100/
│       ├── 2200/
│       ├── 2300/
│       ├── 2400/
│       └── 2500+/
├── src/
│   └── CF_71A/
│       ├── main.cpp
│       ├── input/
│       │   └── sample1.txt
│       └── output/
│           └── sample1.txt
├── templates/
│   └── main.cpp
└── Makefile
```

## Convenção para cadastrar problemas

Use um código único para cada problema:

```text
CF_<contest><letra>
```

Exemplos:

- `CF_71A`
- `CF_231A`
- `CF_1399C`

Para cada problema, crie:

```text
problems/<dificuldade>/<rating>/<categoria>/<codigo>/
src/<codigo>/
```

Dentro da pasta em `problems`, coloque posteriormente o PDF do enunciado e, se quiser, um `README.md` com observações, tags e links.

Dentro da pasta em `src`, coloque a solução e os casos de teste:

```text
src/<codigo>/
├── main.cpp
├── input/
│   ├── sample1.txt
│   └── sample2.txt
└── output/
    ├── sample1.txt
    └── sample2.txt
```

Os arquivos de entrada e saída precisam ter o mesmo nome-base. Por exemplo:

- `input/sample1.txt`
- `output/sample1.txt`

## Comandos

Criar a pasta de uma nova solução a partir do template:

```bash
make new PROB=CF_71A
```

Compilar:

```bash
make build PROB=CF_71A
```

Rodar todos os casos de teste existentes:

```bash
make test PROB=CF_71A
```

Compilar e testar:

```bash
make run PROB=CF_71A
```

Rodar manualmente com entrada padrão:

```bash
make exec PROB=CF_71A < entrada.txt
```

Remover binários gerados:

```bash
make clean
```

Listar problemas com código-fonte:

```bash
make list
```

## Categorias sugeridas

As categorias iniciais foram escolhidas pensando em trilhas comuns de treino SBC/ICPC:

- `implementation`
- `strings`
- `math`
- `greedy`
- `sorting`
- `binary-search`
- `two-pointers`
- `data-structures`
- `graphs`
- `dp`
- `geometry`
- `combinatorics`

Nem todo rating precisa ter todas as categorias no começo. A árvore inicial já vem com as principais, e novas categorias podem ser criadas conforme os treinos amadurecem.

## Ferramenta Codeforces

A ferramenta [`tools/cf_problem_tool.py`](tools/cf_problem_tool.py) usa a API pública do Codeforces para buscar metadados dos problemas e baixa o enunciado/samples da página pública do problema.

Abrir o menu interativo:

```bash
make cf-tool
```

Baixar pelo código do problema:

```bash
make cf-download PROB=CF_71A
```

Escolher um problema aleatório por filtros interativos:

```bash
make cf-random
```


Listar problemas de um contest:

```bash
make cf-contest CONTEST=2248
```

Baixar todos os problemas de um contest:

```bash
make cf-contest-download CONTEST=2248
```

Baixar um problema específico de um contest:

```bash
make cf-contest-problem CONTEST=2248 PROB=CF_2248A
```

Também é possível passar a URL inteira:

```bash
python3 tools/cf_problem_tool.py --contest https://codeforces.com/contest/2248 --download-all
```

Problemas de contests recentes podem ainda não ter rating oficial. Nesses casos, eles ficam temporariamente em:

```text
problems/sem-rating/unrated/<categoria>/<codigo>/
```


Atualizar metadados e reorganizar problemas já baixados:

```bash
make cf-refresh-problems
```

Antes de mover qualquer pasta, você pode simular:

```bash
make cf-refresh-problems-dry
```

Esse comando é útil para problemas baixados enquanto um contest ainda estava sem rating. Quando a API passar a informar o rating, a pasta sai de `problems/sem-rating/unrated/...` e vai para o caminho correspondente, como `problems/facil/1200/...`. O comando não mexe em `src/<codigo>/`.


Também é possível usar argumentos diretamente:

```bash
python3 tools/cf_problem_tool.py --random --category dp --rating 1300-1600
```

Ao baixar um problema, a ferramenta cria/atualiza:

```text
problems/<dificuldade>/<rating>/<categoria>/<codigo>/statement.md
problems/<dificuldade>/<rating>/<categoria>/<codigo>/metadata.json
src/<codigo>/main.cpp
src/<codigo>/input/sampleN.txt
src/<codigo>/output/sampleN.txt
```

## Materiais de treino

- [Catálogo inicial de problemas](docs/problem-catalog.md)
- [Roadmap de treino](docs/roadmap.md)
