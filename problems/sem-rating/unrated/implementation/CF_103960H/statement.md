# CF_103960H — Helping the Transit

- Codeforces: [103960H](https://codeforces.com/gym/103960/problem/H)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 813
- Titulo original: H. Helping the Transit
- time limit per test: 0.25 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

The president of Nlogonia decided, by decree, that all the streets of Nlogonia should be one-way. Due to the lack of knowledge of elementary science, there was no proper planning for the changes. After the new system came in place, people would not be able to go to work, or would not be able to return home from work, for example. As a result, there was chaos and riots in lots of cities.

The president was impeached and the new administration of the country hired a team of scientists to solve the problem. In turn, the committee hired you, an expert in complexity of algorithms, to help them with the efficient computation of solutions.

So, for each city, you are given the reference points of the city, and the one-way streets, each of which connects two reference points. Your task is to determine the minimum number of one-way bridges that must be built in order to have full connectivity in the city. Each bridge should also connect two reference points.

## Input

 The first line of the input contains two integers, `N` and `M` (`1 <= N <= 10^4, 0 <= M <= 10^6)`, where `N` is the number of reference points and `M` is the number of streets. Each one of the next `M` lines contains two integers, `R` and `S`, `1 <= R, S <= N`, `R != S`, that corresponds to a street connecting `R` to `S`, so that every vehicle in that street must move away from `R`, towards `S`.

## Output

 Your program must print a single line containing the minimum number of bridges that are necessary to make the inhabitants happy.

## Examples

### Input 1

```text
7 7
1 2
2 3
3 1
6 1
6 4
4 5
7 6
```

### Output 1

```text
2
```

### Input 2

```text
7 7
2 1
3 2
1 3
1 6
4 6
5 4
6 7
```

### Output 2

```text
2
```

### Input 3

```text
2 1
1 2
```

### Output 3

```text
1
```

### Input 4

```text
3 3
1 2
2 3
3 1
```

### Output 4

```text
0
```

### Input 5

```text
2 0
```

### Output 5

```text
2
```

### Input 6

```text
6 4
1 2
1 3
4 6
5 6
```

### Output 6

```text
3
```
