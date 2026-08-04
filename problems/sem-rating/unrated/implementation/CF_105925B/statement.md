# CF_105925B — Periodic Search

- Codeforces: [105925B](https://codeforces.com/gym/105925/problem/B)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 127
- Titulo original: B. Periodic Search
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

An analysis was conducted on the evolution of the possible quantum states of a system of particles, resulting in a rooted tree of `N` states. Each state, except for the root state, is connected to its parent state by an edge that has a label of a lowercase Latin letter from a to z. This label describes the type of interference that caused the system to collapse into another state. The sequence of interferences of a state is defined as the concatenation of the labels of the edges on the path from the root to that state.

For each state, we define the minimum periodicity of its sequence as the smallest integer `P >= 1` such that the sequence can be obtained by repeating a smaller sequence of length `P` multiple times (at least twice). If there is no valid integer `P >= 1`, the sequence is considered to have a periodicity of `0`. The empty sequence from the root is considered to have a periodicity of `0`.

We are interested in studying periodic interferences within the system of particles, so your task is to determine, among all the states from the root, the highest value of minimum periodicity of their respective interference sequences.

## Input

The first line contains an integer `N` (`2 <= N <= 10^5`), the number of states. The second line contains `N-1` integers `P_1, P_2, ..., P_{N-1}` (`1 <= P_i <= i`), where state `i+1` is connected to state `P_i`. The third line contains a sequence of `N-1` lowercase Latin letters, where the character at position `i` represents the label on the edge between states `P_i` and `i+1`.

## Output

Print a single integer representing the highest minimum period among all sequences formed by the paths from the root to each state.

## Examples

### Input

```text
12
1 2 2 3 5 5 6 8 4 10 6
baaabaaabaa
```

### Output

```text
3
```
