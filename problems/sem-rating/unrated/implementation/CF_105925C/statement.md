# CF_105925C — Matrix Logic Circuits

- Codeforces: [105925C](https://codeforces.com/gym/105925/problem/C)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 62
- Titulo original: C. Matrix Logic Circuits
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

In quantum computing, logic gates operate a bit differently. Quantum logic gates are reversible, and the number of input qubits is equal to the number of output qubits. Additionally, they can be represented by `2^N` by `2^N` matrices, where `N` is the number of qubits.

A quantum circuit is a model for quantum computation where the computation is performed through a sequence of quantum logic gates and measurement devices. A sequence of logic gates can be represented by a matrix resulting from the multiplication of the matrices of the logic gates in the order of application, which is the reverse order of how they are graphically represented. For example, the circuit for adding two bits in its quantum form is:

  In this circuit, we have two variations of a logic gate that we will call `\text{CNOT}(q_c, q_t)` and `\text{CCNOT}(q_{c_1}, q_{c_2}, q_t)`. In the diagram, the qubit `q_t` is marked with a `\oplus`. The logic gate `\text{CNOT}(q_c, q_t)` can be seen as being equal to `\text{CCNOT}(q_c, q_c, q_t)`, that is, the application of the logic gate `\text{CCNOT}` with `q_c = q_{c_1} = q_{c_2}`.

The logic gate `\text{CCNOT}(q_{c_1}, q_{c_2}, q_t)` behaves by inverting the output qubit `q_t` if both control qubits `q_{c_1}` and `q_{c_2}` are set. Mathematically, `q'_t = q_t \oplus (q_{c_1} \land q_{c_2})`. In its matrix form:

  where `i` is the row and `j` is the column with `0 <= i, j \lt 2^N`, and `i` contains bit `k` (`0 <= k`) if `<=ft\lfloor \frac{x}{2^k} \right\rfloor \mod 2 = 1`. The operation `\oplus` is the bitwise exclusive or operation, commonly represented as `\land` in programming languages.

Thus, the matrix of the quantum circuit for adding two bits is given by

  where the qubits `q_0, q_1, q_2, q_3` are used with inputs `|A\rangle, |B\rangle, |C_{in}\rangle, |0\rangle` respectively and result in `|A\rangle, |B\rangle, |S\rangle, |C_{out}\rangle` respectively.

Your task is given the description of a circuit with logic gates `\text{CNOT}` and `\text{CCNOT}` in the order of application, to print the resulting matrix.

## Input

The first line of the input contains the integers `N` (`2 <= N <= 8`), the number of qubits in the circuit, and `M` (`1 <= M <= 10^5`), the number of logic gates in the circuit.

This is followed by `M` lines, each with the description of a logic gate. The first integer `T` (`1 <= T <= 2`) defines the type of the logic gate. If `T = 1`, the description is for the logic gate `\text{CNOT}(q_C, q_T)` and is followed by distinct integers `C` and `T` (`0 <= C, T \lt N`). If `T = 2`, the description is for the logic gate `\text{CCNOT}(q_{C1}, q_{C2}, q_T)` and is followed by distinct integers `C1`, `C2`, and `T` (`0 <= C1, C2, T \lt N`). Note that the logic gates are given in the order of application.

## Output

Print `2^N` lines, each containing exactly `2^N` characters '0' or '1', corresponding to the complete matrix of the quantum circuit.

## Examples

### Input 1

```text
2 1
1 0 1
```

### Output 1

```text
1000
0001
0010
0100
```

### Input 2

```text
4 5
1 0 1
1 1 2
2 1 2 3
1 0 1
2 0 1 3
```

### Output 2

```text
1000000000000000
0000000000000100
0000000000000010
0000000000010000
0000100000000000
0100000000000000
0010000000000000
0000000000000001
0000000010000000
0000010000000000
0000001000000000
0001000000000000
0000000000001000
0000000001000000
0000000000100000
0000000100000000
```

### Input 3

```text
3 1
2 0 1 2
```

### Output 3

```text
10000000
01000000
00100000
00000001
00001000
00000100
00000010
00010000
```

### Input 4

```text
3 1
1 0 1
```

### Output 4

```text
10000000
00010000
00100000
01000000
00001000
00000001
00000010
00000100
```
