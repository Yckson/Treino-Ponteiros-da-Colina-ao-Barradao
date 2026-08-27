# CF_105327G — Geography of Rivers

- Codeforces: [105327G](https://codeforces.com/gym/105327/problem/G)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 31
- Titulo original: G. Geography of Rivers
- time limit per test: 3 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

When studying the geography of the world's rivers, you may ask yourself: when two rivers join together, who chooses the name of the river that results from this junction? In fact, the answer is simple: when two rivers join together, the name of the river that had the largest volume of water becomes the name. Given that all rivers eventually join together and flow into the sea, an interesting problem is to calculate, given the name of each source, the name of the final river that flows into the sea.

Formally, `N` river sources are given. For each source, you have a quantity of liters of water `l_i` that originates from it. Furthermore, pairs of rivers meet (like a binary tree), until they all join and flow into the sea. When two rivers meet, the quantity of liters of water is added together, and the name of the river becomes the name of the river that had more water, or, in case of a tie, the one with the lowest index. The initial name of each source is its index.

What you want to know is the name of the river that eventually flows into the sea. However, it's rainy season! You need to process `Q` operations. In each of them, a rain occurred that caused `q_i` liters more of water to be produced in the source `n_i` (and this will be maintained for future operations). After each operation, calculate the name of the river that flows into the sea.

## Input

The first line contains an integer `N` `(1 <= N <= 10^5)`: the number of river sources.

The second line contains `N` integers `l_i` `(1 <= l_i <= 10^9)`: the number of liters of water that originate in source `i`.

The following `N-1` lines describe how the rivers join together. In the `i`-th of them, two integers `a_i, b_i` `(1 <= a_i, b_i \lt N + i)` indicate that the rivers `a_i` and `b_i` join together to form the river `N+i` (whose volume of water will be the sum of the volumes of `a_i` and `b_i`, and whose name will be the name of the one with the largest volume of water). It is guaranteed that the values `a_i` and `b_i` are valid, that is, `a_i != b_i` and neither of them has been previously joined in the input.

The next line contains an integer `Q` `(1 <= Q <= 10^5)`, the number of operations.

Then `Q` lines with the operations follow: the `i`-th line contains two integers `n_i` and `q_i` (`1 <= n_i <= N` and `1 <= q_i <= 10^9`), meaning that the source `n_i` now sources `q_i` liters more of water.

## Output

Print, on the first line, the name of the river that initially flows into the sea. Then print `Q` lines: after each operation, the name of the river that flows into the sea.

## Examples

### Input

```text
3
1 4 4
1 2
4 3
2
3 2
1 2
```

### Output

```text
2
3
2
```
