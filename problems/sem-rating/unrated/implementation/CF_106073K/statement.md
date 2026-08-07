# CF_106073K — Knockout, swiss and other kinds of tournaments

- Codeforces: [106073K](https://codeforces.com/gym/106073/problem/K)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 102
- Titulo original: K. Knockout, swiss and other kinds of tournaments
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Game and sports tournaments are becoming increasingly common, serving as a way to test participants' skills. The choice of the ideal format depends on the type of competition and the number of participants. For example, a "round-robin" format may be impractical when the number of participants is large, while a knockout tournament ("single-elimination") can be frustrating when two strong players face each other early. The "Swiss-system" format is a good compromise and is used in several competitions. In this format, if there are `N` participants, there will be about `\lceil \log_2 N \rceil` rounds, in which players always face opponents with similar scores.

A similar format has been adopted in some games as an alternative to the Swiss system: we will call this format "`(A,B)`-elimination". In this format, every match has a winner and a loser (i.e., there are no ties), and players always face opponents with the same score. Each participant plays until reaching `A` wins or `B` losses, whichever comes first. This format has a very convenient property: the number of rounds does not depend on the number of participants. In addition to scalability, this property makes it easier to define the prize structure, since it is possible to predict how many participants will finish with each possible score.

Despite its advantages, this format has a drawback: it is not always feasible, as there may not be enough opponents to complete a round under the given restrictions. For example, if `A=2` and `B=2`, and we have `N=6` participants, after the first round there would be 3 players with 1 win and 0 losses. Then, in the second round, since this number is odd, it would not be possible to pair all players with opponents of the same score. On the other hand, if `N=8`, the pairing is possible.

You have been asked to determine, given the values of `A` and `B`, the smallest number of players such that all rounds of the tournament can be completed.

## Input

The input consists of a single line containing two integers `A` and `B` (`1 <= A,B <= 10^{18}`) separated by a space, defining the tournament format as described above.

## Output

Your program should write a single line containing the smallest possible number of players in the tournament. Since the answer can be very large, print the answer modulo `10^9+7`.

## Examples

### Input 1

```text
3 3
```

### Output 1

```text
16
```

### Input 2

```text
3 2
```

### Output 2

```text
16
```
