# CF_106636K — Turnstile

- Codeforces: [106636K](https://codeforces.com/gym/106636/problem/K)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 29
- Titulo original: K. Turnstile
- time limit per test: 2 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Running is useless, but if you insist...
— GePeTo

After the city he lives in was devastated by the overlord GePeTo, Pedro needs to escape to a survivors' shelter, but the only exit available is through the subway.

Unfortunately, he has no money to pay for the fare. However, he notices that there is a special property in the turnstile, which displays a number `C` representing the number of times someone has passed through it: the turnstile allows free passage if all digits of `C` are distinct!

Each person passing through the turnstile increases the counter `C` by `1`. Given the number `C` currently displayed by the turnstile, determine the minimum number of people that need to pass through it so that Pedro can finally pass for free and escape the city.

## Input

The first line contains a single integer `T` (`1 <= T <= 10^5`), the number of test cases.

Each of the next `T` lines contains a single integer `C` (`1 <= C <= 10^{10}`), representing the current number displayed by the turnstile.

## Output

For each test case, print a single line containing the integer `P`. If it is impossible to reach a state where all digits are distinct, print `-1`.

## Examples

### Input

```text
3
1
99
10000000000
```

### Output

```text
0
3
-1
```
