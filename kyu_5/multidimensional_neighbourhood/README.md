# Multidimensional Neighbourhood

I advise you to do some of the previous katas from the: [Neighbourhood collection.](https://www.codewars.com/collections/5b2f4db591c746349d0000ce)

This is the next step. We are going multidimensional. You should build a function
that return the neighbourhood of a cell within a matrix with the given distance
and type. AND it should work for any dimension.

## Input
<!-- markdownlint-disable MD013 -->
```text
* type "moore" or "von_neumann"
* matrix a N-dimensional matrix. N >= 0 (the matrix is always rectangular; could be a list or a tuple)
* coordinates of the cell. It is a N-length tuple. Order of the indices: The first index should be applied for the outer/first matrix layer. The last index for the most inner/last layer. coordinates = (m, n, k) should be apllied like mat[m][n][k]
* distance
```
<!-- markdownlint-enable MD013 -->

## Task

construct get_neighbourhood(n_type, matrix, coordinates, distance)

## Output

he N dimension neighbours of the cell

### Performance

Your code should be performant.

*   There will be one Tests with a very highdimensional matrix
*   There will be 300 Tests with 9 <= distance <= 12
*   There will be 1000 Tests with N == 4, Dimension size == 5
*   There will be 400 Tests with N == 8, Dimension size == 3

**Note:** you should return an empty array if any of these conditions is true:

*   Index is outside the matrix (python: negative indexes are outside the
    matrix too)
*   Matrix is empty
*   Distance equals 0

[Source](https://www.codewars.com/kata/5b47ba689c9a7591e70001a3/train/python)