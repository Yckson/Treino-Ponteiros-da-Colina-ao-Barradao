# CF_103960E — Eliminating Ballons

- Codeforces: [103960E](https://codeforces.com/gym/103960/problem/E)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1793
- Titulo original: E. Eliminating Ballons
- time limit per test: 1.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

An enormous number of balloons are floating about in the Convention Hall after the Awarding Ceremony of the ICPC Subregional Contest. The manager of the Convention Hall is angry, because he will host another event tomorrow and the balloons must be removed. Fortunately this year Carlinhos came prepared with his bow and arrows to pop the balloons.

Also, luckily, due to the air conditioning flow, the balloons are all in the same vertical plane (that is, a plane parallel to a wall), although in distinct heights and positions.

Carlinhos will shoot from the left side of the convention hall, at a chosen height, in the direction of the right side of the Convention Hall. Each arrow moves from left to right, at the height it was shot, in the same vertical plane of the balloons. When an arrow touches a balloon, the balloon pops and the arrow continues its movement to the right, at a height decreased by 1. In other words, if the arrow was at height `H`, after popping a balloon it continues at height `H - 1`.

Carlinhos wants to pop all balloons shooting as few arrows as possible. Can you help him?

## Input

The first line of input contains an integer `N`, the number of balloons (`1 <= N <= 5 * 10^5`). Since all balloons are in the same vertical plane, lets define that the height of a ballon is given in relation to the `y`-axis and the position of a balloon is given in relation to the `x`-axis. Balloons are numbered from 1 to `N`. Balloon numbers indicate theis positions, from leftmost (balloon number 1) to rightmost (balloon number `N`), independent of their heights. The position of balloon number `i` is different from the position of balloon number `i+1`, for all `i`. The second line contains `N` integers `H_i`, where `H_i` indicates the height of balloon number `i` (`1 <= H_i <= 10^6` for `1 <= i <= N`). Notice that several balloons may be at the same height, but there are no repeated (position, height) pairs.

## Output

Your program must output a single line, containing a single integer, the minimum number of arrows that Carlinhos needs to shoot to pop all balloons.

## Examples

### Input 1

```text
5
3 2 1 5 4
```

### Output 1

```text
2
```

### Input 2

```text
4
1 2 3 4
```

### Output 2

```text
4
```

### Input 3

```text
6
5 3 2 4 6 1
```

### Output 3

```text
3
```

### Input 4

```text
5
1 1 1 1 1
```

### Output 4

```text
5
```
