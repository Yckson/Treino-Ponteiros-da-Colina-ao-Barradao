# CF_105327K — Karamell

- Codeforces: [105327K](https://codeforces.com/gym/105327/problem/K)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1004
- Titulo original: K. Karamell
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Karamell, Caramel, Caramello or Caramelo. Different languages, but you know what I'm talking about. Alice and Bob are twins and they also love caramels! So, as a birthday present, they asked for caramels to all the guests at the party they are organizing.

The day of the party Alice and Bob received their presents: `N` bags of caramels. The `i`-th bag contained `a_i` caramels.

Alice and Bob don't want to open the bags right away, they decided to distribute the caramels in the following way: the bags will be considered in order and, at the `i`-th step, the `a_i` caramels from the `i`-th bag are given to the person who has the least caramels at that moment. In case of a tie, Alice gets the caramels (after all, "ladies first").

One thing they didn't like is that, depending on the order in which the bags are considered, the final amount of caramels that each person receives can be different. For example, if the bags were ordered in the quantities described by the sequence `[1, 2, 2, 3]`, Alice would end up with `3` and Bob would end up with `5` candies. On the other hand, if they were considered in the order `[1, 2, 3, 2]`, both would end up with `4`.

You forgot to buy candies for the birthday children, but you decided to give them an even more interesting gift: a program that determines a way to order the bags so that Alice and Bob get the same amount of candies, if possible.

## Input

The first line contains a single integer `N` (`1 <= N <= 100)`, indicating the number of bags. The second line contains `N` integers `a_1, ..., a_N` (`1 <= a_i <= 100)`, where `a_i` indicates the number of candies in bag `i`.

## Output

The output must be a single line. If it is impossible to find an order as requested, print `-1`. Otherwise, print `N` integers separated by spaces, indicating a valid ordering of the `a_i` values that guarantees that the candies will be divided equally among the siblings.

## Examples

### Input 1

```text
4
1 2 2 3
```

### Output 1

```text
1 2 3 2
```

### Input 2

```text
5
1 2 2 3 6
```

### Output 2

```text
1 2 6 2 3
```

### Input 3

```text
6
1 12 21 23 33 34
```

### Output 3

```text
-1
```
