# CF_105327F — Fractions are better when continued

- Codeforces: [105327F](https://codeforces.com/gym/105327/problem/F)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 2272
- Titulo original: F. Fractions are better when continued
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Little Charles was one of the best competitive programmers in the world. However, he never really liked programming. Now that he is retired, he can dedicate his studies to what he really loves: continued fractions.

To prepare for the upcoming Imensa Competição de Phrações Contínuas (ICPC), he needs to solve the following problem:

Define `p_0 = 1` as the level 0 fraction. Then define:

 p_1 = \frac{1}{1 + 1}

as the level 1 fraction, `p_1`. And also,

 p_2 = \frac{1}{1 + \frac{1}{1 + 1}}

as the level 2 fraction, `p_2`, and so on.

Given an integer value `N`, help Charles determine the value of the numerator of the fraction `p_N`.

## Input

The first and only line contains an integer `N` (`1 <= N <= 40`).

## Output

The value `p_N` can be written as a fraction of the form `\frac{a}{b}`, where `a` and `b` are coprime. Print a line containing the value of `a`.

## Examples

### Input 1

```text
2
```

### Output 1

```text
2
```

### Input 2

```text
10
```

### Output 2

```text
89
```
