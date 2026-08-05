# CF_2248E — Excuse for Breaks

- Codeforces: [2248E](https://codeforces.com/problemset/problem/2248/E)
- Score/rating: 1900
- Categoria local: `binary-search`
- Tags Codeforces: binary search, brute force, greedy, math, two pointers
- Resolvidos no Codeforces: 1527
- Titulo original: E. Excuse for Breaks
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

You are given three integers `n`, `m`, and `d`, and two arrays `p_1, p_2, ..., p_m` and `r_1, r_2, ..., r_m`. The array `p` is strictly increasing.

For a binary array `a` of any positive finite length (so `|a|` need not equal `n`), define its value `f(a)` using the following pseudocode:

function f(a):
    v := 0
    c := 0
    for i from 1 to length(a):
        if a[i] is equal to 1:
            v := v + d
            c := c + 1
        else:
            c := 0
        for j from 1 to m:
            if c is equal to p[j]:
                v := v + r[j]
        if c is equal to n:
            c := 0
    return v
 Here, ":=" denotes the assignment operation.Let `I(a)` denote the array `[1,1,...,1]` of length `|a|`. In other words, `I(a)` consists of `|a|` ones.

Determine whether there exists a binary (consisting only of zeros and ones) array `a` such that `f(a) \gt f(I(a))`.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 2000`). The description of the test cases follows.

The first line of each test case contains three integers `n`, `m`, and `d` (`1 <= n <= 10^9`, `0 <= m <= 2000`, `0 <= d <= 10^9`).

The `i`-th of the next `m` lines contains two integers `p_i` and `r_i` (`1 <= p_i <= n`, `1 <= r_i <= 10^9`).

The array `p` is strictly increasing.

It is guaranteed that the sum of `m` over all test cases does not exceed `2000`.

## Output

For each test case, output "YES" if such a binary array `a` exists, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.


## Examples

### Input

```text
3
6 4 3
2 5
3 9
4 1
5 3
7 3 5
2 5
4 5
7 10
684492057 3 386217943
367971233 991739271
612599954 429216213
684492056 402931836
```

### Output

```text
YES
NO
YES
```

## Note

In the first test case, you can choose `a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]`.

The array `a` contains `16` ones, so the total contribution of `d` is `16 * 3 = 48`. Its runs of consecutive ones have lengths `9`, `4`, and `3`. The corresponding total rewards are `32`, `15`, and `14`, respectively. Therefore, `f(a) = 48 + 32 + 15 + 14 = 109`.

Moreover, `I(a)` consists of `18` ones. During the computation of `f(I(a))`, they form three complete blocks of `6` ones, and each block contributes `6 * 3 + 5 + 9 + 1 + 3 = 36`. Thus, `f(I(a)) = 3 * 36 = 108`. Since `f(a) \gt f(I(a))`, the answer is "YES".

In the second test case, no binary array `a` satisfies `f(a) \gt f(I(a))`, so the answer is "NO".
