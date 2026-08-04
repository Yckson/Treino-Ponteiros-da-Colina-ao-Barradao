# CF_105925F — Feynman Memorizing Numbers

- Codeforces: [105925F](https://codeforces.com/gym/105925/problem/F)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 284
- Titulo original: F. Feynman Memorizing Numbers
- time limit per test: 2 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Richard Feynman was the first to propose the use of a quantum phenomenon to perform computational routines. This was during a lecture presented at the First Conference on Physics Computing at MIT. He showed that a classical computer would take a long time to simulate a simple quantum physics experiment. Legend has it that he could memorize large sequences of numbers and mentally calculate various properties at super-fast speeds.

The MythBusters, upon learning this, decided to verify this legend directly with Feynman using their time machine. To verify, they would generate a sequence of numbers and ask how many ways we can choose exactly 4 elements from this sequence that sum to `X`. The creation of the test was assigned to you, the new intern of the MythBusters.

Your task is to write a program that, given a set of numbers and multiple query values, determines how many quadruples `\{i,j,k,l\}` with `1 <= i \lt j \lt k \lt l <= N` have a sum `A_i + A_j + A_k + A_l` equal to the queried values.

## Input

The input consists of a single test case. The first line contains an integer `N` (`4 <= N <= 1000`), representing the number of numbers in the sequence. The second line contains `N` integers `a_i` (`0 <= |a_i| <= 1000`), separated by spaces. The third line contains an integer `Q` (`1 <= Q <= 4000`), representing the number of queries. Finally, each of the next `Q` lines contains an integer `q_i` (`0 <= |q_i| <= 4000`) each, representing the target values queried.

## Output

For each query, your program should print a line containing a single integer: the number of quadruples whose sum is equal to `q_i`.

## Examples

### Input

```text
8
-1 23 4 -8 4 23 4 5
1
30
```

### Output

```text
6
```
