# CF_106636A — Scrabble

- Codeforces: [106636A](https://codeforces.com/gym/106636/problem/A)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 11
- Titulo original: A. Scrabble
- time limit per test: 1 second
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Enrique and Yan frequently play a game called 1D Scrabble. The game is played on a one-dimensional, infinite board using a fixed dictionary of unique words. On the first turn (`i = 1`), any word `w_1` from the dictionary may be played. On every subsequent turn (`i \gt 1`), the played word `w_i` must contain the previous word `w_{i-1}` as a contiguous substring. The game concludes as soon as no valid moves remain.

Recently, Yan did not have time to play, so Enrique started playing with GePeTo. However, GePeTo started hallucinating! It consistently states that this game is trivial, arguing that there are very few combinations. Help Enrique convince GePeTo by calculating the total number of distinct possible games. Two games are distinct if their sequences of played words `(w_1, ..., w_k)` are different.

## Input

The first line contains a single integer `N` (`1 <= N <= 10^5`), the number of words.

Each of the next `N` lines contains a word `w` consisting of lowercase English letters. It is guaranteed that all words are unique and the sum of lengths of all words does not exceed `10^5`.

## Output

Print a single integer: the number of distinct possible games modulo `10^9+7`.

## Examples

### Input 1

```text
3
mara
maratona
tona
```

### Output 1

```text
3
```

### Input 2

```text
3
a
aa
aaa
```

### Output 2

```text
4
```

### Input 3

```text
5
a
ab
abc
bc
c
```

### Output 3

```text
7
```
