# CF_2257D — Bermuda Rectangle

- Codeforces: [2257D](https://codeforces.com/contest/2257/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 0
- Titulo original: D. Bermuda Rectangle
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

The Beaver is swimming across the ocean (yes, he can do that). Here, it aims to explore the Bermuda Rectangle. Of course, it poses no danger to The Beaver, but it is interesting from a scientific perspective.

Unlike the Bermuda Triangle, not much is known about the Bermuda Rectangle. Specifically, The Beaver knows for sure that the area of the rectangle is `S`, its sides are integers, and the bottom left corner is located at the point `(0, 0)`.

The Beaver is interested in how many cells from a rectangle with sides `x` and `y`, whose bottom left corner is at the point `(0, 0)`, can be located within the Bermuda Rectangle. A cell is considered to be within the Bermuda Rectangle if there exists a rectangle that satisfies the given constraints of the Bermuda Rectangle and contains that cell. Help The Beaver quickly respond to queries! You need to answer `q` such queries.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10 000`). The description of the test cases follows.

The first line of each test case contains two integers `S` and `q` — the area of the Bermuda Rectangle and the number of queries (`1 <= S <= 10^{12}`; `1 <= q <= 3 * 10^5`).

This is followed by `q` lines, each containing two integers `x, y` — the next query (`1 <= x, y <= S`).

It's guaranteed that the sum of `q` over all test cases doesn't exceed `3 * 10^5`.

It's guaranteed that the sum of `\sqrt{S}` over all test cases doesn't exceed `10^6`.

## Output

For each query, output a single integer on a separate line — the answer to the query.


## Examples

### Input

```text
3
6 4
2 3
4 5
6 6
1 1
5 2
2 2
3 4
8 2
3 1
5 6
```

### Output

```text
6
11
14
1
3
6
3
15
```

## Note

In the first test case, every cell of the rectangle `(2, 3)` is counted in the first query, since this rectangle itself can be the Bermuda Rectangle.

The second query of the first test case is illustrated in the figure. The answer to the query is the number of cells in the intersection of the blue and red shapes.

    4 blue rectangles — possible positions of the Bermuda Rectangle. Red — the rectangle of the query `(x, y) = (4, 5)` In the third query of the first test case, every cell that can lie in at least one possible Bermuda Rectangle is counted.

In the fourth query of the first test case, the only cell of the query rectangle can lie in the Bermuda Rectangle, so the answer is `1`.
