# Find the safest places in town

[Laura Bassi](https://en.wikipedia.org/wiki/Laura_Bassi) was the first female professor at a European university. Despite her immense intellect, she was not always allowed to lecture publicly.

One day a professor with very strong beliefs against women in academia sent some `agents` to find Bassi and end her career.

Help her escape by telling her the safest places in town!

## Task

Implement the function `advice(agents, n)` where

-   agents is an array of agent coordinates.
-   `n` defines the size of the city that Bassi needs to hide in, in other words the side length of the square grid.

The function should return a list of coordinates that are the furthest away (by [Manhattan distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html)) from all agents.

As an example, say you have a 6x6 map, and agents at locations
```text
[(0, 0), (1, 5), (5, 1)]
```

The distances to the nearest agent look like this.

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/ikostan/codewars/blob/master/img/safest.png" hspace="5">
</div>

The safest spaces are the ones with distance 4, marked in bright red. So the function should return
```text
[(2, 2), (3, 3), (4, 4), (5, 5)]
```
in any order.

Edge cases:

- If there is an agent on every grid cell, there is no safe space, so return an empty list.
- If there are no agents, then every cell is a safe spaces, so return all coordinates.
- If n is 0, return an empty list.
- If agent coordinates are outside of the map, they are simply not considered.
- There are no duplicate agents on the same square.

## Performance

There are `200` random tests with `n <= 50`. Inefficient solutions might time out.

This kata is inspired by [ThoughtWorks' coding challenge.](https://github.com/Fun-Coding-Challenges/ada-lovelace-coding-challenge)

[Source](https://www.codewars.com/kata/5dd82b7cd3d6c100109cb4ed/train/python)