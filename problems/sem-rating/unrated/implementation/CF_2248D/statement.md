# CF_2248D — Good Pair Queries

- Codeforces: [2248D](https://codeforces.com/problemset/problem/2248/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: constructive algorithms
- Resolvidos no Codeforces: 4067
- Titulo original: D. Good Pair Queries
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

You are given two binary strings `s` and `t`, both of length `n`.

For two binary strings `a` and `b` of the same length, the pair `(a, b)` is called good if both strings can be made empty by performing the following operation zero or more times:

 -  Choose a non-empty set of positions `1 <= i_1 \lt i_2 \lt ... \lt i_k <= |a|` and a character `c \in \{\mathtt{0}, \mathtt{1}\}`.
-  Let `x = a_{i_1}a_{i_2}... a_{i_k}` and `y = b_{i_1}b_{i_2}... b_{i_k}`.
-  The character `c` must be a mode`^{\text{∗}}` of both `x` and `y`.
-  Delete the characters at the chosen positions from both strings. The remaining characters are concatenated without changing their relative order.
A binary string may have both `\mathtt{0}` and `\mathtt{1}` as modes.

You need to answer `q` queries. In each query, you are given two integers `l` and `r`. Determine whether the pair of substrings `(s_l s_{l+1} ... s_r, t_l t_{l+1} ... t_r)` is good.

The queries are independent.

`^{\text{∗}}`For a binary string `z`, a character `c` is a mode if it appears at least `<=ft\lceil \frac{|z|}{2} \right\rceil` times in `z`. Here, `\lceil x \rceil` denotes the smallest integer greater than or equal to `x`.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains two integers `n` and `q` (`1 <= n, q <= 2 * 10^5`) — the length of each string and the number of queries.

The second line of each test case contains the binary string `s` of length `n`.

The third line of each test case contains the binary string `t` of length `n`.

Each of the next `q` lines contains two integers `l` and `r` (`1 <= l <= r <= n`) — a query.

It is guaranteed that the sum of `n` over all test cases does not exceed `2 * 10^5`.

It is guaranteed that the sum of `q` over all test cases does not exceed `2 * 10^5`.

## Output

For each query, output "YES" if the pair `(s_l s_{l+1} ... s_r, t_l t_{l+1} ... t_r)` is good. Otherwise, output "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.


## Examples

### Input

```text
3
2 2
01
10
1 1
1 2
5 1
11111
11111
1 3
5 1
00011
01111
1 5
```

### Output

```text
NO
YES
YES
YES
```

## Note

In the first test case, for the first query, the pair is `(\mathtt{0}, \mathtt{1})`. No character is a mode of both strings, so no operation can be performed.

For the second query, choose both positions and `c = \mathtt{0}`. Then `x = \mathtt{01}` and `y = \mathtt{10}`, so `c` is a mode of both strings and the whole pair is deleted.

In the third test case, neither character is a mode of both `\mathtt{00011}` and `\mathtt{01111}`, so the whole pair cannot be deleted in one operation. It can be emptied in three operations:

 -  Choose positions `2` and `4` and `c = \mathtt{1}`. Then `x = \mathtt{01}` and `y = \mathtt{11}`, so `c` is a mode of both `x` and `y`. After deleting the selected positions, the remaining characters are concatenated, giving the pair `(\mathtt{001}, \mathtt{011})`.
-  Choose positions `1` and `2` and `c = \mathtt{0}`. Then `x = \mathtt{00}` and `y = \mathtt{01}`, so `c` is a mode of both `x` and `y`. After deleting the selected positions, the pair becomes `(\mathtt{1}, \mathtt{1})`.
-  Choose the remaining position `1` and `c = \mathtt{1}`. Then `x = \mathtt{1}` and `y = \mathtt{1}`, so `c` is a mode of both `x` and `y`. Deleting the selected position makes both strings empty.
