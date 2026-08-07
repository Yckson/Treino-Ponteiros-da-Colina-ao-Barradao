# CF_106073A — A healthy menu

- Codeforces: [106073A](https://codeforces.com/gym/106073/problem/A)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 2224
- Titulo original: A. A healthy menu
- time limit per test: 2 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

At the Institute of Creative Programming Competitions (ICPC), all students love fruits! Knowing this, management decided to conduct a large survey about food preferences to help in preparing the annual menu. To make the survey more professional, they hired the company SBC Research Solutions™, an acronym for "Saladas Bem Científicas", although some say the name is a tribute to a well-known computer science society...

SBC received the following mission: the school has `M` classes and offers `N` different types of fruit. In each class, for each fruit, the number of students who like that fruit was reported.

However, since SBC did not have access to individual student data, nor do they know how many students are in each class, they now need your help! Based only on the survey results (how many students like each fruit in each class), determine the smallest possible number of students the school can have, knowing that the following constraints are satisfied:

 -  each class has at least one student;
-  each student belongs to a single class;
-  each student likes at least one fruit;
-  the same student can like several fruits.

## Input

The first line of input contains two integers `N` and `M` (`1 <= N, M <= 1000`), the number of fruits and the number of classes, respectively. Each of the following `N` lines contains `M` integers `G_{i,j}`, indicating how many students in class `j` like fruit `i` (`0 <= G_{i,j} <= 10^6` for `1 <= i <= N` and `1 <= j <= M`).

## Output

Your program should print a single line, containing a single integer, the smallest possible number of students in the school, considering the given constraints.

## Examples

### Input 1

```text
3 3
20 15 14
12 20 12
18 5 10
```

### Output 1

```text
54
```

### Input 2

```text
2 3
5 2 4
4 3 6
```

### Output 2

```text
14
```
