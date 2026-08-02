# CF_2248C — Maximize the Score

- Codeforces: [2248C](https://codeforces.com/problemset/problem/2248/C)
- Score/rating: unrated
- Categoria local: `dp`
- Tags Codeforces: dp, greedy
- Resolvidos no Codeforces: 5449
- Titulo original: C. Maximize the Score
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

You are given an array `a` of length `2n`. Each integer from `1` to `n` occurs exactly twice in `a`.

Initially, your score is `0`.

You can repeatedly perform the following operation while `a` is non-empty:

 -  Choose an integer `x` that is present in `a`.
-  Let `l` and `r` be the indices of the leftmost and rightmost occurrences of `x` in the current array, respectively. If `x` occurs only once, then `l = r`.
-  Add `(r - l + 1)^2` to your score.
-  Delete the elements `a_l, a_{l + 1}, ..., a_r` from `a`. The remaining elements are concatenated without changing their order and re-indexed starting from `1`.
Find the maximum possible score after making the array empty.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains a single integer `n` (`1 <= n <= 2 * 10^5`).

The second line contains `2n` integers `a_1, a_2, ..., a_{2n}` (`1 <= a_i <= n`).

It is guaranteed that each integer from `1` to `n` occurs exactly twice in `a`.

It is guaranteed that the sum of `n` over all test cases does not exceed `2 * 10^5`.

## Output

For each test case, output a single integer — the maximum possible score.


## Examples

### Input

```text
6
1
1 1
2
1 2 1 2
2
1 2 2 1
3
1 1 2 3 3 2
3
1 2 3 3 2 1
4
1 2 3 4 1 2 3 4
```

### Output

```text
4
10
16
20
36
28
```

## Note

In the second test case, one optimal strategy is to choose `x = 1` first. This deletes the subarray `[1, 2, 1]` and adds `3^2 = 9` to the score. The remaining array is `[2]`; choosing `x = 2` adds `1`. The total score is `10`.

In the third test case, choosing `x = 1` deletes the whole array and adds `4^2 = 16` to the score.

In the fourth test case, choose `x = 1` first and then choose `x = 2`. The total score is `2^2 + 4^2 = 20`.

In the sixth test case, choose `x = 2` first. This deletes the subarray `[2, 3, 4, 1, 2]` from the middle of the array and adds `5^2 = 25` to the score. After deleting this subarray and concatenating the remaining elements, the array becomes `[1, 3, 4]`. Choosing each of the three remaining values then adds `1`, so the total score is `28`.
