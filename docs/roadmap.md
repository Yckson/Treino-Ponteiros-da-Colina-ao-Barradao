# Roadmap de treino para maratona de programação

Este roteiro é pensado para um time começando ou se organizando para competições no estilo SBC/ICPC: treino em grupo, velocidade de implementação, leitura sob pressão e upsolve disciplinado.

## Princípios

1. Aprender algoritmo dentro de problema, não em isolamento. Se travou e o editorial usa uma ideia nova, leia uma referência curta, implemente no mesmo problema e registre uma frase do aprendizado.
2. Treinar no intervalo em que o time resolve cerca de 30% a 40% dos problemas sozinho. Se todo mundo acerta tudo, está confortável demais; se ninguém sai do lugar, está alto demais.
3. Todo problema precisa terminar em código. Ideia sem implementação é só poesia bonita — útil, mas não passa no judge.
4. Toda semana precisa ter upsolve. O treino real começa quando o placar fecha.

## Fase 0 — Preparação do ambiente, 1 semana

Objetivo: todos usam o mesmo fluxo de treino.

- Revisar C++17, entrada/saída rápida, `vector`, `string`, `pair`, `map`, `set`, `queue`, `stack`, `priority_queue`.
- Cada pessoa deve criar e rodar pelo menos 3 problemas usando `make new PROB=...` e `make run PROB=...`.
- Criar o hábito de guardar exemplos em `src/<codigo>/input` e `src/<codigo>/output`.

Problemas sugeridos: categorias `implementation`, `strings`, `math`, scores 800-1000.

## Fase 1 — Base competitiva, semanas 2 a 5

Objetivo: resolver A/B/C fáceis com consistência.

Temas:

- implementation
- strings
- math básica
- sorting
- greedy

Rotina semanal:

- 2 treinos curtos de 90 minutos, 3 a 5 problemas cada.
- 1 treino individual de upsolve.
- 1 mini-contest misto de 2 horas, sem tags visíveis.

Meta de saída: cada integrante resolve problemas 800-1100 com pouca ajuda e consegue explicar a solução em voz alta.

## Fase 2 — Técnicas lineares e busca, semanas 6 a 9

Objetivo: reduzir força bruta e reconhecer monotonicidade.

Temas:

- binary-search
- two-pointers
- prefix sums / difference arrays
- data structures básicas (`map`, `set`, heap)
- greedy com ordenação

Rotina semanal:

- 1 sessão teórica curta de 30 minutos antes dos problemas.
- 6 a 10 problemas por semana nos scores 1100-1400.
- 1 contest virtual Div. 3 ou Div. 4.

Meta de saída: reconhecer quando uma resposta é monotônica, quando uma janela pode andar sem voltar e quando ordenação troca um problema quadrático por linear/logarítmico.

## Fase 3 — Grafos e DP inicial, semanas 10 a 15

Objetivo: formar o núcleo técnico de SBC/ICPC.

Temas:

- BFS/DFS
- componentes conexos
- árvores
- DSU
- caminhos mínimos básicos
- DP 1D/2D
- knapsack e DP por escolha

Rotina semanal:

- 1 treino focado em grafos.
- 1 treino focado em DP.
- 1 contest virtual de 2h30 a 3h.
- Upsolve obrigatório de pelo menos 2 problemas por pessoa.

Meta de saída: implementar DFS/BFS/DSU sem template externo e modelar problemas simples como grafo ou estado de DP.

## Fase 4 — Consolidação intermediária, semanas 16 a 22

Objetivo: ficar competitivo em problemas 1400-1700 e montar estratégia de time.

Temas:

- DP intermediária
- grafos com estados
- shortest paths
- combinatória básica/modular
- geometria básica
- estruturas como Fenwick/Segment Tree, quando aparecerem naturalmente

Rotina semanal:

- 1 contest virtual ICPC-style de 3 a 5 horas, com 8 a 12 problemas.
- 1 sessão de pós-contest: classificar erros em leitura, ideia, implementação, teste ou tempo.
- 1 sessão de treino por categoria fraca do time.

Meta de saída: o time escolhe bem a ordem dos problemas, divide tarefas sem duplicar trabalho e faz upsolve com registro.

## Fase 5 — Pré-competição, últimas 4 a 6 semanas

Objetivo: simular pressão real.

Rotina:

- 1 simulado completo por semana no estilo ICPC/SBC.
- 1 treino de velocidade com problemas 800-1300.
- 1 treino técnico com problemas 1500-1900.
- Revisão de templates: BFS, DFS, DSU, Dijkstra, Fenwick/Segment Tree, combinatória modular, geometria básica.

Durante o simulado:

- Primeiros 10-15 minutos: leitura geral e marcação de problemas prováveis.
- Resolver primeiro os problemas de alta confiança.
- Se uma pessoa travar por 25-35 minutos sem progresso, trocar de problema ou pedir revisão rápida.
- Registrar submissões erradas e motivo real, não só “bug”.

## Métricas simples para acompanhar

- Problemas resolvidos por semana por pessoa.
- Taxa de AC no primeiro envio.
- Tempo médio até primeira solução no simulado.
- Quantidade de upsolves concluídos.
- Categorias com maior taxa de erro.

## Fontes e referências

- [Codeforces API `problemset.problems`](https://codeforces.com/api/problemset.problems): ratings, tags e estatísticas do catálogo.
- [Codeforces — Competitive Programming Roadmap, por TheScrasse](https://codeforces.com/blog/entry/111099): reforça a ideia de montar uma base de problemas “standard-ish” e treinar tanto reconhecimento quanto raciocínio.
- [Codeforces — Smart Practice Guide](https://codeforces.com/blog/entry/149974): rotina baseada em faixa de dificuldade adequada, implementação obrigatória e upsolve.
- [Codeforces — A way to Practice Competitive Programming](https://codeforces.com/blog/entry/66909): progressão por faixas de rating.
- [USACO Guide](https://usaco.guide/): roteiro organizado por tópicos, recursos curados e listas de problemas.
- [CP-Algorithms](https://cp-algorithms.com/): referência técnica para algoritmos e estruturas clássicas.
