# CF_106073M — Minas Gerais' walls

- Codeforces: [106073M](https://codeforces.com/gym/106073/problem/M)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1040
- Titulo original: M. Minas Gerais' walls
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Due to their privileged location and favorable terrain, only frontal walls were usually necessary to protect medieval cities in Minas Gerais. Even today, it is possible to find traces of these constructions when admiring the beautiful horizon of the region.

Each of these walls was composed of a number of consecutive segments, each with an initial height measured in units, corresponding to the number of blocks used to build it.

From time to time, the builders reinforced the walls by choosing a segment and stacking extra blocks in a staircase pattern: the chosen segment received `K` additional blocks, the previous one `K-1`, and so on until only `1` block was added or there were no more segments to the left.

The defense was considered as strong as its lowest segment.

Given the initial description of a wall, your objective is to determine the largest possible minimum height after applying a single reinforcement.

## Input

The first line contains two integers `N` `(1 <= N <= 10^5)`, the number of wall segments, and `K` `(1 <= K <= N)`, the number of blocks added to the chosen segment.

The second line contains `N` integers `x_1, x_2, ..., x_N` `(1 <= x_i <= 10^9)`, representing the initial heights of the segments.

## Output

Your program should print a single line, containing a single integer: the largest possible minimum height of the wall after a single reinforcement.


## Examples

### Input 1

```text
5 5
5 4 3 2 1
```

### Output 1

```text
6
```

### Input 2

```text
6 1
3 3 1 3 3 3
```

### Output 2

```text
2
```

### Input 3

```text
5 5
3 4 7 8 7
```

### Output 3

```text
7
```

## Note

Explanation of sample 3:

If we reinforce the first segment, the wall now has heights `[8, 4, 7, 8, 7]`. The lowest segment in this case has height `4`.

Reinforcing the last segment, we get `[4, 6, 10, 12, 12]`, where the minimum is `4`.

Of all the options, the best choice is to reinforce the second segment, resulting in `[7, 9, 7, 8, 7]`, where the minimum is `7`.

Therefore, the greatest possible minimum height is `7`.
