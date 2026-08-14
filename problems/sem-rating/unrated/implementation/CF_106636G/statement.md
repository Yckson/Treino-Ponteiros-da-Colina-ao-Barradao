# CF_106636G — The Four Fours

- Codeforces: [106636G](https://codeforces.com/gym/106636/problem/G)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 9
- Titulo original: G. The Four Fours
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Four is the only number whose number of letters equals its value. Coincidence? I think not.
— GePeTo

Lately, GePeTo has developed a fascination with the digit `4`, declaring it the most elegant digit in existence. To prove your mathematical prowess, GePeTo challenges you to the classic "Four Fours" puzzle.

Given a non-negative integer target `X`, your goal is to construct a mathematical expression that evaluates to `X` using **exactly four** digits 4 and any combination of the following allowed operators and notation:

 -  Basic arithmetic: +, -, *, /
-  Exponentiation: ^{}
-  Parentheses: ()
-  Decimal point: . (e.g., .4 for `0.4`, 4.4)
-  Square root: sqrt
-  Factorial: !
Some examples of valid expressions:

 -  5 = (4 * 4 + 4) / 4
-  14 = 4 * (4 - .4) - .4
-  22 = 44 / 4 * sqrt(4)
-  27 = 4 - 4/4 + 4!
-  60 = (4 + 4)^sqrt(4) - 4

## Input

The first line contains a single integer `T` (`1 <= T <= 50`), the number of test cases.

Each of the next `T` lines contains an integer `X` (`0 <= X <= 70`).

## Output

For each test case, print a single line containing a valid expression using exactly four 4's that evaluates to `X`. The expression must have at most 25 characters. If multiple valid expressions exist, any of them will be accepted.

The expression must be well-behaved:

 -  The factorial operator ! may only be applied to non-negative integers.
-  The square root operator sqrt may only be applied to non-negative integers and must yield an integer result.
-  Any exponentiation must use an integer exponent.
-  The numerator and denominator of any intermediate rational value may never exceed `10^9`.

## Examples

### Input

```text
6
5
14
22
27
60
0
```

### Output

```text
((44 - 4!) / 4)
4.4 + (.4 * 4!)
4! - (4 + 4) / 4
4 - (4/4 - 4!)
(4 + 4)^sqrt(4) - 4
44-44
```
