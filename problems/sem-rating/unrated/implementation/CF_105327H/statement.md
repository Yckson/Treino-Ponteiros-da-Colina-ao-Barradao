# CF_105327H — Harmonics with Interference

- Codeforces: [105327H](https://codeforces.com/gym/105327/problem/H)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 815
- Titulo original: H. Harmonics with Interference
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

The transmission of messages by electromagnetic means presents several challenges, such as interference from other natural or artificial signals that can corrupt a transmission.

A common strategy is to send additional information that allows a received message to be validated. Some more robust protocols even allow for the correction of some errors in the sent message.

Arthur and Bruna are testing a new transmission protocol on a device they have developed. A message `M`, which is a sequence of bits, is sent from Arthur to Bruna, along with a control sequence `N`, also represented as a sequence of bits. By composing the message `M` and choosing the bits from `N`, Arthur ensures that the integer encoded by `M` is divisible by the integer represented by `N`.

For each bit received by Bruna, if the bit was transmitted without problems, the value 0 or 1 will be stored in the receiving device. If there was any interference, the symbol * is stored in place of the bit. The result of the transmission will be stored in the pair `(M', N')`.

After the communication, if the message was sent successfully, Bruna can decode the original message `M` (since `M=M'`). If there was a problem, due to the way the protocol works, it may still be possible to decode the message. If many bits were lost, Bruna simply discards the message. But for transmissions where at most 16 bits of the original pair `(M,N)` were lost, Bruna would like to try to recover the message, avoiding retransmissions. She needs your help to recover one of the possible messages encoded by the received pair `(M',N')`.

For example, suppose Bruna received `M'`=111* and `N'`=1*. Two transmissions could have been made:

 -  `M`=1111 with `N`=11. In this case, the numbers `15` and `3` are represented by `M` and `N`, respectively.
-  `M`=1110 with `N`=10. In this case, the numbers `14` and `2` are represented by `M` and `N`, respectively.
Your task is: given the representations of the information received, find a message `M` that could have been sent by Arthur. If more than one message exists, you can print any message that could have been transmitted by Arthur.

## Input

The first line of input will contain a sequence of characters representing `M'`, with `1 <= |M'| <= 500`. The second line of input will contain a sequence of characters representing `N'`, with `1 <= |N'| <= 16`. All characters in `N'` and `M'` will be either 0, 1, or *. In total, there will never be more than 16 * characters in the input. It is guaranteed that `N'` always contains at least one bit 1.

## Output

A single line should be printed, containing a message `M`, compatible with the information received by Bruna.


## Examples

### Input 1

```text
111*
1*
```

### Output 1

```text
1110
```

### Input 2

```text
101**
11
```

### Output 2

```text
10101
```

## Note

Explanation for sample 1: This case corresponds to the example given in the statement.

Explanation for sample 2: In this case, the different ways of choosing the unknown bits would result in messages corresponding to the integers 20, 21, 22 and 23, and only 21, represented by 10101, is divisible by 3.
