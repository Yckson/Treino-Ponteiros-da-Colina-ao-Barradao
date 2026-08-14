# CF_106636B — House Swapping

- Codeforces: [106636B](https://codeforces.com/gym/106636/problem/B)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 39
- Titulo original: B. House Swapping
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Home? What is that? I see houses.
— GePeTo

In order to teach people empathy, GePeTo demands that people often change houses, so that they learn to "live in another's shoes". There are `N` houses in the city, each housing one person, and on the `i`-th house GePeTo placed the label `\pi(i)` meaning that, every day at midnight, the person living in house `i` has to move to house `\pi(i)`. All people move at the same time, and it is guaranteed that after a move no house is left empty, and no house has two people.

We say `\pi` has a cycle of size `k` if, after `k` days, some person returns to the house where they initially lived, that is, if `\pi^k(x) = x` for some `1 <= x <= N`.

GePeTo asks you to swap the labels of two houses in order to maximize the size of the smallest cycle, that is, choose a single pair `(i, j)` and swap `\pi(i)` with `\pi(j)` to maximize the minimum `k` such that `\pi^k(x) = x` for some `1 <= x <= N`. You are allowed to choose `j = i`, in which case `\pi` remains unchanged.

## Input

The first line contains an integer `T` (`1 <= T <= 10^5`), the number of test cases.

Each test case consists of two lines. The first line contains an integer `N` (`2 <= N <= 2 * 10^5`), the number of houses. The second line contains `N` distinct integers between `1` and `N`, the `i`-th being `\pi(i)`. The sum of `N` over all test cases does not exceed `2 * 10^5`.

## Output

For each test case, print a line with three integers `k`, `i`, and `j` (`1 <= k, i, j <= N`), such that the maximum size of the minimum cycle is `k` after swapping positions `i` and `j`. If there are multiple answers, any valid answer will be accepted.

## Examples

### Input

```text
3
4
2 3 4 1
4
3 4 1 2
7
3 5 1 7 2 4 6
```

### Output

```text
4 1 1
4 1 2
3 1 2
```
