# CF_2253F — 4-beauty

- Codeforces: [2253F](https://codeforces.com/problemset/problem/2253/F)
- Score/rating: unrated
- Categoria local: `dp`
- Tags Codeforces: bitmasks, dp, graphs, math
- Resolvidos no Codeforces: 199
- Titulo original: F. 4-beauty
- time limit per test: 5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

For a set of integers `S`, define its divisibility characteristic as the number of ordered pairs `(x, y)` such that `x != y`, `x` and `y` belong to `S`, and `x` is divisible by `y`.

For a set of integers `A`, define its `4`-beauty as follows:

 -  consider all sets of four distinct numbers that belong to `A` and form an arithmetic progression;
-  find the maximum divisibility characteristic among all such sets.
If there are no suitable sets of four numbers, then the `4`-beauty equals `0`.

Initially, the set `\{1, 2, ..., n\}` is given. You may remove numbers from it. Removing the number `i` costs `m_i` coins.

Calculate the minimum number of coins you have to spend in order to decrease the `4`-beauty of the set.

## Input

The first line contains one integer `n` (`4 <= n <= 5 * 10^5`) — the number of elements in the initial set.

The second line contains `n` integers `m_1, m_2, ..., m_n` (`1 <= m_i <= 10^9`), where `m_i` is the cost of removing the number `i`.

## Output

Print one integer — the minimum number of coins you have to spend in order to decrease the `4`-beauty of the set. It can be shown that it is always possible.


## Examples

### Input 1

```text
4
5 3 7 2
```

### Output 1

```text
2
```

### Input 2

```text
5
1 100 100 100 1
```

### Output 2

```text
1
```

### Input 3

```text
8
2 10 100 10 100 3 100 100
```

### Output 3

```text
5
```

### Input 4

```text
10
9 9 7 4 8 2 6 5 1 10
```

### Output 4

```text
4
```

## Note

In the first example, the only arithmetic progression of four numbers is `1, 2, 3, 4`. Its divisibility characteristic equals `4`. It is sufficient to remove the number `4`, paying `2` coins.

In the second example, it is sufficient to remove the number `1`.

In the third example, it is optimal to remove the numbers `1` and `6`, paying `2+3=5` coins.
