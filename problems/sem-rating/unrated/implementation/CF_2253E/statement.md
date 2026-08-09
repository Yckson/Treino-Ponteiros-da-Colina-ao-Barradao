# CF_2253E — Diameter Intersections

- Codeforces: [2253E](https://codeforces.com/problemset/problem/2253/E)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: brute force, dfs and similar, fft, graphs, trees
- Resolvidos no Codeforces: 822
- Titulo original: E. Diameter Intersections
- time limit per test: 4 seconds
- memory limit per test: 512 megabytes
- input: standard input
- output: standard output

---

You are given a tree with `n` vertices. The diameter of a tree is a simple path of maximum length in the tree. The length of a path is the number of edges it contains. The diameter of the given tree has odd length.

We call an integer `k` beautiful if it is possible to choose two diameters in this tree (possibly with the same endpoints; it is allowed to choose the same two diameters) such that their intersection contains exactly `k` edges.

Find all beautiful values of `k` and output them in increasing order.

## Input

The first line contains one integer `t` (`1 <= t <= 10^4`) — the number of test cases.

Each test case is given in the following format:

 -  the first line contains one integer `n` (`2 <= n <= 10^6`) — the number of vertices in the tree;
-  the next `n - 1` lines contain two integers `u` and `v` each (`1 <= u, v <= n`, `u != v`), denoting an edge between vertices `u` and `v`.
Additional constraints on the input:

 -  the sum of `n` over all test cases does not exceed `10^6`;
-  in each test case, the edges form a tree whose diameter has odd length.

## Output

For each test case, print one integer `m` — the number of beauitful values of `k`; then print the values of `k` themselves in increasing order.


## Examples

### Input

```text
5
2
1 2
4
1 2
2 3
3 4
6
1 2
1 3
1 4
2 5
2 6
10
1 2
1 3
3 5
1 4
4 6
2 7
7 9
2 8
8 10
9
1 2
1 3
3 5
1 4
4 6
2 7
7 8
7 9
```

### Output

```text
1 1
1 3
3 1 2 3
3 1 3 5
4 2 3 4 5
```

## Note

Consider the first three examples:

 -  in the first example, the pair of diameters `(1, 2)` and `(1, 2)` gives `k=1`;
-  in the second example, the pair of diameters `(1, 4)` and `(4, 1)` gives `k=3`;
-  in the third example, the pair of diameters `(6, 4)` and `(3, 5)` gives `k=1`; the pair of diameters `(6, 4)` and `(4, 5)` gives `k=2`; the pair of diameters `(6, 4)` and `(6, 4)` gives `k=3`.
