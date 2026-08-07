# CF_106073C — Collatz polynomial

- Codeforces: [106073C](https://codeforces.com/gym/106073/problem/C)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1617
- Titulo original: C. Collatz polynomial
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Everyone knows (or has heard of) the famous Collatz Conjecture: take a positive integer. If it is odd, multiply by 3 and add 1. If it is even, divide by 2. Repeat the process until you reach 1. Despite its simplicity, no one knows how to prove whether the sequence really always reaches 1, regardless of the initial number.

Aline, a fan of this type of curiosity, decided to create a variation using polynomials instead of numbers. To keep things simple, she works only with polynomials whose coefficients are 0 or 1, that is, each power of `x` appears at most once.

The game works like this:

 -  If the polynomial has a constant term (a term that does not depend on `x`), Aline multiplies the polynomial by `(x + 1)` and then adds 1. If any resulting coefficient equals 2, the corresponding term is discarded (note that coefficients greater than 2 cannot arise).
-  If the polynomial has no constant term, Aline divides the polynomial by `x`.
 This process is repeated until the polynomial reduces to `P(x) = 1`.Consider `P(x) = x^3 + 1`. In the first step there is a constant term, so we calculate: (x^3 + 1) \cdot (x + 1) + 1 = x^4 + x^3 + x + 1 + 1. Since the coefficient of the constant term is `2`, this term is discarded, leaving:  x^4 + x^3 + x.

Next, since there is no constant term, we divide by `x`: x^3 + x^2 + 1.

Continuing:

 -  Step 3: `x^4 + x^2 + x`
-  Step 4: `x^3 + x + 1`
-  Step 5: `x^4 + x^3 + x^2`
-  Step 6: `x^3 + x^2 + x`
-  Step 7: `x^2 + x + 1`
-  Step 8: `x^3`
-  Step 9: `x^2`
-  Step 10: `x`
-  Step 11: `1`
 In total, it took 11 operations to reach the polynomial `P(x) = 1`.Aline needs help to study this variation of the Collatz Conjecture. Since doing these calculations manually is prone to errors, write a program that determines the number of operations needed until the polynomial becomes `P(x) = 1`.

## Input

The first line contains an integer `N` (`0 <= N <= 20`), indicating the degree of the polynomial.

The second line contains `N + 1` integers `a_N, a_{N-1}, ..., a_0` (each equal to 0 or 1), where `a_i = 1` indicates that the term `x^i` is present in the polynomial, and `a_i = 0` indicates that it is not. Note that `a_N = 1`, since the degree of the polynomial is `N`.

## Output

Your program must output a single line, containing an integer, representing the number of operations needed until the polynomial becomes `P(x) = 1`.

## Examples

### Input 1

```text
3
1 0 0 1
```

### Output 1

```text
11
```

### Input 2

```text
2
1 0 1
```

### Output 2

```text
6
```

### Input 3

```text
2
1 0 0
```

### Output 3

```text
2
```

### Input 4

```text
0
1
```

### Output 4

```text
0
```
