# CF_105925L — qPhones Production Line

- Codeforces: [105925L](https://codeforces.com/gym/105925/problem/L)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 372
- Titulo original: L. qPhones Production Line
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

The Brazilian Society of Smartphones (SBC) is developing a new model of smartphones that utilizes quantum computing, the qPhones. Unlike traditional devices that store bits, this new architecture will use qubits.

A qubit (quantum bit) is the basic unit of quantum information, just as a bit is in classical computing. However, while a classical bit can only assume one state at a time (0 or 1), a qubit can exist in superposition, assuming multiple states simultaneously as a "quantum mixture" of 0 and 1, each with a probability of being measured when observed.

Thus, if a device can store qubits, all of its combinations can be represented simultaneously due to superposition. For example, if a device stores 3 qubits, we can have the representation of `2^3 = 8` superposed classical states, which are 000, 001, 010, 011, 100, 101, 110, and 111.

In practice, we can assume that to simulate 1 qubit we need 2 bits, to simulate 2 qubits we need 4 bits, to simulate 3 qubits we need 8 bits, and so on. Therefore, to fully simulate the memory of a classical cell phone with `M` megabytes (MB), the engineers at SBC need to ensure that the qubits of the new device can represent at least `M` megabytes. Consider that 1 MB is equivalent to `10^6` bytes.

You have recently been hired by SBC to assist in the production line of the new quantum smartphones. Your task is, given the memory value of `M` megabytes, to determine the minimum number of qubits necessary to simulate all possible states of a classical device with that amount of memory.

## Input

An integer `M` (`1 <= M <= 10^{10}`) representing the amount of memory in MB of a traditional device.

## Output

Output a single line with an integer representing the minimum number of qubits necessary to simulate all possible states of a classical device with `M` megabytes of memory.

## Examples

### Input 1

```text
1
```

### Output 1

```text
23
```

### Input 2

```text
17
```

### Output 2

```text
28
```
