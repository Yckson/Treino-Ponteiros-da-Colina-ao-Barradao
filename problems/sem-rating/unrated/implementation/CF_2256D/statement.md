# CF_2256D — A Ribbon for Tomorrow

- Codeforces: [2256D](https://codeforces.com/contest/2256/problem/D)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 0
- Titulo original: D. A Ribbon for Tomorrow
- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

Nephren has never been fond of long farewells. Before Chtholly leaves for her next mission, she says nothing and begins preparing a small ribbon for her instead.

She places `n` glass beads in a row on the table before threading them onto the ribbon. Each bead is either white or black. A binary`^{\text{∗}}` string `s` represents their colors: the character `\mathtt{0}` represents a white bead, and the character `\mathtt{1}` represents a black bead.

To make the arrangement less ordinary, Nephren turns it into a small game. She can perform the following operation any number of times (possibly zero):

 -  Choose two indices `l` and `r` (`1 <= l <= r <= n`) such that `s_l=s_r` in the current string, and reverse`^{\text{†}}` the substring `s_l s_{l+1}... s_r`.
For example, if `s=\mathtt{00110}`, Nephren may choose `l=1` and `r=5`, since `s_1=s_5=\mathtt{0}`. After the operation, the string becomes `\mathtt{01100}`.

Determine the number of different binary strings that can be obtained from `s`. Since this number may be large, output it modulo `998 244 353`.

`^{\text{∗}}`A binary string is a string where each character is either `\mathtt 0` or `\mathtt 1`.

`^{\text{†}}`To reverse a substring `s_l s_{l+1}... s_r` means to replace it with `s_r s_{r-1}... s_l`.

## Input

Each test contains multiple test cases. The first line contains the number of test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains one integer `n` (`1 <= n <= 10^6`) — the number of beads.

The second line contains a binary string `s` of length `n`, describing the colors of the beads.

It is guaranteed that the sum of `n` over all test cases does not exceed `10^6`.

## Output

For each test case, output a single integer — the number of different binary strings that can be obtained from `s`, modulo `998 244 353`.


## Examples

### Input

```text
4
5
00110
6
001010
5
01010
6
111111
```

### Output

```text
2
3
1
1
```

## Note

In the first test case, exactly the following two strings can be obtained:

 -  `\mathtt{00110}`;
-  `\mathtt{01100}`.
For example, reversing the entire string `\mathtt{00110}` produces `\mathtt{01100}`.

In the second test case, exactly the following three strings can be obtained:

 -  `\mathtt{001010}`;
-  `\mathtt{010010}`;
-  `\mathtt{010100}`.
For example, `\mathtt{010010}` can be obtained by reversing the first four characters of `\mathtt{001010}`, and `\mathtt{010100}` can be obtained by reversing the entire string `\mathtt{001010}`.

In the third test case, every substring whose endpoints contain the same character is a palindrome. Therefore, reversing any valid substring does not change the string, and only `\mathtt{01010}` can be obtained.

In the fourth test case, we can only get `\mathtt{111111}`.
