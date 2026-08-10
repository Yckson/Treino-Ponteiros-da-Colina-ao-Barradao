# CF_2256F — How Long Until Nothing Remains?

- Codeforces: [2256F](https://codeforces.com/contest/2256/problem/F)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 0
- Titulo original: F. How Long Until Nothing Remains?
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Before her final sortie, Chtholly asks Willem three questions.

The first is this: if the end is inevitable, how long will it take until nothing remains?

Willem cannot answer her directly. Instead, he writes down `n` positive integers `a_1,a_2,...,a_n`.

Each operation takes one second. In one operation, Willem does the following:

 -  Choose an index `p` (`1<= p<= n`);
-  Then, replace `a_p` with `<=ft\lfloor\dfrac{a_p}{2}\right\rfloor`, and for every `i!= p`, replace `a_i` by `<=ft\lceil\dfrac{a_i}{2}\right\rceil`. All replacements are performed simultaneously.
Find the minimum number of seconds needed to make all `n` integers equal to `0`.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains one integer `n` (`1<= n<=2*10^5`) — the number of integers.

The second line of each test case contains `n` integers `a_1,a_2,...,a_n` (`1<= a_i<=10^9`) — the initial integers.

It is guaranteed that the sum of `n` over all test cases does not exceed `2*10^5`.

## Output

For each test case, output a single integer — the minimum number of seconds needed to make all integers equal to `0`.


## Examples

### Input

```text
5
1
3
3
1 1 1
3
1 2 4
2
5 2
6
1 2 3 4 5 6
```

### Output

```text
2
3
3
3
6
```

## Note

In the first test case, the only integer changes as `3\to1\to0`, so the answer is `2`.

In the second test case, an integer equal to `1` becomes `0` only when its index is chosen. Thus, at least `3` seconds are necessary, and choosing every index once is sufficient.

In the third test case, an optimal sequence is:

 -  Choose `p=1`: `[1,2,4]\to[0,1,2]`;
-  Choose `p=2`: `[0,1,2]\to[0,0,1]`;
-  Choose `p=3`: `[0,0,1]\to[0,0,0]`.
In the fourth test case, an optimal sequence is `[5,2]\to[2,1]\to[1,0]\to[0,0]`, where the chosen indices are `1`, `2`, and `1`.
