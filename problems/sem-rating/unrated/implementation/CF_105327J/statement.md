# CF_105327J — Journey through Colors

- Codeforces: [105327J](https://codeforces.com/gym/105327/problem/J)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 41
- Titulo original: J. Journey through Colors
- time limit per test: 10 s
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

In the land of Oz, roads are paved with colored stones. Each road connects exactly two cities, can be traveled in both directions, and is colored with stones of a single color.

Dorothy is visiting Oz for the first time and wants to take a tour of the country, meeting the following conditions:

  -  The tour must start and end in the same city.
-  The tour must pass through each road in the country exactly   once and cannot use two consecutive roads (i.e., one   immediately after the other) that have the same color.
-  The first and last roads of the tour must have different colors.
Figure (a) below illustrates an example with five cities and six roads. Figure (b) shows a possible tour that starts and ends in city 2 and satisfies the road color restrictions. In figure (b), the tour starts in city 2 and goes, in sequence, through roads 1 (red), 3 (green), 4 (blue), 2 (red), 6 (blue) and, finally, 5 (green).

  Help Dorothy find such a tour or, if it is not possible, indicate that it does not exist.

## Input

The first line of the input contains three integers, `N`, `M`, and `K`, representing the number of cities (`2 <= N <= 1000`), the number of roads (`1 <= M <= 1000`), and the number of colors (`1 <= K <= 1000`), respectively. Cities are identified by integers from `1` to `N`, roads are identified by integers from `1` to `M`, and colors are identified by integers from `1` to `K`. Each of the following `M` lines describes a road and contains three integers `I`, `J`, and `C`, where `I` and `J` represent cities (`1 <= I, J <= N`, and `I != J`), and `C` indicates the color of road `1 <= C <= K`. The roads are given in the order of their identification, that is, the first road in the input is number `1`, the second road is number `2`, and so on.

## Output

If there is no tour that satisfies the constraints, print a single integer `-1`. Otherwise, your program should output two lines describing a valid tour. The first line should contain the identifier of the starting city of the tour. The second line should contain `M` distinct integers, each identifying a road, in tour order. If there is more than one possible tour, print any one of them.


## Examples

### Input 1

```text
5 6 3
1 2 1
2 3 1
1 4 2
2 4 3
2 5 2
3 5 3
```

### Output 1

```text
1
3 4 2 6 5 1
```

### Input 2

```text
2 4 2
1 2 1
1 2 1
1 2 2
1 2 2
```

### Output 2

```text
1
4 2 3 1
```

### Input 3

```text
6 6 3
1 2 1
2 3 2
3 1 3
4 5 1
5 6 2
6 4 3
```

### Output 3

```text
-1
```

### Input 4

```text
3 2 2
1 2 1
1 2 2
```

### Output 4

```text
1
2 1
```

### Input 5

```text
3 3 1
1 2 1
2 3 1
3 1 1
```

### Output 5

```text
-1
```

## Note

Explanation for example 1: This is the example from the statement. There are five cities, six roads and three colors (`1 =` red, `2 =` green, `3 =` blue). Note also that there are other possible tours, for example starting from city 1: `3 \rightarrow 4 \rightarrow 2 \rightarrow 6 \rightarrow 5 \rightarrow 1`.
