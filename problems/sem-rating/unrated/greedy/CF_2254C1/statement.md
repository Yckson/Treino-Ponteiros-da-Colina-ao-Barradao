# CF_2254C1 — Marenol (easy version)

- Codeforces: [2254C1](https://codeforces.com/problemset/problem/2254/C1)
- Score/rating: unrated
- Categoria local: `greedy`
- Tags Codeforces: greedy
- Resolvidos no Codeforces: 12878
- Titulo original: C1. Marenol (easy version)
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

This is the easy version of the problem. In this version, you are only asked to determine whether string `a` can be transformed into string `b`.

Yousef has given you two binary strings, `a` and `b`, of the same length `n`.

You are allowed to perform any of the following operations:

 -  Choose a substring`^{\text{∗}}` in `a` equal to `\texttt{001}` and replace it with `\texttt{100}`, or vice versa (i.e., `\texttt{001} \rightarrow \texttt{100}` or `\texttt{100} \rightarrow \texttt {001}`).
-  Choose a substring in `a` equal to `\texttt{110}` and replace it with `\texttt{011}`, or vice versa (i.e., `\texttt{011} \rightarrow \texttt{110}` or `\texttt{110} \rightarrow \texttt {011}`).
Your task is to determine whether it is possible to transform string `a` into string `b` using a finite number of operations.

`^{\text{∗}}`A string `a` is a substring of a string `b` if `a` can be obtained from `b` by deletion of several (possibly zero or all) characters from the beginning and several (possibly zero or all) characters from the end.

## Input

The first line contains a single integer `t` (`1 <= t <= 10^4`) — the number of test cases.

The first line of each test case contains a single integer `n` (`1 <= n <= 2 * 10^5`) — the length of each string.

The second line of each test case contains a binary string `a` (`|a| = n`), consisting of only characters `\texttt{0}` and/or `\texttt{1}`.

The third line of each test case contains a binary string `b` (`|b| = n`), consisting of only characters `\texttt{0}` and/or `\texttt{1}`.

It is guaranteed that the sum of `n` over all test cases does not exceed `2 * 10^5`.

## Output

For each test case, output "YES" if the string `a` can be transformed into string `b` using a finite number of operations, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.


## Examples

### Input

```text
9
1
0
0
2
01
10
3
001
100
4
1010
0101
4
1100
1000
5
01001
10010
6
110000
000011
6
111000
000111
7
1001100
0000111
```

### Output

```text
YES
NO
YES
NO
NO
YES
YES
NO
YES
```

## Note

In the first test case, it already holds that `a = b`. Therefore, the answer is YES.

In the second test case, we cannot perform any operation. Since `a != b`, the answer is NO.

In the third test case, we can choose the substring `a[1, 3] = \texttt{001}` and replace it with `\texttt{100}`, making `a = b`. Therefore, the answer is YES.

In the seventh test case, we can do the following in order:

 -  `\texttt{1}``{\color{blue}{\texttt{100}}}``\texttt{00}` `\rightarrow` `\texttt{1}``{\color{blue}{\texttt{001}}}``\texttt{00}`
-  `\texttt{100}``{\color{blue}{\texttt{100}}}` `\rightarrow` `\texttt{100}``{\color{blue}{\texttt{001}}}`
-  `{\color{blue}{\texttt{100}}}``\texttt{001}` `\rightarrow` `{\color{blue}{\texttt{001}}}``\texttt{001}`
-  `\texttt{00}``{\color{blue}{\texttt{100}}}``\texttt{1}` `\rightarrow` `\texttt{00}``{\color{blue}{\texttt{001}}}``\texttt{1}`
Therefore, the answer is YES.
