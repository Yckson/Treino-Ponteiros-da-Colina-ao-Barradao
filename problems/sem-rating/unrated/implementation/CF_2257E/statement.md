# CF_2257E — Busy Beaver

- Codeforces: [2257E](https://codeforces.com/contest/2257/problem/E)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 0
- Titulo original: E. Busy Beaver
- time limit per test: 2 seconds
- memory limit per test: 512 megabytes
- input: standard input
- output: standard output

---

The Beaver founded a construction company called "Busy Beaver". And now, in order to build up the company's reputation, it needs to construct the tallest building possible.

The company has an initial capital of `x` carrots (a very valuable currency for beavers) and `n` projects available for construction. A separate site has been allocated for each project, and nothing has been built there yet. A building project is represented by a sequence of contracts for constructing the next floor. To build the `j`-th floor of the `i`-th building, it is necessary to spend `a_{i, j}` carrots; upon completing it, the company immediately receives `b_{i,j}` carrots, which are added to the budget, and the company may use them to build higher floors of the same building or to work on other projects. Since the company is still young, not all contracts are necessarily profitable; in other words, it is possible that `a_{i,j} \gt b_{i,j}`.

The Beaver hired you to plan the company's course of action. You choose in which order to build which floors. Note that it is not necessary to complete projects, or even to start them at all. Moreover, between constructing floors of the same building, it is allowed to complete an arbitrary number of contracts unrelated to that building. The main goal is — to build the tallest building possible.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 3 * 10^4`). The description of the test cases follows.

The first line of each input data set contains integers `n` and `x` — the number of building projects and the initial amount of money (`1 <= n <= 2 * 10^5; 0 <= x <= 10^{18}`).

Next, there are `n` descriptions of projects. The first line of the description of project number `i` contains the number `m_i` — the maximum number of floors available for construction in this building (`1 <= m_i <= 2 * 10^5`).

The second line of the project description contains `m_i` integers `a_{i, 1}, a_{i, 2}, ... a_{i, m_i}` — the costs of building the floors. The third line of the project description contains `m_i` integers `b_{i, 1}, b_{i, 2}, ... b_{i, m_i}` — the profits from building the floors. `(0 <= a_{i, j}, b_{i, j} <= 10^9)`.

It is guaranteed that the sum of `m_i` over all test cases does not exceed `2 * 10^5`.

## Output

For each set of input data, output two numbers — the height, in floors, of the tallest building that can be constructed, and the smallest index of the building for which it is possible to build that number of floors.


## Examples

### Input

```text
2
1 6
4
4 4 2 1
2 4 1 1
2 3
2
4 4
5 5
2
2 20
4 0
```

### Output

```text
4 1
2 1
```

## Note

In the first set, there are enough carrots to sequentially build all `4` floors of the only building.

In the second set, you need to first build the first floor of the second building, earning `2` carrots from it, after which you can build both floors of the first building.
