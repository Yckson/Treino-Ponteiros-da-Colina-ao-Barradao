# CF_104555B — Best Fair Shuffles

- Codeforces: [104555B](https://codeforces.com/gym/104555/problem/B)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 425
- Titulo original: B. Best Fair Shuffles
- time limit per test: 0.6 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

A Fair shuffle is a specific method of shuffling `N` distinct cards arranged horizontally from left to right. In a Fair shuffle, the cards are divided into two contiguous partitions which may have different card counts, and one of them may even have zero cards. Let's denote the left partition as `L` and the right partition as `R`.

Cards from the left partition (`L`) are then merged with the cards from the right partition (`R`) while maintaining the relative order between the cards of each partition.

Given the final permutation obtained after applying `K` Fair shuffles to an initial sequence of `N` non-repeating cards numbered from `1` to `N`, your task is to determine the minimum possible value of `K`.

For example, if we start with the sequence 1 2 3 4 5 and perform a Fair shuffle by partitioning it into `L`: 1 2 and `R`: 3 4 5, cards from `L` and `R` can be merged in various ways:

 -  1 3 2 4 5
-  1 3 4 2 5
-  3 4 5 1 2
-  1 2 3 4 5
-  etc
 Each arrangement represents a possible outcome of applying a single Fair shuffle. However, 1 3 2 5 4 is not a possible outcome as the relative order of cards 4 and 5 from `R` is not preserved.Assume that the outcome of the first Fair shuffle is 1 3 2 4 5. If we perform a second Fair shuffle on it, we could partition the sequence into `L`: 1 3 2 4 and `R`: 5 and merge it as 1 3 2 5 4.

## Input

The first line contains an integer `N (1 <= N <= 10^6)`, the number of cards in the deck. The second line contains a permutation of integer numbers from `1` to `N` describing the final arrangement of the cards.

## Output

Output a single line with an integer `K` indicating the minimum number of Fair shuffles required to transform the initial sequence into the given one.

## Examples

### Input 1

```text
5
3 4 5 1 2
```

### Output 1

```text
1
```

### Input 2

```text
10
1 6 5 2 10 3 4 8 7 9
```

### Output 2

```text
3
```

### Input 3

```text
5
5 4 2 3 1
```

### Output 3

```text
2
```

### Input 4

```text
8
1 6 2 3 7 8 4 5
```

### Output 4

```text
1
```

### Input 5

```text
5
1 2 3 4 5
```

### Output 5

```text
0
```
