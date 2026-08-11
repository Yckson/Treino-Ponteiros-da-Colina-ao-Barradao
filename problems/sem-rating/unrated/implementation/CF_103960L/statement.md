# CF_103960L — Listing Tedious Paths

- Codeforces: [103960L](https://codeforces.com/gym/103960/problem/L)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 553
- Titulo original: L. Listing Tedious Paths
- time limit per test: 1 s
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

A tree is a graph that is connected (there exists a path between any two of its vertices), undirected (the edges of the graph have no direction), and acyclic (there are no cycles).

A colorful tree is a tree in which each of its vertices has a specific color.

A tedious path is a path in the tree such that both the initial and final vertices have the same color, and there is no vertex or edge that appear more than once in the path. Note that the color of the intermediate vertices, if there are any, are irrelevant.

Given a colorful tree, with `N` vertices, your task is calculate, for each of the edges, the number of tedious paths that go through that edge.

## Input

The first line contains the number of vertices `N` (`2 <= N <= 10^5`). The second line contains `N` integers `C_1, ..., C_N`, where `C_i` (`1 <= C_i <= N`) represents the color of the vertex `i`. The next `N - 1` lines contains two integers each, `u` and `v`, representing an edge (`1 <= u, v <= N` and `u != v`). It's guaranteed that the given graph is a tree.

## Output

Print `N-1` integers, representing the number of tedious paths that go through each edge, following the same order of the edges as they are given in the input.

## Examples

### Input 1

```text
6
1 1 1 2 2 1
1 2
2 3
4 6
2 4
1 5
```

### Output 1

```text
4 3 3 4 1
```

### Input 2

```text
12
1 2 3 1 2 2 1 3 2 3 1 2
1 2
2 3
2 4
4 5
4 6
1 7
7 8
7 9
9 10
6 11
6 12
```

### Output 2

```text
10 2 10 4 9 9 2 6 2 3 4
```
