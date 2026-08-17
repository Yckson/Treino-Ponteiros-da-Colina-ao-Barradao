# CF_104555D — Detour

- Codeforces: [104555D](https://codeforces.com/gym/104555/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 268
- Titulo original: D. Detour
- time limit per test: 5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

In the city of Nlogonia, the mayor is taking action on his promises to revitalize the city's road infrastructure. However, the road renewal process renders certain roads temporarily impassable, requiring the establishment of detours to ensure uninterrupted traffic flow.

Each road segment connects two crossroads in the city, has a positive length and can be traversed in both directions. A detour is a designated alternative route that temporarily replaces a road segment under renewal. Specifically, when the road connecting crossroads `U` and `V` is impassable, the detour must be a sequence of roads that originates at `U` and terminates at `V`, while intentionally avoiding the direct road between `U` and `V`. The goal is to find the shortest detour for each road segment to minimize disruptions while road improvements take place.

As the Intern at the Center for Pavement and Cars, your responsibility is to support the mayor's initiative by calculating the length of the shortest detour for each road segment within the city.

## Input

The first line contains two integers, `N` and `M` (`1 <= N <= 300`), representing the number of crossroads in the city and the number of road segments. Each of the following `M` lines contains three integers, `U`, `V`, and `L` `(1 <= U <= N`, `1 <= V <= N`, `U != V`, `1 <= L <= 10^6`), representing a two-way road segment of length `L` that connects crossroads `U` and `V`. No road segment is duplicated.

## Output

 Output `M` lines, each line containing an integer. The integer on the `i`-th line represents the shortest detour length for the `i`-th road segment or -1 if there is no possible detour. The answer for each road segment should be given in the same order as road segments are described in the input.

## Examples

### Input 1

```text
4 5
1 2 4
1 3 8
2 3 4
4 1 2
3 4 3
```

### Output 1

```text
9
5
9
11
10
```

### Input 2

```text
2 1
1 2 1
```

### Output 2

```text
-1
```
