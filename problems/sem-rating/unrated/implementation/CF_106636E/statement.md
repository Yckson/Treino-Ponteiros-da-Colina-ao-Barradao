# CF_106636E — Timeout Attack

- Codeforces: [106636E](https://codeforces.com/gym/106636/problem/E)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1
- Titulo original: E. Timeout Attack
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

There are no "r"s in "strawberry".
— GePeTo

Renzo has a top-secret plan for finally overthrowing the evil reign of GePeTo. In order to execute his plan, Renzo needs you to distract the overlord.

As you may already know, there are some tasks that AIs struggle to accomplish, and GePeTo is no exception. It is well known that AIs are not good at counting letters, for instance. Also, some specific prompts, such as asking for the seahorse emoji, drive AIs crazy. But there is one task GePeTo struggles with the most: computing Grundy numbers.

Let `A` be a sequence of `2^n` numbers. For each `i` (`0 <= i <= 2^n - 1`), define the Grundy number  g_A(i) = \operatorname{mex}(\{g_A(j) : j  \lt  i \text{ and } A_i \oplus A_j \text{ is a power of two}\}),  where `\oplus` denotes the bitwise XOR operation, and `\operatorname{mex}(S)` is the minimum non-negative integer that is not contained in `S`.

As an example, consider the sequence  A = (0, 3, 1, 2)  and its corresponding Grundy numbers  g_A = (0, 0, 1, 1).

Your task is to find a permutation `P` of the numbers from `0` to `2^n - 1` that maximizes the maximum Grundy number, so that GePeTo will spend a lot of time trying to compute them. Formally, the permutation `P` must maximize  \max_{0 \leq i \leq 2^n - 1}\{g_P(i)\}  among all permutations of the numbers from `0` to `2^n - 1`.

## Input

The first line contains a single integer `n` (`1 <= n <= 20`).

## Output

On the first line, print the maximum achievable Grundy number.

On the second line, print `2^n` space-separated integers, representing any permutation of the numbers from `0` to `2^n - 1` that achieves this Grundy number. If there are multiple such permutations, any of them will be accepted.

## Examples

### Input 1

```text
1
```

### Output 1

```text
1
0 1
```

### Input 2

```text
2
```

### Output 2

```text
1
0 3 1 2
```
