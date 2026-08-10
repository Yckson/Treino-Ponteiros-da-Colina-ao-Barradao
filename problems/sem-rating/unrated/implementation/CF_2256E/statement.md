# CF_2256E — Even If the World Turns

- Codeforces: [2256E](https://codeforces.com/contest/2256/problem/E)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 0
- Titulo original: E. Even If the World Turns
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Now, no matter what anyone says, I am the happiest girl in the world.
— Chtholly

This is a run-twice (communication) problem.

At the Fairy Warehouse, Nygglatho prepared an unusual game for Chtholly and Willem.

They would be separated and unable to exchange a single word. Between them there would be only a black-and-white picture — one that Nygglatho could shift, rotate, reflect, or even invert its colors.

Nygglatho saw it as a test of how well they understood each other. Chtholly and Willem perhaps saw only another kind of promise. No matter how the world turned, they would still find the same place.

The two players are Chtholly and Willem. The jury, acting as Nygglatho, first communicates with Chtholly. After Chtholly finishes, the jury communicates with Willem. Chtholly and Willem may agree on the strategy they will use beforehand, but they cannot directly pass information to each other.

In each test case, Nygglatho prepares a black-and-white picture consisting of `n * n` cells and chooses a target cell `x`. The rows and columns are numbered from `1` to `n`.

The picture contains `w` black cells. It is guaranteed that `\gcd(n,w)=1`.

Nygglatho first shows the picture and the target cell `x` to Chtholly. Chtholly must choose two cells and swap their colors. The two cells are allowed to be the same. If they are the same, or if they have the same color, the picture does not change. She cannot send Willem any other information.

Swapping colors does not move the target cell.

Nygglatho then secretly transforms the picture. She may perform the following operations any number of times, possibly zero, in any order:

 -  Choose two integers `d_r` and `d_c` (`0<= d_r,d_c \lt n`) and cyclically shifts the picture. Every cell `(r,c)` moves to `<=ft(<=ft(r-1+d_r\right)\bmod n+1,<=ft(c-1+d_c\right)\bmod n+1\right)`;
-  Rotate the picture clockwise by `90^\circ`. One such rotation moves every cell `(r,c)` to `(c,n+1-r)`;
-  Reflect the picture across its vertical axis. Such a reflection moves every cell `(r,c)` to `(r,n+1-c)`;
-  Invert all colors. This changes every black cell into a white cell and every white cell into a black cell.
The target cell `x` undergoes every cyclic shift, rotation, and reflection in exactly the same way as the picture. Color inversions do not move it.

Finally, Nygglatho shows only the resulting picture to Willem. Willem must determine the final position of `x`.

Your program will be run exactly twice on each test. On the first run, it must act as Chtholly. On the second run, it must act as Willem. No information is preserved between the two runs except for the information passed by the jury according to the rules above.

The order of the test cases may be changed between the two runs.

First Run

On the first run, you are Chtholly.

Input

The first line contains the string first, indicating that this is the first run.

After this line, the remaining input has the following format.

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains an integer `n` (`2 <= n <= 800`) — the height and width of the picture.

Each of the next `n` lines contains a string of length `n`. The character `\mathtt{\#}` denotes a black cell, and the character `\mathtt{.}` denotes a white cell.

The next line contains two integers `r_x` and `c_x` (`1 <= r_x,c_x <= n`) — the row and column of the target cell `x`.

Let `w` be the number of black cells in the picture. It is guaranteed that `\gcd(n,w)=1`.

It is guaranteed that the sum of `n^2` over all test cases does not exceed `800^2`.

Output

For each test case, output four integers `r_1`, `c_1`, `r_2`, and `c_2` (`1 <= r_1,c_1,r_2,c_2 <= n`) — the two cells whose colors Chtholly chooses to swap. The two cells are allowed to be the same.

Second Run

On the second run, you are Willem.

Input

The first line contains the string second, indicating that this is the second run.

After this line, the remaining input has the following format.

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The value of `t` is the same as on the first run, although the test cases may appear in a different order.

The first line of each test case contains the integer `n` (`2 <= n <= 800`).

Each of the next `n` lines contains a string of length `n`, describing the resulting picture after Chtholly's swap and Nygglatho's transformations for the corresponding test case from the first run. Again, `\mathtt{\#}` denotes a black cell and `\mathtt{.}` denotes a white cell.

It is guaranteed that the sum of `n^2` over all test cases does not exceed `800^2`.

Output

For each test case, output two integers `r'_x` and `c'_x` (`1 <= r'_x,c'_x <= n`) — the row and column of the target cell after all transformations.

Hacks are disabled in this problem.


## Examples

### Input 1

```text
first
2
5
#....
.#...
.....
.....
.....
3 4
5
.....
####.
.....
#####
.....
1 1
```

### Output 1

```text
1 1 4 1
1 1 1 1
```

### Input 2

```text
second
2
5
.....
####.
.....
#####
.....
5
...#.
.....
.....
..#..
.....
```

### Output 2

```text
1 1
1 4
```

## Note

The first example shows Chtholly's run for two test cases. The second example shows Willem's run for the same two test cases. The outputs shown for Chtholly's run are just one possible set of valid choices.

In the first test case, Chtholly swaps cells `(1,1)` and `(4,1)`. Afterwards, the two black cells are at `(2,2)` and `(4,1)`.

In this example, Nygglatho performs the following transformations.

 -  she cyclically shifts the picture one row down and two columns to the right;
-  she rotates the picture clockwise by `90^\circ` once;
-  she reflects the picture across its vertical axis;
The target moves from `(3,4)` to `(4,1)` after the cyclic shift, then to `(1,2)` after the rotation, and finally to `(1,4)` after the reflection. The two black cells finally arrive at `(3,5)` and `(4,3)`, giving exactly the picture in Willem's run. Willem reports the target position `(1,4)`.

In the second test case, the target is already `(1,1)`, the position of the only black cell. Chtholly chooses `(1,1)` twice, so the picture does not change.

Nygglatho performs no transformation and does not invert the colors. Therefore, Willem sees the black cell at `(1,1)` and reports that position.
