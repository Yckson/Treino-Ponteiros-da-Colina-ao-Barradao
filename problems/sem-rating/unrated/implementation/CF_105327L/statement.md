# CF_105327L — Lecographically Maximum

- Codeforces: [105327L](https://codeforces.com/gym/105327/problem/L)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1483
- Titulo original: L. Lecographically Maximum
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

A list of `N` integers `a_1, ..., a_N` is stored in the memory of an electronic device. This device has a very peculiar operation available: bit swapping between numbers. More precisely, given integers `i`, `j` and `k`, this operation swaps the `k`-th bit of the integer `a_i` with the `k`-th bit of the integer `a_j` (and vice-versa).

Very interesting phenomena can occur when performing this operation one or more times, such as obtaining numbers that did not even belong to the original list, or even numbers larger or smaller than all the original elements.

For this problem, we are interested in using the operation as many times as necessary to change the list of numbers so that the resulting list is the lexicographically maximum, that is, that `a_1` is the largest possible, that `a_2` is the largest possible among the possible solutions that maximize `a_1`, and so on.

## Input

The first line of input contains an integer `N` (`1 <= N <= 10^5`) and the second line contains `N` integers, separated by spaces, corresponding to the list `a_1, ..., a_N` (`0 <= a_i <= 10^9`).

## Output

Your program should print a single line containing `N` space-separated integers corresponding to the lexicographically maximum obtainable sequence.

## Examples

### Input 1

```text
4
8 4 2 1
```

### Output 1

```text
15 0 0 0
```

### Input 2

```text
4
12 15 1 20
```

### Output 2

```text
31 13 4 0
```
