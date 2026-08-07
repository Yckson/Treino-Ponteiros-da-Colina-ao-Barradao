# CF_106073E — Expansion of the road network

- Codeforces: [106073E](https://codeforces.com/gym/106073/problem/E)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 17
- Titulo original: E. Expansion of the road network
- time limit per test: 1.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Legend has it that, long ago, the Service of Braveway Connections (SBC) administered a network of bidirectional roads that connected various cities. At that time, the layout was extremely simple: between any two cities there was exactly one path.

With population growth and increased transportation of goods, the Institute of Connected and Planned Cities (ICPC) took control and decided to modernize the network. To avoid internal traffic in intermediate cities and speed up travel, new direct roads were built between certain pairs of cities. A new road was created between two cities `A` and `B` whenever, in the original layout, the path between them passed through exactly one intermediate city.

Today, we only have the current map of the network, and ICPC wants to find out whether it could indeed have arisen from this process.

Your task is to analyze the current map and determine whether the legend could be true. If possible, you should also reconstruct and print a possible original layout of the network.

## Input

The first line contains two integers `N` and `M` (`3 <= N <= 10^5`, `2 <= M <= 4 * 10^5`), representing, respectively, the number of cities and the number of roads in the current map.

Each of the following `M` lines contains two integers `u_i` and `v_i` (`1 <= u_i, v_i <= N`, `u_i != v_i`), indicating that there is a bidirectional road between cities `u_i` and `v_i`. In the current map, it is guaranteed that there is a path between any pair of cities and that there is at most one road between any pair of cities.

## Output

If the current map could have arisen from the process described in the legend, the output should contain `N-1` lines. Each line should contain two integers `a_i` and `b_i` (`1 <= a_i, b_i <= N`, `a_i != b_i`), indicating that there was a direct road between cities `a_i` and `b_i` in the original layout.

Otherwise, the output should contain only one line with a single character '*' (asterisk).

If there is more than one possible original layout, print any of them.


## Examples

### Input 1

```text
3 3
1 2
3 2
1 3
```

### Output 1

```text
1 2
1 3
```

### Input 2

```text
3 2
1 2
2 3
```

### Output 2

```text
*
```

## Note

Explanation of sample 1:

One possible original route is `1-2-3`. In this case, a single road was added by the process described in the legend, the road `1-3`, which passes through the intermediate city `2`.

Other possible original routes are `1-3-2` and `2-1-3`.
