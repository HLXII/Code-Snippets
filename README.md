# Code-Snippets

Repository for a bunch of random code snippets that I wrote. None of them particularly useful.

## Theoretically Complete

### GridMovement

Assume you are on an infinite grid of squares. Given a set number of random moves (either up, down, left, or right), what is the probability of landing on any square?

Given an even number of moves, any square with an odd coordinate sum will be impossible to land on, which leads to a checker pattern of squares.

The outcome (found through brute force) seems to be dependent on factorials and combinations, however I was too lazy to come up with the formula.

### FractionalKnapsack

This covers the Fractional Knapsack problem. This is a greedy algorithm that usually runs in O(nlog(n)), however there is a way to find the solution in O(n) time.

## Incomplete

### Forest

A little journal of me trying to figure out how to generate all possible forests given a number of vertices in a graph. This was supposed to turn into some way of applying a genetic algorithm on graphs by somehow keeping sections of topologies between graphs. I think there's something already out there (called NEAT or something), however I wanted to see if I could come up with something myself.

## Ideas

### Max Cost Choice with Changing Marginal Costs

There is a phone game called Magikarp Go!, where you train magikarps to jump higher. Don't judge me on what I do in my free time. The main point is, you can upgrade training tasks with money, so a training task will 'train' the magikarp better.

However, the cost of upgrading tasks increases with each upgrade, and the increase in training is also variable. If there is a certain starting amount of money, what set of upgrades would you choose to obtain the maximum average training.

Consider this chart:
| Training | Level | Value | Cost |
|----------|-------|-------|------|
| A        | 1     | 1     | 1    |
| A        | 2     | 3     | 2    |
| A        | 3     | 5     | 4    |
| B        | 1     | 2     | 2    |
| B        | 2     | 5     | 2    |
| B        | 3     | 11    | 10   |

If you are given n dollars, what would be the optimal allocation of your money to maximize your total value? For instance in this chart, given only 1 dollar, you would choose A at level 1. For 14 dollars, you would choose B at level 3, rather than A level 2 and B level 2. since 14 > 3+5.

This seems like something to be solved with dynamic programming, but I've been too busy to figure out how to solve it.

In addition, if you have already invested some money in training levels and you have n dollars, what would be the optimal solution then. I feel like this is the same question though.









