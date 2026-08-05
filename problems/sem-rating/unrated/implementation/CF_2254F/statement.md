# CF_2254F — Whiplash

- Codeforces: [2254F](https://codeforces.com/problemset/problem/2254/F)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: bitmasks, constructive algorithms, math
- Resolvidos no Codeforces: 976
- Titulo original: F. Whiplash
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Yousef has given you an even integer `n` and two arrays, `a` and `b`, both consisting of `n` non-negative integers.

You can perform the following operation on array `a` any number of times (possibly zero):

 -  Choose an index `i` (`1 <= i <= n`).
-  For all `j` such that `1 <= j <= n` and `j != i`, replace `a_j` with `a_j \oplus a_i`. (Here, `\oplus` denotes the bitwise XOR operation).
-  The element `a_i` remains unchanged.
Determine whether it is possible to transform array `a` into array `b` using a finite number of operations.

## Input

The first line contains an integer `t` (`1 <= t <= 10^4`) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an even integer `n` (`2 <= n <= 2 * 10^5`) — the length of the array.

The second line of each test case contains `n` integers `a_1, a_2, ..., a_n` (`0 <= a_i \lt 2^{30}`) — the elements of the array `a`.

The third line of each test case contains `n` integers `b_1, b_2, ..., b_n` (`0 <= b_i \lt 2^{30}`) — the elements of the array `b`.

It is guaranteed that the sum of `n` over all test cases does not exceed `2 * 10^5`.

## Output

For each test case, output "YES" if the array `a` can be transformed into array `b` using a finite number of operations, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.


## Examples

### Input

```text
6
2
1 2
1 0
4
1 2 4 7
6 7 5 3
4
1 2 4 8
8 4 2 1
4
1 2 3 4
1 2 4 5
4
1 2 0 3
3 3 0 3
6
3 5 6 9 10 12
6 5 3 12 15 9
```

### Output

```text
NO
YES
YES
NO
NO
YES
```

## Note

In the first test case, starting from `[1, 2]`, there is no sequence of operations that ends at `[1, 0]`, so the answer is "NO".

In the second test case, one valid sequence is:

 -  Choose index `2`, `[1, {\color{blue}{2}}, 4, 7] \rightarrow [3, {\color{blue}{2}}, 6, 5]`.
-  Choose index `3`, `[3, 2, {\color{blue}{6}}, 5] \rightarrow [5, 4, {\color{blue}{6}}, 3]`.
-  Choose index `4`, `[5, 4, 6, {\color{blue}{3}}] \rightarrow [6, 7, 5, {\color{blue}{3}}]`.
In the third test case, one valid sequence is:

 -  Choose index `1`, `[\color{blue}{1}, 2, 4, 8] \rightarrow [\color{blue}{1}, 3, 5, 9]`.
-  Choose index `2`, `[1, \color{blue}{3}, 5, 9] \rightarrow [2, \color{blue}{3}, 6, 10]`.
-  Choose index `3`, `[2, 3, \color{blue}{6}, 10] \rightarrow [4, 5, \color{blue}{6}, 12]`.
-  Choose index `2`, `[4, \color{blue}{5}, 6, 12] \rightarrow [1, \color{blue}{5}, 3, 9]`.
-  Choose index `4`, `[1, 5, 3, \color{blue}{9}] \rightarrow [8, 12, 10, \color{blue}{9}]`.
-  Choose index `1`, `[\color{blue}{8}, 12, 10, 9] \rightarrow [\color{blue}{8}, 4, 2, 1]`.
