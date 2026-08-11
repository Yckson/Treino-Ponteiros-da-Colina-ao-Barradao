# CF_103960D — Displacing Particles

- Codeforces: [103960D](https://codeforces.com/gym/103960/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1196
- Titulo original: D. Displacing Particles
- time limit per test: 0.25 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

A square has its vertices at the coordinates `(0, 0), (0, 2^N), (2^N, 2^N), (2^N, 0)`. Each vertex has an attractor. A particle is placed initially at position `(2^{N-1}, 2^{N-1})`. Each attractor can be activated individually, any number of times. When an attractor at position `(i, j)` is activated, if a particle is at position `(p, q)`, it will be moved to the midpoint between `(i, j)` and `(p, q)`.

Given `N` and a point `(x, y)`, calculate the least number of times you have to activate the attractors so that the particle ends up at position `(x, y)`. You may assume that for all test cases a solution exists.

## Input

The input consists of a single line containing three integers `N`, `x` and `y`, such that `1 <= N <= 20` and `0 \lt x, y \lt 2^N`.

## Output

Print a single line, containing the least number of times you have to active the attractors.

## Examples

### Input 1

```text
1 1 1
```

### Output 1

```text
0
```

### Input 2

```text
4 12 4
```

### Output 2

```text
1
```

### Input 3

```text
4 3 1
```

### Output 3

```text
3
```
