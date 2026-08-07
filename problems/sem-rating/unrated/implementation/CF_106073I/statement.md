# CF_106073I — Investigating Quadradômeda

- Codeforces: [106073I](https://codeforces.com/gym/106073/problem/I)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 715
- Titulo original: I. Investigating Quadradômeda
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

The Society for Beyond-Earth Cosmonautics (SBC) is training its teams for the next edition of the International Challenge of Planetary Cosmonautics (ICPC).

SBC will conduct a simulated exploration of a distant galaxy called Quadrameda. For this mission, `N` stars were selected for their geometrically strategic locations, and a visitation order was determined, numbered from `1` to `N`. To prepare the teams, simplified models are used, in which each star is represented by a point in the plane with integer coordinates `(x_i, y_i)`.

The stars are arranged so that, for each `1 <= i \lt N`, star `i` is aligned with star `i+1`, that is, they share the same `x` coordinate or the same `y` coordinate.

The mission's objective is to orbit each star `i` along a circle of constant integer radius `R_i >= 1`. During the simulation, the spacecraft orbits the current star and, upon reaching the point of the orbit closest to the next star, leaves this orbit and immediately begins orbiting the following star. For this maneuver to be possible, for each `1 <= i \lt N`, the radius `R_i` must be strictly less than the Euclidean distance between stars `i` and `i+1`.

The example below illustrates a valid orbit configuration with `N=3`; the stars are at the points `(0,0)`, `(4,0)` and `(4,4)`. In this configuration, we have `R_1=1`, `R_2=3` and `R_3=1`.

  Your task is to determine the largest integer value of `R_1` such that it is possible to choose values `R_1, R_2, ..., R_N` that satisfy all the conditions above. If no valid orbit configuration exists, report that the mission is impossible.

## Input

The first line contains an integer `N` (`2 <= N <= 10^5`), the number of stars.

Each of the next `N` lines contains two integers `x_i` and `y_i` (`|x_i|, |y_i| <= 10^9`), the coordinates of star `i`. For each `1 <= i \lt N`, stars `i` and `i+1` are aligned horizontally or vertically. All stars are located at distinct points.

## Output

Your program should produce a single line containing the largest integer value of `R_1` such that a valid orbit configuration exists, or -1 if the mission is impossible.

## Examples

### Input 1

```text
3
0 0
4 0
4 4
```

### Output 1

```text
3
```

### Input 2

```text
5
0 0
4 0
4 2
4 6
6 6
```

### Output 2

```text
-1
```

### Input 3

```text
4
0 0
4 0
4 4
4 7
```

### Output 3

```text
2
```
