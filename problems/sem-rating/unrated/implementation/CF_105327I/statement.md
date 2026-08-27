# CF_105327I — Ingredients that may Harm You

- Codeforces: [105327I](https://codeforces.com/gym/105327/problem/I)
- Score/rating: unrated
- Categoria local: `implementation`
- Tags Codeforces: sem tags
- Resolvidos no Codeforces: 708
- Titulo original: I. Ingredients that may Harm You
- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

---

In Nlogonia, foods are identified by numbers. Prime numbers identify the basic ingredients, and the number that identifies each food is given by the product of the numbers associated with the ingredients that compose it, respecting multiplicities. For example, a food with the number `12` contains two units of the ingredient `2`, and one unit of the ingredient `3`, since `12 = 2 * 2 * 3`.

You live in Nlogonia, and you own a self-service restaurant, that is, where people assemble their own dishes with the food available in the restaurant. You are expecting to serve `Q` people in your restaurant today.

Each person has a set of allergies, which are identified by an integer in the same way: each prime number that divides the person's number indicates that he or she is allergic to the ingredient associated with that prime number.

Given the numbers associated with each food item in your restaurant, calculate, for each of the `Q` people, how many different dishes she can assemble so that there is no ingredient in the dish to which she is allergic.

## Input

The first line of the input contains an integer `N` `(1 <= N <= 10^5)`, the number of foods in your restaurant. The next line contains the numbers associated with each food `V_i` `(1 <= V_i <= 10^6)`. The next line contains an integer `Q` `(1 <= Q <= 10^5)`, the number of people who will eat at your restaurant. `Q` lines follow; the `i`-th of them contains a number `X_i` `(1 <= X_i <= 10^6)`, the number representing the allergies of person `i`.

## Output

For each of the `Q` people, print a number: the number of dishes that can be assembled with the restaurant's ingredients, so that none of the ingredients to which the person is allergic are present. Since the answer may be very large, print the remainder when dividing it by `10^9+7`.


## Examples

### Input

```text
6
1 2 3 4 5 6
4
1
2
4
6
```

### Output

```text
64
8
8
4
```

## Note

Explanation for sample 1: The first person has no allergies, so all `64` possible dishes are valid for her. On the other hand, the last person is allergic to foods that contain the ingredients associated with the prime numbers `2` and `3`. Therefore, only 4 dishes are possible for her: the empty plate (without any food), the plate with only food `1` (which has no ingredients), the plate with food `5`, and the plate with foods `1` and `5`.
