# CF_2254E — Chronostasis

- Codeforces: [2254E](https://codeforces.com/problemset/problem/2254/E)
- Score/rating: unrated
- Categoria local: `binary-search`
- Tags Codeforces: binary search, data structures, greedy
- Resolvidos no Codeforces: 3603
- Titulo original: E. Chronostasis
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Yousef has a hidden array `a` of length `n` consisting entirely of strictly positive integers.

An operation was performed exactly once to create an array `b`:

 -  Set `b_1 = a_1`.
-  For every `i` from `2` to `n`, set `b_i = a_i - a_{i-1}`.
-  After this, the elements of `b` were completely shuffled.
You are given the shuffled array `b`. Reconstruct the lexicographically smallest original array `a`. If it's impossible for any arrangement of `b` to produce an array `a` of strictly positive integers, output `-1`.

## Input

The first line of input contains an integer `t` (`1 <= t <= 10^4`) — the number of test cases.

The first line of each test case contains an integer `n` (`1 <= n <= 2 * 10^5`) — the size of the array.

The second line of each test case contains `n` integers `b_1, b_2, ..., b_n` (`-10^9 <= b_i <= 10^9`) — the elements of the shuffled array `b`.

It is guaranteed that the sum of `n` over all test cases does not exceed `2 * 10^5`.

## Output

For each test case, output `n` strictly positive integers `a_1, a_2, ..., a_n` (`a_i >= 1`) — the lexicographically smallest original array `a`. If it's impossible to create a valid array `a`, output `-1` instead.


## Examples

### Input

```text
8
1
5
4
-5 2 1 1
6
-3 4 2 -1 1 0
6
-2 -2 4 1 0 1
7
0 0 -2 3 0 -1 2
8
-1 -1 -1 -1 5 0 0 1
5
1000000000 500000000 750000000 100000000 900000000
10
1000000000 -1000000000 500000000 -500000000 1 1 -1 -1 2 -2
```

### Output

```text
5
-1
1 1 3 2 6 3
1 1 2 6 4 2
2 1 1 1 1 4 2
1 1 1 6 5 4 3 2
100000000 600000000 1350000000 2250000000 3250000000
-1
```

## Note

In the first test case, the only valid array is `a = [5]`.

In the second test case, there is no valid arrangement of the elements of `b` that reconstructs an array `a` consisting entirely of strictly positive integers. Therefore, the answer is `-1`.

In the third test case, one valid arrangement reconstructs the array `a=[1,1,3,2,6,3]`. The resulting sequence of differences `[1, 0, 2, -1, 4, -3]` is a permutation of the given array `b`, and among all valid reconstructions, this array is lexicographically smallest.
