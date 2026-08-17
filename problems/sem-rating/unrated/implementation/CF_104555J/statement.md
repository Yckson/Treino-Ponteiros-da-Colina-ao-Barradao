# CF_104555J — Jumping to Victory

- Codeforces: [104555J](https://codeforces.com/gym/104555/problem/J)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 43
- Titulo original: J. Jumping to Victory
- time limit per test: 8 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

The stage is set for the Olympic Games super volleyball finals, and tensions are high! Ricardão, the coach of a competing team, is meticulously positioning his players for a strategic advantage. However, a lingering concern plagues him: the possibility that some areas of the court might be inadequately covered by his players. This could lead to exhausting lateral jumps to reach the ball.

In this high-stakes match, your task is to assist Coach Ricardão by analyzing the court layout and the positions of the players. Calculate the maximum jump distance required by any player to intercept the ball, ensuring that no point on the court remains vulnerable. Professional super volleyball teams are very good, and can easily determine which is the closest player to where the ball will fall; only this player will try to reach it, all other will remain still.

The court is defined by an axis-aligned rectangle `\mathcal{R}` defined by its four vertices and the players modelled as a set of `N` points inside this rectangle. Your task is to determine the smallest distance `d` such that any point on the court can be reached by at least one player, if a player can jump a distance of up to `d` in any direction. Remember: the border of the court is also part of the court and must be covered by the players!

## Input

The first four lines contains the four vertices of `\mathcal{R}`; that is, the `i`-th line contains two integers `x_i` and `y_i` (`-10^5 <= x_i, y_i <= 10^5`), representing the coordinates of the `i`-th vertex of `\mathcal{R}`. The fifth line contains a single integer `N` (`1 <= N <= 10^5`), representing the number of players. Each of the following `N` lines contains the players coordinates, where the `i`-th line contains two integers `x_i` and `y_i` (`-10^5 <= x_i, y_i <= 10^5`), representing the coordinates of the `i`-th player. It's guaranteed that every player is inside the court.

## Output

Output a single line with the least `d` that is enough to guard the whole court. The output will be considered correct if it is within an absolute or relative error of `10^{-5}` of the correct answer.

## Examples

### Input 1

```text
-1 -1
1 -1
1 1
-1 1
1
0 0
```

### Output 1

```text
1.414213562373
```

### Input 2

```text
1 -1
-1 3
1 3
-1 -1
3
0 0
1 3
-1 3
```

### Output 2

```text
1.666666666667
```
