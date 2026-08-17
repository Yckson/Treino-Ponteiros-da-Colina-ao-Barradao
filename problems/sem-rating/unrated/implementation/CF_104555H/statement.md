# CF_104555H — Honest Worker

- Codeforces: [104555H](https://codeforces.com/gym/104555/problem/H)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 342
- Titulo original: H. Honest Worker
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Rafael lives in an ideal egalitarian society: all jobs offer identical payment rates and you only have to work at a job that you find personally fulfilling. Unfortunately, even such a utopia can't account for the fact that Rafael is not very skilled at anything.

To compensate for this, Rafael turns to contractor work, where potential employers lack the time to realize how unqualified for the job he is. Even then, given his lack of qualifications for these contractor positions, he must expend money on acquiring fake cover letters in order to even get hired.

Rafael has a choice of `N` contractor jobs available to him. The `i`-th job starts at day `\ell_i`, ends at the end of day `r_i` and pays exactly `S` gold coins a day. Rafael is a really bad worker, and cannot work two jobs at the same time; moreover, he can only start job `i` at day `\ell_i` but, once hired, he can choose to quit at the end of any day, keeping the money from the days he worked (including the last one), and being able to start another job from the next day on, but not on the same day. Additionally, Rafael knows that it would cost `c_i` gold coins to buy a fake cover letter for job `i`. Aware of his inabilities and the need for fake cover letters, Rafael always has enough savings to pay for any number of cover letters he might need, even before working any of the `N` jobs.

Given the description of the available jobs, what is the maximum profit that Rafael can attain, factoring in the expenses for the required fake cover letters?

## Input

The first line contains two integers `N` (`1 <= N <= 10^6`) and `S` (`1 <= S <= 10^9`), representing the number of jobs available and what is their daily pay.

Each of the following `N` lines contains three integers: `\ell_i`, `r_i` and `c_i` (`1 <= \ell_i <= r_i <= 10^{9}`, `1 <= c_i <= 10^{9}`), representing the start date, end date, and cost of obtaining a fake cover letter for job `i`, respectively.

## Output

Output a single line with an integer indicating the amount of money Rafael can make after all the jobs are over.


## Examples

### Input 1

```text
3 3
1 5 10
2 10 4
5 15 1
```

### Output 1

```text
37
```

### Input 2

```text
3 5
1 1 3
2 3 4
3 3 1
```

### Output 2

```text
8
```

### Input 3

```text
1 1000
1 1 654
```

### Output 3

```text
346
```

### Input 4

```text
1 5
1 3 20
```

### Output 4

```text
0
```

## Note

Explanation of sample 1:

It is optimal to start the second job, then switch to the third one, for a total of `14 * 3 - 4 - 1 = 37` gold coins.

Explanation of sample 3:

Even though he has to take money from savings to buy the fake cover letter he can still make some profit.

Explanation of sample 4:

Not worth spending money on the fake cover letter for this job.
