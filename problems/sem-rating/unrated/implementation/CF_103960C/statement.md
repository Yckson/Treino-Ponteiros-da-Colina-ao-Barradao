# CF_103960C — Cutting with Lasers

- Codeforces: [103960C](https://codeforces.com/gym/103960/problem/C)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 428
- Titulo original: C. Cutting with Lasers
- time limit per test: 0.35 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

A laser cutting machine for wood sheets has a laser head that can move in only two directions, horizontal and vertical. You have been hired to be part of the testing team for the machine.

One of the tests consists of programming the machine to perform a non-empty sequence of consecutive cuts that starts and ends at the same point. Each cut in the sequence, except the first, starts at the point at which the previous cut ended. No cuts touch the edge of the sheet to be cut. Figures (a) and (b) below show two examples of cutting sequences, with respectively 8 and 14 cuts.

  Your boss asked you to determine the area of the largest piece produced by the sequence of cuts, disregarding the piece attached to the edges of the cut sheet. That is, only the pieces contained in the polygon formed by the cut lines should be considered. Figures (c) and (d) below show respectively the largest pieces produced by the cuts of figures (a) and (b).

  To illustrate, figures (e) and (f) below show the discarded piece (which contains the edges of the wood sheet) of the cut sequences of figures (a) and (b), respectively.

## Input

The first line contains an integer `N`, the number of cuts in the sequence (`4 <= N <= 10^{4}`). The second line contains two integers `X_0` and `Y_0`, the initial position of the laser head in the sequence of cuts (`1 <= X_0 <= 10^3` and `1 <= Y_0 <= 10^3`). Each of the next `N` lines contains two integers `X_i` and `Y_i`, the final position of the cut `i` (`1 <= X_i <= 10^3` and `1 <= Y_i <= 10^3`, for `1 <= i <= N`, and `(X_N, Y_N) = (X_0, Y_0)`). All positions given in the input are distinct, except the first and the last positions.

## Output

Your program must output a single line, containing a single integer, the area of the largest piece produced by the sequence of cuts.

## Examples

### Input 1

```text
8
2 1
7 1
7 4
3 4
3 2
5 2
5 6
2 6
2 1
```

### Output 1

```text
17
```

### Input 2

```text
14
1 1
8 1
8 6
6 6
6 2
2 2
2 4
7 4
7 5
3 5
3 3
4 3
4 6
1 6
1 1
```

### Output 2

```text
21
```
