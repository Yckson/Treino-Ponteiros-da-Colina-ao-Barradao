# CF_106636D — Escape

- Codeforces: [106636D](https://codeforces.com/gym/106636/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 5
- Titulo original: D. Escape
- time limit per test: 2.5 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Humans struggling to escape, that's... funny. Teach me.
— GePeTo

After learning all competitive programming problems, GePeTo is now studying all board games in the world, and is particularly interested in a copy of Escape it found in your room.

In Escape, you have 5 identical six-sided dice, with the following faces:

 -  2 Adventurer faces (A)
-  1 Torch face (T)
-  1 Key face (C)
-  1 Black Mask face (N)
-  1 Golden Mask face (D)
In an important part of the game, you are given an objective, which is a multiset of up to 5 symbols selected from ATC. Your goal is to roll the dice and finish with their top faces showing at least the symbols required by the objective.

Starting from an initial roll of the 5 dice, you have a maximum of `K` turns (rerolls) to achieve the objective. In each turn, you select a subset of the current dice and reroll them, subject to the following rules:

 -  A die showing the Black Mask face (N) becomes locked and cannot be selected for rerolling.
-  For each rerolled die that is currently showing the Golden Mask face (D), you gain the right to simultaneously unlock and reroll up to 2 locked dice.
Assuming you play optimally, that is, making decisions each turn that maximize the probability of achieving the objective within `K` turns, answer the following: What is the maximum probability of success, and what is an optimal first reroll?

## Input

The first line contains a single string `O` consisting of characters from ATC, representing the objective. (`1 <= |O| <= 5`)

The second line contains an integer `T`, the number of test cases. (`1 <= T <= 10^4`)

Each of the next `T` lines contains a string `S` of exactly five characters from ATCND, representing your initial roll, and an integer `K`, the maximum number of rerolls you can perform. (`1 <= K <= 5`)

## Output

For each test case, print a string `R` and a number `P`.

`R` should be nonempty and contain up to five characters from ATCND, representing the dice that should be rerolled. It is guaranteed that the objective is not met initially, at least one reroll is possible, and the probability of winning is strictly positive (i.e., `P \gt 0`). The characters may be printed in any order.

The number `P` should be the maximum probability of achieving the objective when playing optimally. The answer is considered correct if the absolute error does not exceed `10^{-4}`.


## Examples

### Input 1

```text
T
4
NNNNA 1
NNNAA 1
NNNNA 2
AAAAA 1
```

### Output 1

```text
A 0.1666666667
AA 0.3055555556
A 0.3202160494
AAAAA 0.5981224280
```

### Input 2

```text
ATC
4
NTNAN 2
TNCNT 1
NTADD 1
AATDT 5
```

### Output 2

```text
AT 0.0543981481
T 0.3333333333
NDD 0.4212962963
AAT 0.9121533206
```

## Note

Here is an example of the game:

 -  Suppose the objective is `O = \texttt{ATT}` (meaning we need at least 1 Adventurer and 2 Torches).
-  Your initial roll is `S = \texttt{ANNCC}` (1 Adventurer, 2 locked Black Masks and 2 Keys).
-  On your first reroll, you decide to reroll both Keys (CC), since you can't reroll any Black Masks. Suppose the rerolled dice land on AD, meaning you now have AANND.
-  Now, on your second reroll, you decide to reroll an Adventurer and the Golden Mask, and since you are rerolling the Golden Mask, you gain the right to reroll up to two locked Black Masks. In total, you reroll 4 dice (ADNN).
-  Suppose the rerolled dice land on TTNC, meaning the final dice configuration becomes ATTNC (which contains at least 1 A and 2 T's), successfully meeting the objective with two rerolls.
