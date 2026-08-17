# CF_104555L — Lexicographical Challenge

- Codeforces: [104555L](https://codeforces.com/gym/104555/problem/L)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1631
- Titulo original: L. Lexicographical Challenge
- time limit per test: 0.3 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

In the picturesque village of Lexicoville there lived two friends, Lily and Ethan. One day, a mysterious letter arrived at their house, sealed with a bunch of beatiful insignia full of sparkle and enchantment. Inside the envelope, they found a riddle too complex, even for the wisest minds of their village.

In this riddle, they were given an integer `K` and a string `S` containing only lower-case letters, which could be changed according to a curious rule. At each moment, the villagers have the freedom to choose an index `i`; then, magically, the characters `S_i` and `S_{i+K}` will be swapped! The riddle will be solved when the lexicographically minimum string, using only the allowed operation, is found.

The village was filled with curiosity and excitement with this riddle, but none more so than Lily and Ethan. The friends, always craving adventure, decided to dive headfirst into this challenge. However, as they observed the string, they noticed that the road to success was paved with countless possible swaps.

With the riddle's words echoing in their minds, they wondered: How could they navigate this web of possibilities to unveil the lexicographically minimum string? Every swap was like turning a page in a magical book, revealing new secrets and mysteries.

A long time has passed, but neither Lily nor Ethan have been able to solve the riddle. Can you help them?

## Input

The first line contains the string `S` (`1 <= |S| <= 10^5`). The seconds line contains the integer `K` (`1 <= K \lt |S|`).

## Output

Output a single line with the lexicographically earliest string that can be obtained.

## Examples

### Input 1

```text
zaaab
4
```

### Output 1

```text
baaaz
```

### Input 2

```text
njoab
2
```

### Output 2

```text
banjo
```
