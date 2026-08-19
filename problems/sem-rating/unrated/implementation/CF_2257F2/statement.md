# CF_2257F2 — Beaver's Jumping Track (Hard Version)

- Codeforces: [2257F2](https://codeforces.com/contest/2257/problem/F2)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 0
- Titulo original: F2. Beaver's Jumping Track (Hard Version)
- time limit per test: 3 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

This is the hard version of the problem. The difference between the versions is that in this version, the constraint on `x` and time limit are higher. You can hack only if you solved all versions of this problem.

The Beaver is training to jump long distances. The Beaver can already jump `x` meters. However, just jumping as far as possible is easy and boring. Therefore, the Beaver has created an unusual training track for jumping.

The track consists of `n` platforms; each platform consists of `d_i` meter cells. If the Beaver stands on platform number `i`, jumps, and lands back on the same platform, this results in `s_i` penalty points being awarded; otherwise, no penalty points are given. The Beaver can jump forward any integer number of cells less than or equal to `x`. Note that the Beaver can skip one or more platforms in a single jump without landing on them at all.

The Beaver has unlimited computational power in its mind and always jumps in such a way as to minimize the total penalty for passing the track. Moreover, the track is not constant, and sometimes the lengths and penalties of some platforms change. Learn to calculate what penalty the Beaver will get if it starts standing on the first cell of platform number `l` and finishes standing on the last cell of platform number `r`.

## Input

The first line contains three integers `n`, `q`, `x` — the number of sections of the track, the number of queries, and the maximum jump length, respectively (`1 <= n <= 10^6`; `1 <= q <= 10^4`; `1 <= x <= 10`).

The second line contains `n` integers `d_i` — the lengths of the platforms (`1 <= d_i <= 10^7`).

The third line contains `n` integers `s_i` — the penalties (`1 <= s_i <= 10^5`).

The following `q` lines describe the queries in one of the following formats:

 -  "1 `i` `v`" — set the length of the `i`-th platform to `v` (`1 <= i <= n`; `1 <= v <= 10^7`);
-  "2 `i` `y`" — set the penalty on the `i`-th platform to `y` (`1 <= i <= n`; `1 <= y <= 10^5`);
-  "? `l` `r`" — calculate the minimum penalty for passing the track consisting of platforms from `l` to `r` (`1 <= l <= r <= n`).

## Output

For each query of the third type, output a single number on a separate line — the minimum penalty.


## Examples

### Input

```text
5 8 3
4 2 5 1 3
4 2 7 1 5
? 1 3
2 2 10
? 1 3
1 1 2
? 1 3
? 2 5
1 3 2
? 2 5
```

### Output

```text
11
11
7
7
0
```

## Note

During the first query, the lengths of the course sections are `[4, 2, 5]` with costs `[4, 2, 7]`; the optimal route is

1 \rightarrow 4 \rightarrow 6 \rightarrow 8 \rightarrow 11 In this case, the penalty is `4 + 0 + 0 + 7 = 11`.

Before the second query, the penalty of the second course increased, but we never get it; thus, the answer to this query is also `11`.

Before the third query, we have the lengths of the courses `[2, 2, 5]`; then the route 1 \rightarrow 4 \rightarrow 6 \rightarrow 9 gives a penalty of 7, as the only penalizing jump is within one platform: `6 \rightarrow 9`.
