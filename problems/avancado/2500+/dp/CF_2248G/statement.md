# CF_2248G — No Balance Left

- Codeforces: [2248G](https://codeforces.com/problemset/problem/2248/G)
- Score/rating: 3000
- Categoria local: `dp`
- Tags Codeforces: bitmasks, dp, math
- Resolvidos no Codeforces: 102
- Titulo original: G. No Balance Left
- time limit per test: 6 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Alisa has a shopping card with an initial balance of `h`. There are `n` types of products in a supermarket. A product of type `i` costs `c_i`, and Alisa can buy any number of products of each type.

There are also `m` rebate activities. The `j`-th activity applies to a purchase if its total cost is at least `a_j` and gives a rebate of `b_j`.

For each purchase, Alisa performs the following operations:

 -  She chooses one or more products whose total cost `x` does not exceed the current balance on her card and pays `x` using the card.
-  Among all rebate activities that apply to this purchase, the one with the largest rebate takes effect and its rebate is added to the card balance. If no rebate activity applies, no rebate is added.
For every `h` from `1` to `s`, determine whether Alisa can make the balance on her card equal to `0` after finitely many purchases.

## Input

The first line contains three integers `n`, `m`, and `s` (`1 <= n, m, s <= 125 000`) — the number of product types, the number of rebate activities, and the maximum initial balance to consider, respectively.

The second line contains `n` integers `c_1, c_2, ..., c_n` (`1 <= c_i <= 125 000`) — the price of a product of each type.

The `i`-th of the next `m` lines contains two integers `a_i` and `b_i` (`1 <= a_i, b_i <= 125 000`) — the spending threshold and the rebate of the `i`-th activity, respectively.

It is guaranteed that `a_1 \lt a_2 \lt *s \lt a_m` and `b_1 \lt b_2 \lt *s \lt b_m`.

## Output

Print `s` lines. For each `i` (`1 <= i <= s`), print "YES" if Alisa can make the balance on her card equal to `0` when its initial balance is `i`, and print "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.


## Examples

### Input 1

```text
2 1 15
4 7
8 4
```

### Output 1

```text
NO
NO
NO
YES
NO
NO
YES
YES
NO
NO
YES
YES
NO
YES
YES
```

### Input 2

```text
5 3 25
4 8 12 16 20
6 8
7 9
8 10
```

### Output 2

```text
NO
NO
NO
YES
NO
NO
NO
YES
NO
YES
NO
YES
NO
YES
NO
YES
NO
YES
NO
YES
NO
YES
NO
YES
NO
```

## Note

In the first example, Alisa can make the balance equal to `0` when the initial balance is `15` as follows:

 -  She buys one product of each type for a total cost of `4 + 7 = 11`. The balance decreases from `15` to `4`.
-  Since `11 >= 8`, the rebate of `4` takes effect. The balance increases from `4` to `8`.
-  She buys one product of the first type for `4`. No rebate activity applies, so the balance decreases from `8` to `4`.
-  She buys one product of the first type again for `4`. No rebate activity applies, so the balance decreases from `4` to `0`.
Therefore, the `15`-th line of the first example output is "YES".

In the second example, if the initial balance is `4`, Alisa can buy one product of the first type for `4`. Since `4 \lt 6`, no rebate activity applies, and the balance becomes `0`. Therefore, the fourth line of the second example output is "YES". If the initial balance is `1`, no product is affordable, so the first line is "NO".
