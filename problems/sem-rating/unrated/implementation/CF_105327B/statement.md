# CF_105327B — Bacon Number

- Codeforces: [105327B](https://codeforces.com/gym/105327/problem/B)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 560
- Titulo original: B. Bacon Number
- time limit per test: 3 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Carlinhos loves movies, and recently he has been fascinated by the Bacon Number, which is defined as follows.

  -  The Bacon number of the actor Kevin Bacon is equal to `0`;
-  If the smallest Bacon number of an actor with whom X has appeared in the same movie is `b`, the bacon number of the actor X is `b+1`.
That is, the Bacon number measures the shortest path between any actor and the actor Kevin Bacon, in which two actors are connected if they appeared together in the same movie.

Carlinhos is interested in a more general problem: given two actors, how to connect them through intermediate movies and actors? Given `N` movies, and, for each movie, which of the existing `M` actors acted in it. Carlinhos wants to answer `Q` queries: in the `i`-th of them, we want to compute some way to connect actor `x_i` with actor `y_i`. We must find some sequence `x_i = a_1, f_1, a_2, f_2, ..., f_{k-1}, a_k = y_i`, where `1 <= a_j <= M` are actors and `1 <= f_j <= N` are movies, and actor `a_j` acted in movies `f_{j-1}` and `f_j`, or indicate that no such sequence exists.

## Input

In the first line of the input, two integers `N` `(1 <= N <= 100)` and `M` `(1 <= M <= 10^6)` are given, the number of movies and the number of actors.

`N` lines follow. In the `i`-th line, the first integer `n_i` `(1 <= n_i <= M)` denotes the number of actors in movie `i`. Next, `n_i` numbers in ascending order separated by spaces: the indices, from `1` to `M`, of the actors who acted in movie `i`.

The next line, contains an integer `Q` `(1 <= Q <= 10^4)`: the number of queries.

The next `Q` lines describe the queries. In the `i`-th of them, read two numbers `x_i, y_i` `(1 <= x_i != y_i <= M)`, the actors we want to connect. It is guaranteed that the total number of actors in the movies is at most `10^6`. That is, `\sum_i n_i <= 10^6`.

## Output

For each of the queries, if there is no sequence, print a line with `-1`. Otherwise, print two lines. In the first line, print the number of actors `k_i` `(2 <= k_i <= 10^6)` in some way to connect `x_i` and `y_i`. In the second, print the sequence as described, with `k_i` actors and `k_i - 1` movies, alternating. If there is more than one way to connect the actors, print any of them.

## Examples

### Input

```text
4 6
3 1 2 5
3 1 3 5
2 2 4
1 6
4
1 5
1 4
3 4
1 6
```

### Output

```text
2
1 1 5
3
1 1 2 3 4
4
3 2 5 1 2 3 4
-1
```
