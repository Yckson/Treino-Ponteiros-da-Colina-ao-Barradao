# CF_104555A — Amusement Park Adventure

- Codeforces: [104555A](https://codeforces.com/gym/104555/problem/A)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 2659
- Titulo original: A. Amusement Park Adventure
- time limit per test: 0.3 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Meet Carlitos, a spirited adventure enthusiast with an insatiable love for amusement parks. Despite his vibrant passion, Carlitos faces a unique challenge – his height. As he eagerly plans his weekend escapade, he realizes that his vertical limitations might hinder his amusement park experience. It's not just about choosing a park; it's about finding one where he can enjoy the thrill of the rides.

Picture the kaleidoscope of colors, the jubilant laughter, and the heart-pounding rush of the rides. Carlitos has always been drawn to the energy of amusement parks. With the weekend approaching, he pores over park brochures, studying the height requirements of each ride. His goal is to maximize his enjoyment, and that's where you come in.

Your task is to help Carlitos determine the number of rides he can enjoy at a specific park. By considering his height and the minimum height requirements of each ride, guide him in making the most of his amusement park adventure.

## Input

The first line contains two integers, `N` and `H` (`1 <= N <= 6` and `90 <= H <= 200`), representing the number of rides in a park and Carlitos' height in centimeters, respectively.

The second line contains the minimum heights `A_1, ..., A_N` (`90 <= A_i <= 200`) of each ride in the park.

## Output

Output a single line with an integer indicating the number of rides Carlitos can go on, that is, the number of rides for which Carlitos' height is at least as large as the minimum height required.

## Examples

### Input 1

```text
1 100
100
```

### Output 1

```text
1
```

### Input 2

```text
6 120
200 90 100 123 120 169
```

### Output 2

```text
3
```
