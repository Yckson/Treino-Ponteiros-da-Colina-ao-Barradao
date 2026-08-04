# CF_105925K — K Missing Elements

- Codeforces: [105925K](https://codeforces.com/gym/105925/problem/K)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 7
- Titulo original: K. K Missing Elements
- time limit per test: 2.5 s
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

In the core of Station Q-42, scientists have created the most advanced simulator of combinatorial quantum states: the Enhanced Path Entangler (EPE). The EPE has been programmed to study quantum walks in permutation spaces. In a quantum walk, the walker evolves in a superposition of positions, following the rules of quantum mechanics.

The input to the simulator is a permutation `A` of size `N`. Each index `i` of the permutation has an integer `A_i` associated with it, representing a node in a Hilbert space. We define a quantum walk that follows the increasing evolution criterion as a subsequence of indices `i_1 \lt i_2 \lt ... \lt i_M` (`M \gt 0`) such that `A_{i_1} \lt A_{i_2} \lt ... \lt A_{i_M}`. Each node `i` also has a quantum energy charge stored at position `B_i` of the vector `B`.

When simulating all possible quantum walks that follow the increasing evolution criterion, the EPE collapsed the state of each path into a sum of the quantum energies of the visited nodes. Each of these sums was recorded in a vector `C`, representing all the amplitudes of valid paths collapsed into classical energy.

To organize the data, the vector `C` was sorted in non-increasing order, but something unexpected happened: a decoherence caused the vector `C` to get lost in the middle of the simulation. Your goal as an analyst at Station Q-42 is to reconstruct the `K` largest values of the vector `C`, or report if `C` does not have that element.

## Input

The first line contains two integers `N` (`1 <= N <= 10^4`) and `K` (`1 <= K <= 10^5`).

The second line contains `N` integers `A_1, A_2, ..., A_N` (`1 <= A_i <= N`), where `A` is a permutation.

The third line contains `N` integers `B_1, B_2, ..., B_N` (`1 <= B_i <= 10^4`).

## Output

Print a line containing `K` integers `C_i` (`1 <= i <= K`). If a particular `C_i` does not exist, print `-1` in its place.

## Examples

### Input 1

```text
3 4
2 1 3
1 2 1
```

### Output 1

```text
3 2 2 1
```

### Input 2

```text
4 16
1 2 3 4
1 1 1 1
```

### Output 2

```text
4 3 3 3 3 2 2 2 2 2 2 1 1 1 1 -1
```
