# CF_106073B — Baralho Alho

- Codeforces: [106073B](https://codeforces.com/gym/106073/problem/B)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 81
- Titulo original: B. Baralho Alho
- time limit per test: 1 second
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Researcher Isadora loves playing cards with her friends. More specifically, she plays a version called Baralho Alho, in which there are `N` cards (duplicates are allowed). Initially, the `N` cards are in a specific order: the `i`-th card has value `A_i`. Two cards are considered equal if they have the same value.

Before the game starts, Isadora declares: "I always shuffle Baralho Alho." Naively, her friends agree and let her command the shuffling. Little do they know that Researcher Isadora loves to cheat. Her goal is to shuffle in such a way that, at the end of the process, the `i`-th card has value `B_i`.

However, she only knows one type of shuffling: it maps the card originally at position `i` to position `P_i`. For example, if `P = [3, 2, 4, 1]`, then the first card goes to the third position, the second remains in place, the third goes to the fourth, and the fourth goes to the first. Thus, if the initial deck is `[4, 2, 6, 1]`, after applying the shuffling, Isadora gets `[1, 2, 4, 6]`.

  Even with this limitation, Isadora is quite intelligent and plans to repeat the shuffling several times in order to reach new deck configurations.

Write a program that, given `A_i`, `B_i`, and `P_i`, determines the minimum number of times Isadora needs to apply the shuffling so that the deck is in the desired order. If this is impossible, print "IMPOSSIVEL" (without quotes). If the minimum number of shuffles is greater than `10^9`, print "DEMAIS" (without quotes).

## Input

The first line of input contains an integer `N` (`1 <= N <= 10^6`).

The second line contains `N` integers `A_i` (`1 <= A_i <= 10^9`), representing the initial configuration of the deck.

The third line contains `N` integers `B_i` (`1 <= B_i <= 10^9`), representing the desired final configuration of the deck.

The fourth line contains `N` distinct integers `P_i` (`1 <= P_i <= N`), indicating that the card in position `i` goes to position `P_i` after one application of the shuffling.

## Output

Print a single integer `k`: the minimum number of times the shuffling must be applied, starting from `A_i`, until the resulting configuration is `B_i`.

If this is impossible, print "IMPOSSIVEL" (without quotes).

If the minimum `k` is greater than `10^9`, print "DEMAIS" (without quotes).


## Examples

### Input 1

```text
6
8 6 5 5 1 3
5 1 8 5 3 6
2 3 6 5 1 4
```

### Output 1

```text
2
```

### Input 2

```text
2
3 3
3 3
1 2
```

### Output 2

```text
0
```

### Input 3

```text
5
6 3 8 4 2
3 6 4 2 8
2 1 4 5 3
```

### Output 3

```text
5
```

### Input 4

```text
4
1 2 1 2
1 2 2 1
2 1 4 3
```

### Output 4

```text
IMPOSSIVEL
```

### Input 5

```text
3
1 2 3
2 1 4
1 2 3
```

### Output 5

```text
IMPOSSIVEL
```

## Note

Explanation of sample 1:

We can see the deck's configuration after each number of shuffles `k`:

 -  `k = 0`: the deck is in the order `8, 6, 5, 5, 1, 3`;
-  `k = 1`: the deck is in the order `1, 8, 6, 3, 5, 5`;
-  `k = 2`: the deck is in the order `5, 1, 8, 5, 3, 6`.
Therefore, the answer is `k = 2`.

Explanation of sample 2:

In this case, the deck is already in the desired configuration, so no shuffle is needed.
