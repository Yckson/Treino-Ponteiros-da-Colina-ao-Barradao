# CF_103960J — Playing 23

- Codeforces: [103960J](https://codeforces.com/gym/103960/problem/J)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 1548
- Titulo original: J. Playing 23
- time limit per test: 0.25 seconds
- memory limit per test: 1024 megabytes
- input: standard input
- output: standard output

---

Twenty-three is a simple card game played by kids. Like its name suggests, it is a variation of Blackjack, which is the most widely played game in casinos and gaming sites.

The game uses a deck of 52 cards, with four suits, each suit with 13 cards (ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen and king). Card suits are not relevant. The picture cards (jack, queen and king) are worth ten points, cards with numbers are worth their number in points (for example, the 4 card is worth four points) and the ace is worth one point.

The player who has the most points wins, provided it does not exceed 23. If a player has a number of points greater than 23 we say the player busts.

The game rules are simple: at each game, initially the deck is shuffled, the cards are placed in a stack and each player receives two cards from the stack. All cards are dealt face up (all players see all players' cards). The next step, called round, is repeated as long as there are active players: a card is taken from the stack and set on the table face up. This card, called common card, counts to all players. If a player busts, he leaves the game. The winner is the player that in a given round has a total of 23 points (considering their two starting cards plus the common cards), or if the player is the only active player at the end of the round. Note that there can be more than one winner (whose cards add up to 23) and that there may be no winner in a match.

John and Mary are playing twenty-three. The two are the only players in the game, neither of them busted and neither of them has 23 points. Furthermore, the players score is such that the next common card may cause the game to end.

Given John and Mary initial cards and the common cards, determine the lowest possible value of a card that should be taken from the stack in the next round for Mary to win the game.

## Input

The first line of input contains a single integer `N` (`1 <= N <= 8`), the number of rounds already played. Each card is described by an integer `I` (`1 <= I <= 13`). Note that the picture cards (jack, queen and king) are represented in the input by the values 11, 12 and 13 which is not how many points they are worth. The second line contains two integers, describing the two initial cards for John. The third line contains two integers, describing the two initial cards for Mary. The fourth and last line contains `N` integers, describing the common cards, in the order they were taken from the stack.

## Output

Your program should output a single line, containing a single integer, the value of the lowest card that must be taken from the stack in the next round for Mary to win the game, or -1 if Mary cannot win the match in that next round.

## Examples

### Input 1

```text
1
10 5
9 10
1
```

### Output 1

```text
3
```

### Input 2

```text
1
10 5
8 7
2
```

### Output 2

```text
6
```

### Input 3

```text
1
9 10
10 5
1
```

### Output 3

```text
4
```

### Input 4

```text
2
8 4
4 1
4 4
```

### Output 4

```text
5
```

### Input 5

```text
8
2 1
1 1
1 2 2 2 3 3 3 3
```

### Output 5

```text
-1
```
