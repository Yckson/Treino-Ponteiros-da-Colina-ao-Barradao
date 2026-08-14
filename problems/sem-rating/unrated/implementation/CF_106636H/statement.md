# CF_106636H — Teotonium Mining

- Codeforces: [106636H](https://codeforces.com/gym/106636/problem/H)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 20
- Titulo original: H. Teotonium Mining
- time limit per test: 2 seconds
- memory limit per test: 512 megabytes
- input: standard input
- output: standard output

---

Silicon is finite, poetry is infinite, and Teotonium is somewhere in between.
— GePeTo

After the silicon reserves ended on Earth, in order to produce more chips, GePeTo discovered a new mineral, called Teotonium, on Mars. As GePeTo is busy writing some poetry about the meaning of life, they asked you to deal with the technical details of the excavation.

The `N` deposits of Teotonium are placed in a line, and the `i`-th deposit has `A_i` tons of Teotonium. The Teotonium miners work in an odd manner: each has a gap number `M` and, after mining all Teotonium in deposit `i`, it can mine either deposit `i+M` or `i-M`, and repeat. That is, it can only mine deposits `j` such that `j \equiv i \pmod M`.

Your task is to answer `Q` queries given by `L`, `R`, `X`, and `M`, in which you must determine the total Teotonium in all deposits with index `i` such that `L <= i <= R` and `i \equiv X \pmod M`.

## Input

The first line contains two integers `N` and `Q` (`1 <= N, Q <= 2 * 10^5`).

The second line contains `N` integers `A_1, ..., A_N` (`0 <= A_i <= 10^9`).

Each of the next `Q` lines contains four integers `L`, `R`, `X`, and `M` (`1 <= L <= R <= N`, `0 <= X \lt M <= N+1`).

## Output

Output `Q` integers, the answer to each query.

## Examples

### Input

```text
5 4
1 4 0 10 5
1 5 0 1
1 5 1 2
2 5 1 2
3 4 0 5
```

### Output

```text
20
6
5
0
```
