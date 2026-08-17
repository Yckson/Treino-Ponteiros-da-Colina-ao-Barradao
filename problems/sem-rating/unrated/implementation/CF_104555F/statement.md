# CF_104555F — Fatigue-Fighting Vacation

- Codeforces: [104555F](https://codeforces.com/gym/104555/problem/F)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 2084
- Titulo original: F. Fatigue-Fighting Vacation
- time limit per test: 0.3 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

William is planning his upcoming vacations. A recurring problem when he takes vacations is the need to deal with fatigue. Some days he does not enjoy much, as after several activities, the fatigue becomes greater than what he can deal with.

This time, William had an idea. He will estimate the impact on his disposition for each of the tourism activities. He noticed that some of the vacation activities, such as sports and hikes, are tiring and consume his disposition, while other activities, such as theatre plays and musicals, are invigorating and restore his disposition.

More precisely, William starts with `D` units of disposition and separates his activities into two groups: `C` tiring activities and `R` invigorating activities. Each tiring activity requires a certain amount of disposition and consumes that amount of disposition when performed. Each invigorating activity provides him with a certain amount of disposition when performed. Additionally, he arranges the activities in each group according to his preferences, as there are activities he is more willing to perform. It is important to note that activities from both sets can be interleaved, but William will never do an activity from one group without having done all the previous activities from that group, as this would not conform with his preferences.

Throughout his vacation, when deciding which activity to do next, he will choose the first untaken tiring activity, provided he has enough disposition to do it. Otherwise, he will perform the next untaken invigorating activity, if any remains, replenishing a certain amount of disposition. Naturally, if there are no remaining tiring activities at any point, he can simply perform all the remaining invigorating activities.

Considering this process, William has asked for your help to determine how many activities (including both tiring and invigorating ones) he will be able to perform.

## Input

The first line of input contains three integer numbers, `D`, `C`, and, `R`, representing, respectively, the initial amount of disposition, the number of tiring activities, and the number of invigorating activities (`1 <= D <= 10^5`, `1<= C <= 10^4`, and `1 <= R <= 10^4`). Each of the next `C` lines contains an integer number `C_i` (`1 <= C_i <= 10^5` for `1 <= i <= C`), representing the required amount of disposition for a tiring activity, in order of preference. Finally, each of the next `R` lines contains an integer number `R_i` (`1 <= R_i <= 10^5` for `1 <= i <= R`), representing the provided amount of disposition for an invigorating activity, in order of preference.

## Output

Print a single line with a single integer number, the total number of activities (including both tiring and invigorating ones) that William will be able to perform.

## Examples

### Input 1

```text
40 3 3
30
20
10
5
5
5
```

### Output 1

```text
5
```

### Input 2

```text
40 2 2
60
80
5
10
```

### Output 2

```text
2
```

### Input 3

```text
100 3 1
60
60
50
10
```

### Output 3

```text
2
```
