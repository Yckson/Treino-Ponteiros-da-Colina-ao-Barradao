# CF_2248F — Matrix Elimination

- Codeforces: [2248F](https://codeforces.com/problemset/problem/2248/F)
- Score/rating: 2500
- Categoria local: `binary-search`
- Tags Codeforces: binary search, greedy, math
- Resolvidos no Codeforces: 386
- Titulo original: F. Matrix Elimination
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

You are given an integer `k` and a matrix `v` with `n` rows and `m` columns. The element in row `i` and column `j` is denoted by `v_{i,j}`.

A cell `(x, y)` is called a peak if its value is greater than or equal to the sum of the values in all other cells in row `x` and column `y`. Formally, `(x, y)` is a peak if

 v_{x,y} \ge \sum_{\substack{1 \le i \le n \\i \neq x}} v_{i,y} + \sum_{\substack{1 \le j \le m \\j \neq y}} v_{x,j}.

You may perform the following operation any number of times (possibly zero):

 -  Choose four integers `x_l`, `x_r`, `y_l`, and `y_r` (`1 <= x_l <= x_r <= n`, `1 <= y_l <= y_r <= m`).
-  Subtract `1` from `v_{i,j}` for every `x_l <= i <= x_r` and `y_l <= j <= y_r`.
Find the minimum number of operations required to obtain a matrix with at least `k` peaks.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains three integers `n`, `m`, and `k` (`1 <= n, m <= 10^5`, `1 <= k <= n * m`, `n * m <= 10^5`) — the number of rows, the number of columns, and the required number of peaks.

The `i`-th of the next `n` lines contains `m` integers `v_{i,1}, v_{i,2}, ..., v_{i,m}` (`-10^9 <= v_{i,j} <= 10^9`).

It is guaranteed that the sum of `n * m` over all test cases does not exceed `10^5`.

## Output

For each test case, output a single integer — the minimum number of operations required to obtain at least `k` peaks.

If there is no solution, print a single integer `-1`.


## Examples

### Input

```text
16
3 3 7
-1 -30 7
6 -3 22
1 -18 16
3 1 2
100000000
300000000
200000000
1 3 1
2 3 4
1 3 1
1 2 3
1 2 2
5 7
5 2 8
531959596 -61416172
425363565 672913308
981527099 451180253
-161687136 898803495
-388356105 897723313
1 1 1
0
1 1 1
-5
1 4 3
-8 -4 4 -11
1 9 5
-12 -4 -13 9 -1 -15 6 -15 -4
1 3 3
-12 -15 8
1 5 5
10 8 -4 0 -4
1 3 3
12 9 -1
1 3 3
-14 11 -6
1 6 6
-1 0 15 3 1 -14
1 2 2
1000000000 -1000000000
```

### Output

```text
2
100000000
1
0
2
734592698
0
-1
0
0
11
6
12
11
7
2000000000
```

## Note

For the first test case, you can perform the following two operations:

 -  choose `(x_l, x_r, y_l, y_r) = (1, 3, 2, 3)`;
-  choose `(x_l, x_r, y_l, y_r) = (2, 3, 1, 3)`.
After these operations, the matrix will be:

 `\color{green}{-1}``-31``\color{green}{6}``5``\color{green}{-5}``\color{green}{20}``\color{green}{0}``\color{green}{-20}``\color{green}{14}` The seven peaks are highlighted in green. For example:

 -  The cell `(1, 1)` is a peak because `-1 >= 5 + 0 - 31 + 6 = -20`;
-  The cell `(3, 1)` is a peak because `0 >= -20 + 14 - 1 + 5 = -2`;
-  The cell `(2, 1)` is not a peak because `5 \lt -5 + 20 - 1 + 0 = 14`.
It can be shown that fewer than two operations cannot create seven peaks, so the answer is `2`.

In the eighth test case, the only cell has value `-5`. A cell in a `1 * 1` matrix is a peak if and only if its value is non-negative. Since every operation only decreases its value, it is impossible to make it a peak.

For the last test case, both cells are peaks exactly when their values are equal. Therefore, the first cell must be decreased from `10^9` to `-10^9`, which requires `2 * 10^9` operations.
