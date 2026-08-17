# CF_104555C — Challenging Hike

- Codeforces: [104555C](https://codeforces.com/gym/104555/problem/C)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 870
- Titulo original: C. Challenging Hike
- time limit per test: 0.5 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Finally, the exhausting exams are behind you, and the time has come to relish a well-deserved vacation away from the college hustle. With your bags neatly packed, you set out for an adventure to explore one of the most renowned mountains in your region – a destination you've been dreaming of visiting for a considerable period.

This majestic mountain boasts impressive dimensions and offers a plethora of hiking options. Comprising a total of `N` landmarks, each uniquely identified by a number ranging from `1` to `N`, the mountain presents a captivating network of `N-1` interconnected paths. These pathways ensure that you can effortlessly traverse from any landmark to another, connecting the entire mountain in a seamless web.

Each landmark, denoted by the index `i`, possesses an associated score, aptly named `v_i`. This score reflects the expected number of likes your social media post of that landmark would attract. Brimming with enthusiasm, you've decided to infuse an extra layer of excitement into your hike by embracing the "photos hype challenge". In this challenge, your objective is nothing short of extraordinary: capture and post photos in a manner that guarantees each successive photo garners more likes than its predecessor.

The rules of this challenge dictate your journey to unfold as follows:

 -  You commence your hike from landmark `1`.
-  Progressing along the available paths, you navigate through the landmarks, always moving forward and never backtracking.
-  At each landmark you visit, you are presented with the choice of capturing a photo and posting it on your social media platform.
As your journey unfolds, you're curious about the potential outcomes. Specifically, for every landmark `i`, you seek to determine the maximum number of photos that can be posted if you initiate the hike from landmark `1` and conclude at landmark `i` (although you not necessarily took a photo of landmark `i`). The challenge is to strategically select the landmarks to capture photos, ensuring that each photo outshines its predecessor in terms of expected likes.

Your task is to calculate this maximum number of photos for each landmark. Can you rise to the challenge and uncover the most captivating and likable path through this mountain?

## Input

The first line contains an integer `N` (`1 <= N <= 10^5`), representing the number of landmarks in the mountain. The second line contains `N-1` integers `p_2, p_3, ..., p_N` `(1 <= p_i <= N)`, where `p_i` represents that there is a path between the landmarks `i` and `p_i`. The third line contains `N` integers `v_1, v_2, ..., v_N` `(1 <= v_i <= 10^9)`, where `v_i` represents the expected number of likes a photo of the `i`-th landmark would get.

## Output

Output a single line with `N-1` integers, where the `i`-th integer represents the maximum number of photos you can post if you start the hike on landmark `1` and finish on landmark `(i+1)`.

## Examples

### Input 1

```text
5
1 1 3 3
5 7 7 6 8
```

### Output 1

```text
2 2 2 3
```

### Input 2

```text
5
3 1 3 1
5 4 7 6 5
```

### Output 2

```text
2 2 2 1
```
