# CF_106073J — João João

- Codeforces: [106073J](https://codeforces.com/gym/106073/problem/J)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 2331
- Titulo original: J. João João
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

In 2025, the person responsible for coordinating the team that creates the OBI – Online Battle of Influencers – exam is Professor João João, who, in addition to being a professor, is a famous and influential influencer.

So far, the team has created 10 tasks, and each task has been categorized into one of four difficulty levels: 1, 2, 3, and 4.

Professor João João wants to know how many more tasks need to be created so that it is possible to assemble an exam with exactly four tasks, each at a different difficulty level.

Given the list of difficulty levels of the tasks already created, can you help Professor João João determine how many tasks still need to be created?

## Input

The input consists of a single line containing 10 integers `D_1, ..., D_{10}`, where `D_i` denotes the difficulty level of task `i` (`1 <= D_i <= 4`, for `1 <= i <= 10`).

## Output

Your program should print a single line to the output, containing a single integer: the minimum number of tasks that need to be created so that it is possible to assemble an exam with four tasks, each at a different difficulty level.


## Examples

### Input 1

```text
1 3 4 1 3 4 1 3 4 1
```

### Output 1

```text
1
```

### Input 2

```text
4 1 1 4 3 1 2 1 2 2
```

### Output 2

```text
0
```

## Note

Explanation of sample 1:

Tasks with difficulty levels 1, 3, and 4 have already been created. Only one task of difficulty level 2 is missing, so the answer is 1.

Explanation of sample 2:

Tasks with difficulty levels 1, 2, 3, and 4 have already been created. Since no difficulty levels are missing, the answer is 0.
