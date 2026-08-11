# CF_276C — Little Girl and Maximum Sum

- Codeforces: [276C](https://codeforces.com/problemset/problem/276/C)
- Score/rating: 1500
- Categoria local: `data-structures`
- Tags Codeforces: data structures, greedy, implementation, sortings
- Resolvidos no Codeforces: 42275
- Titulo original: C. Little Girl and Maximum Sum
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: stdin
- output: stdout

---

The little girl loves the problems on array queries very much.

One day she came across a rather well-known problem: you've got an array of `n` elements (the elements of the array are indexed starting from 1); also, there are `q` queries, each one is defined by a pair of integers `l_i`, `r_i` `(1 <= l_i <= r_i <= n)`. You need to find for each query the sum of elements of the array with indexes from `l_i` to `r_i`, inclusive.

The little girl found the problem rather boring. She decided to reorder the array elements before replying to the queries in a way that makes the sum of query replies maximum possible. Your task is to find the value of this maximum sum.

## Input

The first line contains two space-separated integers `n` (`1 <= n <= 2*10^5`) and `q` (`1 <= q <= 2*10^5`) — the number of elements in the array and the number of queries, correspondingly.

The next line contains `n` space-separated integers `a_i` (`1 <= a_i <= 2*10^5`) — the array elements.

Each of the following `q` lines contains two space-separated integers `l_i` and `r_i` (`1 <= l_i <= r_i <= n`) — the `i`-th query.

## Output

In a single line print, a single integer — the maximum sum of query replies after the array elements are reordered.

Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specifier.

## Examples

### Input 1

```text
3 3
5 3 2
1 2
2 3
1 3
```

### Output 1

```text
25
```

### Input 2

```text
5 3
5 2 4 1 3
1 5
2 3
2 3
```

### Output 2

```text
33
```
