# CF_103960K — Kalel, the Jumping Frog

- Codeforces: [103960K](https://codeforces.com/gym/103960/problem/K)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 112
- Titulo original: K. Kalel, the Jumping Frog
- time limit per test: 15 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Kalel is a frog that likes jumping over stones.

There are `N` stones in a row, numbered from `1` to `N` from left to right. Kalel begins at stone `1` and he wants to reach stone `N`.

At each move, Kalel can choose among `M` types of jump. The `j`-th jump allows him to jump from stone `x` to stone `x + d_j` and costs `p_j` energy points. It may happen that `p_j` equals `0` for some `j`. You can assume Kalel never runs out of energy.

Given `N` and `K`, calculate in how many ways Kalel can reach stone `N` spending at most `K` energy points in total. Two ways are considered different if the sequence of jump choices is different. As this number can become very large, we are only interested in its remainder modulo `10^9` (one billion).

## Input

The first line contains three integers, `N`, `M` and `K` (`1 <= N <= 10^9`, `1 <= M <= 10^5`, `0 <= K <= 400`). The next `M` lines contain two integers each, the numbers `d_j` and `p_j` (`1 <= d_j <= 10`, `0 <= p_j <= K`).

## Output

Print a single line, containing in how many different ways Kalel can get to the rock `N` spending a maximum of `K` energy points, modulus `10^9` (one billion).

## Examples

### Input 1

```text
5 3 10
1 3
2 0
3 1
```

### Output 1

```text
6
```

### Input 2

```text
100000 3 10
1 9
2 0
7 3
```

### Output 2

```text
85449877
```
