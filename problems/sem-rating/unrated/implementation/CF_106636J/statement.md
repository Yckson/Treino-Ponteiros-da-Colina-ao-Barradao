# CF_106636J — Can you even?

- Codeforces: [106636J](https://codeforces.com/gym/106636/problem/J)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 44
- Titulo original: J. Can you even?
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

42... so pretty.
— GePeTo

In order to obtain more food tokens, you plan to present the GePeTo overlord with an array of numbers `A`. As they were trained on more even numbers than odd numbers, GePeTo prefers even numbers, so you want to change some numbers in `A` to maximize the number of even numbers.

Since you are already the first in line, you only have time to apply a single operation to `A`: pick a number `X` and a range `[L,R]` and add `X` to elements `A_L, ..., A_R`. After performing this operation exactly once, what is the maximum possible number of even numbers in `A`?

## Input

The first line contains an integer `N`. (`1 <= N <= 2 * 10^3`)

The second line contains `N` integers `A_1, A_2, ..., A_N`, where `1 <= A_i <= 1000`.

You may choose any integer `X` (`1 <= X <= 1000`) and any range `1 <= L <= R <= N`. You must perform the operation exactly once.

## Output

Print a single integer `E`, the maximum possible number of even numbers in the array after the operation.

## Examples

### Input 1

```text
3
1 2 3
```

### Output 1

```text
2
```

### Input 2

```text
14
1 2 2 1 1 1 2 1 1 2 2 2 1 1
```

### Output 2

```text
10
```

### Input 3

```text
1
1000
```

### Output 3

```text
1
```
