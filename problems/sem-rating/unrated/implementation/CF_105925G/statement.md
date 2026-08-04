# CF_105925G — Grover and His Special Paths

- Codeforces: [105925G](https://codeforces.com/gym/105925/problem/G)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 24
- Titulo original: G. Grover and His Special Paths
- time limit per test: 1.5 s
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Grover is an Indo-American computer scientist who wants to propose a quantum search algorithm that offers a quadratic speedup over classical search algorithms for unstructured databases. To achieve this, he needs to solve a problem in trees that is part of his research to develop his algorithm.

Grover has a tree with `N` vertices and `N - 1` undirected edges, and his goal is to assign a value `v_i` to each vertex satisfying some constraints:

 -  `1 <= v_i <= 5`
-  There are exactly `cnt_x` vertices with the value `v_i = x`, for `1 <= x <= 5`
-  For each vertex `i`, there is a set of values that the value of `v_i` can take
-  Additionally, in this tree, there are `P` special paths for Grover, where a special path is represented by a pair of vertices `(X_i, Y_i)` (the paths may intersect, and a path may appear more than once in the input) and for these paths, the values assigned to the vertices along the path (in the order from `X_i` to `Y_i`) must form a strictly increasing sequence.
If there is a valid solution, print any one that satisfies the constraint imposed by Grover; otherwise, print `-1`.

## Input

The first line of the input will contain an integer `N` (`1 <= N <= 5 * 10^4`), the number of vertices in the tree. The second line of the input will contain 5 integers, the values of `cnt_1, cnt_2, cnt_3, cnt_4, cnt_5` respectively. It is guaranteed that the sum `cnt_1 + cnt_2 + cnt_3 + cnt_4 + cnt_5 = N`.

The next `N` lines of input start with an integer `M_i` (`1 <= M_i <= 5`), followed by `M_i` distinct integers between 1 and 5, indicating the values that the `i`-th vertex can take. This is followed by `N - 1` lines, each with two numbers `U, V` (`1 <= U, V <= N`) indicating an edge of the tree.

Next, there will be a line with a single integer `P` (`1 <= P <= 5`), indicating the number of special paths. Finally, the next `P` lines of input will contain two numbers `X_i, Y_i` (`1 <= X_i, Y_i <= N`), indicating the special paths.

## Output

If a solution exists, print `N` integers `v_1, v_2, ..., v_n` indicating a valid solution to the problem. Otherwise, print `-1`. If there are multiple valid answers, any one will be accepted.

## Examples

### Input 1

```text
10
1 1 4 2 2
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 6
5 4
5 3
5 8
3 10
10 9
9 1
3 7
10 2
5
7 1
3 10
10 2
5 6
7 6
```

### Output 1

```text
5 4 2 3 3 5 1 3 4 3
```

### Input 2

```text
6
1 1 1 1 2
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
5 1 2 3 4 5
1 2
2 3
3 4
4 5
5 6
1
1 6
```

### Output 2

```text
-1
```

### Input 3

```text
1
0 0 0 0 1
4 1 2 3 4
1
1 1
```

### Output 3

```text
-1
```

### Input 4

```text
10
2 1 4 1 2
5 1 2 3 4 5
4 1 2 3 5
1 3
3 2 4 5
2 4 5
1 3
5 1 2 3 4 5
3 1 2 3
1 4
2 1 5
8 5
5 2
8 9
9 10
8 4
4 1
1 6
9 3
4 7
4
7 10
1 4
6 6
7 10
```

### Output 4

```text
1 3 3 2 5 3 1 3 4 5
```
