# CF_105925J — Journey of the Particles

- Codeforces: [105925J](https://codeforces.com/gym/105925/problem/J)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 253
- Titulo original: J. Journey of the Particles
- time limit per test: 1 second
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

An experiment at the Large Hadron Collider is being set up to test phase properties of various different particles. There are `N` filters arranged in a circle, where the `i`-th filter allows particles with a phase less than or equal to its limit `A_i` to pass.

An experiment begins with the release of a particle at the position of the `i`-th filter, with an initial phase set to `A_i`. When passing through filter `i`, including the first one, the particle:

 -  Is filtered out if the phase of the particle is greater than the limit `A_i`, ending the experiment.
-  Otherwise, the particle passes through the filter, increases its phase by `K`, and moves to the next filter on the right, the `(i \bmod N) + 1`-th filter.
We want to simulate the result of this experiment to compare with the results verified empirically. To achieve this, we need to create a vector `B_i` of size `N`, where `B_i` (`1 <= B_i <= N`) is the position of the filter that stopped the particle that started at position `i`.

## Input

The first line contains two integers `N` (`1 <= N <= 2 * 10^5`) and `K` (`1 <= K <= 10^9`). The second line contains `N` integers `A_1, A_2, ..., A_N` (`-10^9 <= A_i <= 10^9`).

## Output

Print a line containing `N` integers `B_1, B_2, ..., B_N`.

## Examples

### Input 1

```text
4 1
4 3 1 2
```

### Output 1

```text
2 3 2 2
```

### Input 2

```text
5 5
-10 -5 0 5 10
```

### Output 2

```text
1 1 1 1 1
```

### Input 3

```text
6 2
12 4 5 9 2 3
```

### Output 3

```text
2 3 5 5 6 2
```
