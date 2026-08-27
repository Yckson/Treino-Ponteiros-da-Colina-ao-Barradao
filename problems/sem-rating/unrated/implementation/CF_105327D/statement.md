# CF_105327D — Decrease the Boss Strength

- Codeforces: [105327D](https://codeforces.com/gym/105327/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 87
- Titulo original: D. Decrease the Boss Strength
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Fulano, an avid gamer, has come across an epic challenge in the online game "Boss Challenge". The goal is to defeat a powerful boss, whose power is described by a set of ancient runes. These runes represent a giant binary number `N`, indicating the total strength of the enemy.

To defeat the boss, Fulano has `M` different spells at his disposal, and the goal is to reduce the total strength of the enemy to zero using these spells. The `i`-th spell is described with two integers `a_i` and `b_i`. When used, the `i`-th spell reduces the value of `N` by `a_i` units. This spell can be used as many times as the player wants, as long as two specific conditions are met:

 -  The value of `a_i` must be less than or equal to the current value of `N`.
-  The current value of `N` must be divisible by `2^{b_i}`. In other words, the spell `i` can only be used if the last `b_i` digits of `N` are zeros.
Fulano is fascinated by the game and wants to find out how many different ways he can combine the spells to reduce the binary number `N` to exactly zero and thus defeat the boss. Two combinations are considered different if the sequence in which the spells are used is different.

Since the number of possible combinations can be very large, the answer should be given modulo `10^9 + 7`.

Help Fulano find the answer!

## Input

The first line contains two integers, `N` `(1 <= N <= 10^{18})`, representing the boss's power, and `M` `(1 <= M <= 10^5)`, denoting the number of spells available.

The next `M` lines contain the spell descriptions: the `i`-th of these lines contains two numbers `a_i` `(1 <= a_i <= 100)` and `b_i` `(0 <= b_i <= 60)`.

## Output

Print a single integer: the number of different sequences of spell uses (taken modulo `10^9 + 7`) that reduce the boss's power from `N` to 0.

## Examples

### Input 1

```text
6 2
1 0
2 1
```

### Output 1

```text
8
```

### Input 2

```text
9 5
1 0
1 1
4 3
1 1
8 0
```

### Output 2

```text
92
```
