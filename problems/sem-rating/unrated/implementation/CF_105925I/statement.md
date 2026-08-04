# CF_105925I — Inspecting the Entanglement

- Codeforces: [105925I](https://codeforces.com/gym/105925/problem/I)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 100
- Titulo original: I. Inspecting the Entanglement
- time limit per test: 1 second
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

In the laboratory of the Institute of Quantum Physics, a team of scientists is conducting a new experiment. The idea is to reconstruct the evolution of a set of entangled particles over time. The problem is that the experiment cannot be observed directly.

Therefore, the laboratory has a network of `N` quantum sensors distributed in space. The sensors detect various properties of the particles (spin, polarization, angular momentum, etc.). However, for technical and energy reasons, the same sensor cannot be activated for a very short time (to avoid noise) and cannot remain active for too long (to avoid overheating).

The experiment will last `T` seconds. To avoid wasting energy and to ensure that all information is collected, exactly one of the sensors must be on each second, collecting information, and no sensor should remain on after the end of the experiment.

Each sensor i at time j provides a reliability score `c(i, j)`, reflecting the quality of the measurement at that moment. The team's challenge is to select which sensors to activate throughout the experiment, ensuring that after a sensor is activated, it must remain active for at least `L` seconds and at most `U` seconds. Additionally, a sensor can be used multiple times during the experiment, as long as the time it remains active is respected.

The final reliability of the experiment is equal to the sum of the reliability of the chosen sensors at each second during the test. The team's goal is to select the sensors in such a way as to maximize the reliability of the reconstruction of the quantum state. Since the physicists are very busy studying other quantum matters, they have sent this problem to the teams of the Fase Zero da Maratona SBC de Programação to solve.

## Input

The first line contains two integers `N` (`1 <= N <= 5 * 10^3`) and `T` (`1 <= T <= 100`) representing the number of sensors and the duration of the experiment, respectively.

The next `N` lines each contain `T` integers, where the `i`-th line's `j`-th integer will be `c(i,j)` (`1 <= c(i,j) <= 5 * 10^7`).

The last line contains two integers `L` and `U` (`1 <= L <= U <= T`) representing the minimum and maximum time that each sensor can remain active.

## Output

Output a single line with an integer representing the highest possible reliability. If there is no solution for the given constraints, print `-1`.

## Examples

### Input 1

```text
3 5
2 3 2 1 2
1 1 5 1 2
1 2 2 1 5
1 5
```

### Output 1

```text
16
```

### Input 2

```text
3 5
2 3 2 1 2
1 1 5 1 2
1 2 2 1 5
2 3
```

### Output 2

```text
13
```

### Input 3

```text
3 5
2 3 2 1 2
1 1 5 1 2
1 2 2 1 5
2 2
```

### Output 3

```text
-1
```
