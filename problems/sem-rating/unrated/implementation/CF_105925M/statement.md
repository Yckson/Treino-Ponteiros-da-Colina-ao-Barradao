# CF_105925M — Spooky Movement at a Distance

- Codeforces: [105925M](https://codeforces.com/gym/105925/problem/M)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 27
- Titulo original: M. Spooky Movement at a Distance
- time limit per test: 1 second
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Charles is a great physicist, cryptographer, and computer scientist, known for his significant contributions, including foundational work on the relationship between physics and information. During his studies on quantum teleportation, Charles discovered a quantum field with `N` positions numbered from 1 to `N`. In an experiment, Charles can place a particle initially in any position of the quantum field. At each moment in time, the particle can decide whether to teleport to a position greater than its current position or to remain still and finish its path. Thus, there are `2^N - 1` possible paths.

Let a path be a sequence of positions visited by a particle in an experiment. Each position `i` (`1 <= i <= N`) of the quantum field has an associated coefficient `A_i`. Charles defines the beauty of a path as the greatest common divisor of all the coefficients of the positions visited in the path.

Charles will perform several operations in sequence, which are:

 -  1 X: Consider that all possible paths have the same probability of being taken. What is the probability that the path taken has beauty equal to `X`?
-  2 I X: Update the value of the coefficient `A_I` to be `X`.
Can you help Charles with his experiments?

## Input

The first line of the input contains the integer `N` (`1 <= N <= 10^5`), the number of positions in the quantum field. The second line contains `N` positive integers `A_1, A_2, ..., A_N` (`1 <= A_i <= 10^5`). The third line of the input contains the integer `Q` (`1 <= Q <= 10^5`), the number of queries. The next `Q` lines will contain operations. Each line is an operation identified by the integer `T` (`1 <= T <= 2`). Operations with `T = 1` are followed by an integer `X`, and operations of type 2 are followed by the integers `I` (`1 <= I <= N`) and `X`. In both operations, `1 <= X <= 10^5`.

## Output

For each experiment conducted by Charles, print the probability `\frac{P}{Q}` that the experiment has beauty equal to `X` in the form `P * Q^{-1} \pmod{998244353}`. It is guaranteed that `Q^{-1}` exists under this modulus.

## Examples

### Input 1

```text
4
1 2 4 8
6
1 1
1 2
1 4
1 8
1 3
1 5
```

### Output 1

```text
931694730
465847365
732045859
865145106
0
0
```

### Input 2

```text
3
18 29 15
5
1 12
1 25
1 28
2 1 25
1 5
```

### Output 2

```text
0
0
0
855638017
```
