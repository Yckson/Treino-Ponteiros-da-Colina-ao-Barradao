# CF_103960M — Hopscotch Marathon

- Codeforces: [103960M](https://codeforces.com/gym/103960/problem/M)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 172
- Titulo original: M. Hopscotch Marathon
- time limit per test: 2 s
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

October 8th, 2022. This is the date of the most awaited event of the year by computer science students across the country. No, we are not talking about ICPC.

We are talking, of course, about Hopscotch! For those unfamiliar, Hopscotch is an annual competition traditionally held as an ICPC side event. Live streamed to spectators from all continents, and to practitioners of the most esoteric programming languages, this exotic variant of the popular children's game takes place in an infinite, spiral-shaped court, subdivided into sequentially numbered areas starting at zero, as depicted below.

  This year, Hopscotch has attracted a record number of `N` participants, numbered sequentially from `1` to `N`. It is known that the `i`-th participant starts in the area numbered `A_i`.

Hopscotch consists of `Q` rounds. During the `q`-th round, Carlão, beloved Hopscotch organizer for longer than anyone can remember, will communicate two integers to participants: `c_q` and `d_q`. This is an order for all participants with identifying number `i` such that `i` and `c_q` share a common integer factor larger than `1` to retrogress `d_q` positions in the Hopscotch court, one by one, never going back further than position `0`. (Any participant who eventually returns to position `0` should remain there indefinitely, ignoring any further retrogress commands, so as not to leave the court.)

Under the assumption that the participants have executed the instructions perfectly (they would never want to disappoint Carlão), your task is to determine, for each participant, the number of the round in which he or she returns to position `0` (or otherwise indicate that this never happens).

## Input

The first line contains the integers `N` and `Q` (`1 <= N, Q <= 10^5`). The second line contains `N` integers, namely, `A_1`, `A_2`, `*s`, `A_N` (`1 <= A_i <= 10^9`). Each of the next `Q` lines contains two integers, `c_q` and `d_q` (`1 <= c_q <= 10^5`, `1 <= d_q <= 10^9`).

## Output

You must output `N` lines. The `i`-th line should contain a single integer, indicating the number of the round when the `i`-th participant returns to position `0` (or the value `-1`, if that never happens).

## Examples

### Input 1

```text
7 6
10 20 30 40 50 60 70
2 25
3 36
100 42
5 10
7 70
1 1000
```

### Output 1

```text
-1
1
2
3
4
2
5
```

### Input 2

```text
6 4
100 100 100 100 100 100
2 50
3 50
5 99
5 1
```

### Output 2

```text
-1
-1
-1
-1
4
2
```
