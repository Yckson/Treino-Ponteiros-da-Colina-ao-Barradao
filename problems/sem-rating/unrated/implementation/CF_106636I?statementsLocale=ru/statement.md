# CF_106636I?statementsLocale=ru — Problem I. Collision Course

- Codeforces: [106636I?statementsLocale=ru](https://codeforces.com/gym/106636/problem/I?statementsLocale=ru)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 0
- Titulo original: I. Collision Course
- time limit per test: 4 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

GePeTo has assumed control of practically all machines on the planet. During a resistance mission, your team was cornered by an army of robots and the only option to escape is to use an old combat spaceship.

Viewed from above, the spaceship is shaped like a convex polygon. The robots are represented by points in the plane and are all initially outside the spaceship.

The navigation systems have been damaged: before departing, it is possible to choose only one direction, and then the spaceship will follow this direction indefinitely, without making turns or rotations.

A robot is destroyed if the spaceship passes over its position at any point during its movement. Positions on the boundary of the spaceship are also considered hit.

Determine the maximum number of robots that can be destroyed by choosing the spaceship's direction of movement optimally.

## Input

The first line contains a single integer `N` (`3 <= N <= 2 * 10^5`), the number of vertices of the polygon representing the spaceship.

Each of the next `N` lines contains two integers `x_u` and `y_u` (`-2 * 10^9 <= x_u, y_u <= 2 * 10^9`), representing the coordinates of the `u`-th vertex of the spaceship. The vertices are given in counter-clockwise order and form a convex polygon.

The next line contains a single integer `M` (`1 <= M <= 2 * 10^5`), the number of robots.

Each of the next `M` lines contains two integers `x_v` and `y_v` (`-2 * 10^9 <= x_v, y_v <= 2 * 10^9`), representing the position of the `v`-th robot.

It is guaranteed that all robots are initially outside the spaceship's polygon.

## Output

Print a single integer: the maximum number of robots that can be destroyed by choosing a direction of movement.


## Examples

### Input

```text
4
0 0
5 0
5 5
0 5
6
15 15
20 15
20 12
20 10
-15 0
0 20
```

### Output

```text
4
```

## Note

The spaceship can choose any non-zero direction in the plane.

Throughout the movement, its shape and orientation remain unchanged: all of its points move by the same distance and in the same direction.

A robot is considered destroyed if, at some instant, its position is inside or on the boundary of the polygon occupied by the spaceship.
