# CF_103960B — Fun with Stones

- Codeforces: [103960B](https://codeforces.com/gym/103960/problem/B)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 345
- Titulo original: B. Fun with Stones
- time limit per test: 0.25 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Alice and Bob will play a game with `3` piles of stones. They take turns and, on each turn, a player must choose a pile that still has stones and remove a positive number of stones from it. Whoever removes the last stone from the last pile that still had stones wins. Alice makes the first move.

The `i`-th pile will have a random and uniformly distributed number of stones in the range `[L_i, R_i]`. What is the probability that Alice wins given that they both play optimally?

## Input

The input consists of a line with 6 integers, respectively, `L_1, R_1, L_2, R_2, L_3, R_3`. For each `i`, `1 <= L_i <= R_i <= 10^{9}`.

## Output

Print an integer representing the probability that Alice wins modulo `10^9+7`.

It can be shown that the answer can be expressed as an irreducible fraction `\frac{p}{q}`, where `p` and `q` are integers and `q \not\equiv 0 (\textrm{mod} 10^9+7)`, that is, we are interested in the integer `p * q^{-1} (\textrm{mod} 10^9+7)`.

## Examples

### Input 1

```text
3 3 4 4 5 5
```

### Output 1

```text
1
```

### Input 2

```text
4 4 8 8 12 12
```

### Output 2

```text
0
```

### Input 3

```text
1 10 1 10 1 10
```

### Output 3

```text
580000005
```

### Input 4

```text
5 15 2 9 35 42
```

### Output 4

```text
1
```
