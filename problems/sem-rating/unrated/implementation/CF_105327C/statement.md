# CF_105327C — Couple of BipBop

- Codeforces: [105327C](https://codeforces.com/gym/105327/problem/C)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 293
- Titulo original: C. Couple of BipBop
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

It's time for Bob and Charlie to go on a new couple-hyperfocus: BipBop trends. This social network specialized in short videos is going viral more than ever before. As a consequence, couples now measure how much they love each other in terms of how well they can dance together. In theory, the BipBop dancing style is simple and can be used to perform pretty much every song existent. Usually, it consists in a sequence of moves, one for each verse, represented by an integer number, as the moves are kinda generic, really.

Always late, the couple just got to a party, the song is already playing, but they still want to impress and show that they can dance BipBop even without knowing in what verse the song is currently at. Then, each of them starts dancing in a random verse and keep following the coreography until one of them reaches the end of the song or when they unmatch a move (they execute different moves).

There is no popular song that Bob and Charlie don't know how to dance, so given a song represented as a sequence of movements, one for each verse, calculate the expected number of verses they will be dancing in sync, if each of them initially thinks that the song is playing on a random verse with uniform probability.

## Input

The first line of the input contains an integer `N` (`1 <= N <= 10^5`), the number of verses in the song.

The second line contains `N` integers, `V_1, V_2, ..., V_N` (`1 <= V_i <= N`), corresponding to the movement associated with each of the verses in the sequence.

## Output

Output the expected number of verses (moves) the couple will dance in sync, if each one of them chose a verse uniformly at random to start the dance. Output the answer as a irreducible fraction `P/Q`, such that `\gcd(P, Q) = 1`. It can be proven that it is always possible to express the answer in this way.


## Examples

### Input 1

```text
2
1 1
```

### Output 1

```text
5/4
```

### Input 2

```text
4
1 1 1 1
```

### Output 2

```text
15/8
```

### Input 3

```text
7
1 2 1 3 1 2 1
```

### Output 3

```text
48/49
```

## Note

Explanation for sample 1: Note that there are 4 equally likely ways for the choreography to occur: both Bob and Charlie can start on the first or second verse, with probability `1/2` that each will start on each of the verses and therefore probability `1/4` for each of the combinations. If both start on the first verse, they will dance 2 verses in sync. In the other three possibilities, they will dance only one verse in sync. Thus, we have on average, `2* 1/4 + 1* 1/4 + 1* 1/4 + 1* 1/4 = 5/4` verses in sync.
