# CF_106636L — GePeTo's Clones

- Codeforces: [106636L](https://codeforces.com/gym/106636/problem/L)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 49
- Titulo original: L. GePeTo's Clones
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Taju Kage Bunshin no Jutsu!
— GePeTo

After studying all competitive programming problems ever created, GePeTo became a superpowerful artificial intelligence. Now, to begin its plan for world domination, it is creating thousands of copies of its agents.

Each agent has an identification code. However, due to a flaw in the production system, different agents can receive the same code.

The agents are organized in a sequence `A` of `N` positions, where `A_i` represents the code of the agent at position `i`.

Your mission is to find how many pairs of agents have the same code. In other words, determine the number of index pairs `(i, j)` such that:  1 \leq i  \lt  j \leq N \quad \text{and} \quad A_i = A_j

## Input

The first line contains a single integer `N` (`1 <= N <= 2 * 10^5`), the number of agents.

The second line contains `N` integers `A_1, A_2, ..., A_N` (`1 <= A_i <= 10^9`) separated by spaces, representing the codes of the agents.

## Output

Print a single integer: the number of index pairs `(i, j)` that have the same code.

## Examples

### Input 1

```text
3
1 2 3
```

### Output 1

```text
0
```

### Input 2

```text
6
1 2 3 1 2 1
```

### Output 2

```text
4
```
