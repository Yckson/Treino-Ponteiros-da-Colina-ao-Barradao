# CF_106636F — Shelter Network

- Codeforces: [106636F](https://codeforces.com/gym/106636/problem/F)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 19
- Titulo original: F. Shelter Network
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

You call it a network of tunnels. I call it a tree that is ready for pruning.
— GePeTo

After GePeTo assumed control of the surface, the last members of the resistance were forced to hide underground.

To protect themselves from the robots, they built a network of tunnels connecting `N` underground points. The network was designed without redundant paths: between any two points, there is exactly one possible path.

The resistance's shelters are located at the extremities of this network, that is, at the vertices that have only one tunnel connected to them (the leaves of the tree).

To plan communication between the shelters, the resistance needs to answer `Q` queries. In each query, given an integer `X`, determine how many pairs of shelters are separated by exactly `X` tunnels.

## Input

The first line contains two integers `N` (`2 <= N <= 2 * 10^5`) and `Q` (`1 <= Q <= 10`), representing the number of points in the network and the number of queries, respectively.

Each of the next `N-1` lines contains two integers `u` and `v` (`1 <= u, v <= N`), indicating that there is a tunnel directly connecting vertices `u` and `v`. It is guaranteed that the given connections form a tree.

Each of the next `Q` lines contains a single integer `X` (`1 <= X <= N-1`), representing the query distance.

## Output

For each query, print a single integer: the number of unordered pairs of distinct shelters `(u, v)` whose distance is exactly `X`.

## Examples

### Input 1

```text
2 1
1 2
1
```

### Output 1

```text
1
```

### Input 2

```text
6 5
1 2
2 3
2 4
4 5
1 6
1
2
3
4
5
```

### Output 2

```text
0
0
2
1
0
```
