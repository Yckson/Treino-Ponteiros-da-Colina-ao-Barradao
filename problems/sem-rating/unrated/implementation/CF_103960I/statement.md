# CF_103960I — Intercepting Information

- Codeforces: [103960I](https://codeforces.com/gym/103960/problem/I)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 2548
- Titulo original: I. Intercepting Information
- time limit per test: 0.25 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Spies Breaching Computers (SBC) is a private digital spy agency that is developing a new device for intercepting information using electromagnetic waves, which allows spying even without physical contact with the target.

The device tries to collect information one byte at a time, this is, a sequence of 8 bits where each of them, naturally, can have a value of 0 or 1. In certain situations, due to interference from other devices, the reading cannot be done successfully. In this case, the device returns the value 9 for the corresponding bit, informing that the reading could not be performed.

In order to automate the recognition of the information the device reads, a request was made for a program that, based on the information read by the device, informs whether all bits were read successfully or not. Your task is to write this program.

## Input

The input consists of a single line, containing 8 integers `N_1, N_2, N_3, N_4, N_5, N_6, N_7` and `N_8`, indicating the values read by the device (`N_i` is 0, 1 or 9 for `1 <= i <= 8`).

## Output

Print a single line containing the capital letter 'S' if all bits are read successfully; otherwise print a single line containing the capital letter 'F', corresponding to a failure.

## Examples

### Input 1

```text
0 0 1 1 0 1 0 1
```

### Output 1

```text
S
```

### Input 2

```text
0 0 1 9 0 1 0 1
```

### Output 2

```text
F
```
