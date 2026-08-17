# CF_104555K — `K` for More, `K` for Less

- Codeforces: [104555K](https://codeforces.com/gym/104555/problem/K)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 196
- Titulo original: `K` for More, `K` for Less
- time limit per test: 1.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

The life of those who study computer science is not always as easy as it seems. Some days you might be implementing a revolutionary algorithm, and other days you find yourself reading the same book for the tenth time. But at all times we are looking for the same thing: to optimize and automate tasks. In this case, a teacher needs your help to guide his students to the next exam. In the professor's opinion, it is not easy to decide how much time students should spend studying theoretical topics and how much time they should spend implementing algorithms.

This is not the first time that the professor has taught this subject, so the amount of data available is so large that he was able to create two polynomials to describe the final performance of each student. If the student spends `x` units of his time studying theory, his grade will increase by `t(x)`. If the student spends `x` units of his time implementing algorithms, his grade will increase by `p(x)`. In such a way that the student who spends the same amount `x` of time in each of the areas will have a final grade of `t(x) + p(x)`.

Recently one of the students has been standing out unpredictably. He does not hide his technique from anyone: "I study theory a lot more than practice!". The professor believes this is a lie and, to confirm his suspicion, he decided to estimate students grades if they always studied more theory than practice (or more practice than theory). Can you compute the polynomial `q(x) = t(x + K) + p(x - K)`? It will be able to describe every student grade if they change their study strategy.

## Input

The input consists of three lines. The first line contains two integers: `N`, representing the degree of the polynomials `t` and `p` (`1 <= N <= 10^5`) and `K` (`-10^5 <= K <= 10^5`). The second line contains the `N+1` coefficients of `t`, and the third line contains the `N+1` coefficients of `p`. The coefficients are given in increasing order of degree, with the last coefficient in the row corresponding to the term with degree `N`, all of which are non-negative with a maximum value of `10^6`.

## Output

Your program should print a line with `N+1` integers, the coefficients of the polynomial `q(x)` in increasing order of degree modulo 998244353.

## Examples

### Input 1

```text
1 2
1 2
0 1
```

### Output 1

```text
3 3
```

### Input 2

```text
2 0
1 2 3
4 5 6
```

### Output 2

```text
5 7 9
```

### Input 3

```text
2 -1
3 3 3
1 0 0
```

### Output 3

```text
4 998244350 3
```
