# CF_106073G — Generating patterns

- Codeforces: [106073G](https://codeforces.com/gym/106073/problem/G)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 99
- Titulo original: G. Generating patterns
- time limit per test: 1.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Sandy is developing a new computer as part of the ambitious System for Binary Compression (SBC) project. This project is part of a major technological challenge known as the Interface for Compact Pattern Coding (ICPC), whose goal is to achieve maximum efficiency in writing large volumes of data.

The SBC proposal is bold: choose a base pattern `B`, consisting of 8 bits `b_0,...,b_7`, and from it generate any other pattern by applying only simple, fast operations.

Sandy wants to write a sequence of `N` bits to memory, with `N >= 8`, denoted by `C = c_0,...,c_{N-1}`. Initially, memory contains only zeros. She may then repeat the following operation any number of times:

 -  Choose an integer `i` between `-7` and `N-1`, the position at which `B` will be applied;
-  For each position of `B` that overlaps the sequence, that is, for every `j` from `0` to `7` such that `0 <= i+j <= N-1`, replace `c_{i+j}` with `b_j \oplus c_{i+j}`, where `\oplus` denotes the XOR (exclusive OR) operation.
 The following example illustrates two applications of the procedure: applying pattern `B` to content `C`, the final result `C'` is obtained.  Since the data we want to write to memory is usually not random, Sandy believes that, with a good choice of base pattern `B`, it will be possible to produce the desired content with few operations.

To test this hypothesis, she needs your help: given the content `C` that must be written to memory, determine the base pattern `B` that minimizes the number of operations needed to generate `C` as described, and also the number `Q` of operations required.

It can be proven that it is always possible to write any content using this procedure. However, for the SBC project to be successful and earn the ICPC seal of excellence, your solution needs to be fast and efficient!

## Input

The first line contains an integer `N` (`8 <= N <= 4096`), the length of `C`.

The second line contains a sequence of `N` bits, representing `C`, the content that must be written to memory.

## Output

Your program should print a single line containing the 8-bit sequence `B`, representing the base pattern that minimizes the number of operations, and an integer `Q`, representing the minimum number of operations.

If there is more than one pattern `B` that minimizes the number of operations, print the one with the smallest integer value when interpreted in base 2, where `b_0` is the most significant bit and `b_7` is the least significant bit.

## Examples

### Input 1

```text
9
101001111
```

### Output 1

```text
00111101 2
```

### Input 2

```text
12
111111001010
```

### Output 2

```text
00010101 3
```

### Input 3

```text
10
0101001111
```

### Output 3

```text
01000011 2
```
