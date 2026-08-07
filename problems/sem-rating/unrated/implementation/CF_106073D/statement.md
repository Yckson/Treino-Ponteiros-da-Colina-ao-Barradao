# CF_106073D — Dominoes

- Codeforces: [106073D](https://codeforces.com/gym/106073/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 279
- Titulo original: D. Dominoes
- time limit per test: 1.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Alice, tired of going out with her friends, invented her own variation of the classic game of dominoes. Her version uses the same set of domino pieces as the traditional game, where each piece is a tile with two ends, each marked with a number from 1 to 6.

To start the game, Alice shuffles the domino pieces into a pile and then takes one piece at a time from the top. When Alice takes the first piece from the pile, she simply places it on the table. From the second piece onward, she needs to place it on either the left or right end of the chain formed by the pieces already on the table.

To place a piece at one end of the chain, one of its numbers must match the number on that end. The other number on the newly played piece becomes the new free end of the chain. If Alice cannot place a piece, she loses the game; otherwise, if she manages to place all pieces successfully, she wins.

  Alice is not interested in games she cannot win, so she would like to know if it is possible to win with a given set of dominoes. Additionally, she may not have a complete set, as she may have lost some pieces.

Since Alice can choose to play with a subset of her pieces (effectively discarding the rest to make the game winnable), you must calculate the total number of subsets of her dominoes for which there is a nonzero chance of winning.

## Input

The input contains multiple test cases. The first line contains an integer `T` `(1 <= T <= 10^4)`, the number of test cases. Each test case is described as follows:

The first line of each case contains an integer `N` `(1 <= N <= 21)`, the number of pieces Alice has.

The following `N` lines contain two integers `a_i` and `b_i` (`1 <= a_i <= b_i <= 6`), indicating that Alice's `i`-th domino tile shows the numbers `a_i` and `b_i`.

It is guaranteed that Alice does not have duplicate pieces; in other words, `(a_i,b_i) != (a_j,b_j)` if `i != j`.

## Output

For each test case, print a single line containing an integer: the number of subsets of pieces for which Alice has a nonzero chance of winning.


## Examples

### Input

```text
3
3
1 2
2 3
3 4
4
1 1
1 2
2 3
3 4
3
1 2
2 2
2 3
```

### Output

```text
6
10
7
```

## Note

Explanation of sample 1:

For the third case of input, we have pieces 1-2, 2-2, and 2-3. Considering the subset where all pieces are present, a possible order for the pieces drawn from the pile after shuffling is the one shown in the image: 2-2, followed by 1-2, and finally 2-3. In this order, Alice can place piece 1-2 to the left of 2-2 and then 2-3 to the right, as illustrated in the image. Therefore, for this subset, Alice's chance of winning is greater than zero.
