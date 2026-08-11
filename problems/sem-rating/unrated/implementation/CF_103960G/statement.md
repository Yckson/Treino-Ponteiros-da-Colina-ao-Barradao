# CF_103960G — Geometry of Triangles

- Codeforces: [103960G](https://codeforces.com/gym/103960/problem/G)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 185
- Titulo original: G. Geometry of Triangles
- time limit per test: 1 second
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Every polygon can be constructed by joining triangles. In particular, we can do this iteratively: we start with a triangle, we add a second triangle identifying one of its sides to one of the sides of the initial triangle, we add a third triangle identifying one of its sides to one of the free sides of one of the original triangles, and so on. We will only consider polygons that can be constructed in this way, where each added triangle touches (and is identified with) exactly one side of a previously positioned triangle.

Given a polygon `P`, let `T` be the set of triangles used to form it. The sides of each triangle are line segments. Let `L` be the set of segments that are sides of some triangle in `T`. Note that each element of `L` is one side of one or two elements of `T`.

Once we have a polygon positioned in the plane, in some cases we can remove some of the triangles that compose it, without changing the set `L`. We want to remove triangles so that the set `L` is maintained and the total area of the remaining triangles is minimal. Equivalently, we want to select a subset `S` of triangles from `T` such that:

 -  Every element of `L` is the side of at least one triangle in `S`; and
-  The sum of the areas of the elements of `S` is as small as possible.

## Input

The first line of the input contains an integer `N`, `1<= N <= 10^5` corresponding to the number of triangles in the triangulation of `P`. Each of the following `N` lines contains 6 numbers, `x_1, y_1, x_2, y_2, x_3` and `y_3`, indicating the existence of a triangle with coordinates `(x_1,y_1), (x_2, y_2)` and `(x_3,y_3)`. The triangles are given in arbitrary order. All coordinates will be integers with absolute value at most `10^6`.

## Output

Print the minimum area possible, respecting the conditions of the problem, with exactly one decimal place.


## Examples

### Input 1

```text
4
0 0 0 10 10 0
10 10 0 10 10 0
10 10 0 10 0 20
10 10 20 0 10 0
```

### Output 1

```text
150.0
```

### Input 2

```text
3
0 0 0 10 10 0
10 10 0 10 10 0
10 10 20 0 10 0
```

### Output 2

```text
150.0
```

### Input 3

```text
1
0 0 1 0 0 1
```

### Output 3

```text
0.5
```

## Note

  In the figure above , the triangulations `T_1 = \{a, b, c, d\}` and `T_2 = \{a, b, c\}` represent, respectively, the first and second examples. Note how `S_1 = \{a, c, d\}` is a valid subset for the first case. Triangle `b` is left out, but all of its sides are present in the selected triangles.
