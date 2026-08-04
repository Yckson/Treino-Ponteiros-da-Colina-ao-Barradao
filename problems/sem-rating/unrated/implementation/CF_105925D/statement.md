# CF_105925D — Quantum Decoherence

- Codeforces: [105925D](https://codeforces.com/gym/105925/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 428
- Titulo original: D. Quantum Decoherence
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

The SBC (Brazilian Computer Society) is developing various models of architectures for quantum computers, with the goal of making them accessible to everyone in the future. One of the main challenges faced by the development teams is quantum decoherence, which occurs when a qubit in superposition (simultaneously representing states `0` and `1`) collapses to `0` or `1` due to environmental interference.

For each model developed, the rate of quantum decoherence will be analyzed. To do this, the qubits will be observed in an isolated state and under normal temperature and pressure conditions. The rate of quantum decoherence is the ratio between the number of qubits that collapsed under normal temperature and pressure conditions and the number of qubits that were in superposition in the isolated state.

Since there are several models, you have been asked to develop a program that calculates this rate. After all, you need extracurricular hours to graduate, right?!

## Input

The first line contains an integer `N` (`10 <= N <= 10^5`) indicating the number of qubits in the computer. The next two lines contain the strings `S` (isolated state) and `T` (normal conditions), respectively, each of size `N`, composed of the characters `\{0, 1, *\}`, where `*` indicates a qubit in superposition.

It is guaranteed that:

 -  At least one qubit is in superposition in `S`
-  Every qubit not in superposition in `S` remains identical in `T`

## Output

The output should contain the rate of quantum decoherence in decimal form, with exactly two decimal places.

## Examples

### Input 1

```text
10
0*1**100*1
0110*100*1
```

### Output 1

```text
0.50
```

### Input 2

```text
13
*1*01*100*01*
01*0101001011
```

### Output 2

```text
0.80
```

### Input 3

```text
25
*10*1*110*01*011100*110*0
*1011*110001*011100*110*0
```

### Output 3

```text
0.29
```
