# CF_106636C — Saving Space

- Codeforces: [106636C](https://codeforces.com/gym/106636/problem/C)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 50
- Titulo original: C. Saving Space
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Screams compress really well this way.
— GePeTo

As GePeTo assimilates all data on the internet, they are looking for a way to compress that data so it occupies less space. For this purpose, they came up with the following compression algorithm.

Given a string `s` containing lowercase English letters, each maximal consecutive repetition of a letter `c` must be replaced by `c` followed by `n`, where `n` is the number of repetitions of that letter. If the letter is repeated just once, then it should not be replaced by `c1`, as that would increase the size of the string.

As an example, consider the string "zzzabbc". Since the letter 'z' is repeated three times consecutively and 'b' twice, the result of the compression is "z3ab2c".

Your task is to implement this algorithm.

## Input

The first line contains a single string `s` (`1 <= |s| <= 1000`) consisting of lowercase English letters, from 'a' to 'z'.

## Output

Print the result of the compression of `s`.

## Examples

### Input 1

```text
abccccaax
```

### Output 1

```text
abc4a2x
```

### Input 2

```text
zzzabbc
```

### Output 2

```text
z3ab2c
```

### Input 3

```text
aaaaaaaaaa
```

### Output 3

```text
a10
```
