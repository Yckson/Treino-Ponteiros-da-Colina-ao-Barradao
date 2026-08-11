# CF_103960A — Finding Maximal Non-Trivial Monotones

- Codeforces: [103960A](https://codeforces.com/gym/103960/problem/A)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 2430
- Titulo original: A. Finding Maximal Non-Trivial Monotones
- time limit per test: 0.25 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

In this problem we will be dealing with character sequences, often called strings. A sequence is non-trivial if it contains at least two elements.

Given a sequence `s`, we say that a chunk `s_i, ..., s_j` is monotone if all its characters are equal, and we say that it is maximal if this chunk cannot be extended to left or right without losing the monotonicity.

Given a sequence composed only of characters "a" and "b", determine how many characters "a" occur in non-trivial maximal monotone chunks.

## Input

The input consists of two lines. The first line contains a single integer `N`, where `1 <= N <= 10^5`. The second line contains a string with exactly `N` characters, composed only of the characters "a" and "b".

## Output

Print a single line containing an integer representing the total number of times the character "a" occurs in non-trivial maximal monotone chunks.

## Examples

### Input 1

```text
7
abababa
```

### Output 1

```text
0
```

### Input 2

```text
7
bababab
```

### Output 2

```text
0
```

### Input 3

```text
10
aababaaabb
```

### Output 3

```text
5
```

### Input 4

```text
10
bbaababaaa
```

### Output 4

```text
5
```
