# CF_104555I — Investigating Zeroes and Ones

- Codeforces: [104555I](https://codeforces.com/gym/104555/problem/I)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1275
- Titulo original: I. Investigating Zeroes and Ones
- time limit per test: 0.3 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

You find yourself in a mysterious binary world, where an array of `N` binary digits awaits your scrutiny. Each digit is either a zero or a one, creating a unique pattern across the landscape. Your quest is to uncover the hidden patterns of this binary realm by unraveling the significance of subarrays with an odd number of ones.

The array of digits is denoted as `b_1, b_2, ..., b_N`. Your task is to embark on a journey to discover the enigmatic subarrays – segments of consecutive digits – and determine the count of subarrays that harbor an odd number of ones.

As you traverse this binary landscape, remember that a subarray is defined by its starting and ending digits. For instance, in the sequence `[b_1, b_2, b_3]`, subarrays include `[b_1]`, `[b_2]`, `[b_3]`, `[b_1, b_2]`, `[b_2, b_3]`, and `[b_1, b_2, b_3]`.

Your mission is to design an algorithm that determines the total number of subarrays containing an odd number of ones within this binary sequence. Please don't forget that the answer might not fit in a 32-bits integer.

## Input

The first line contains an integer `N` (`1 <= N <= 10^5`) representing the length of the binary sequence.

The second line contains `N` binary digits `b_1, b_2, ..., b_N` `(b_i \in \{0, 1\})` representing the elements of the sequence.

## Output

Output a single line with an integer representing the count of subarrays in the sequence that hold an odd number of ones.

## Examples

### Input 1

```text
3
0 1 0
```

### Output 1

```text
4
```

### Input 2

```text
10
1 0 0 1 1 0 1 1 1 0
```

### Output 2

```text
30
```
