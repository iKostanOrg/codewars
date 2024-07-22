# Maximum Multiple

## Task

Given a Divisor and a Bound, Find the largest integer N, Such That,

## Conditions

*   N is divisible by divisor
*   N is less than or equal to bound
*   N is greater than 0.

## Notes

*   The parameters (divisor, bound) passed to the function are only positve values.
*   It's guaranteed that a divisor is Found .

## Input > Output Examples
<!-- markdownlint-disable MD013 -->
```text
> maxMultiple (2,7) ==> return (6)

`(6)` is divisible by `(2)`, `(6)` is less than or equal to bound `(7)`, and `(6)` is > 0.
```

```text
> maxMultiple (10,50)  ==> return (50)

`(50)` is divisible by `(10)`, `(50)` is less than or equal to bound `(50)`, and `(50)` is > `0`.*
```

```text
> maxMultiple (37,200) ==> return (185)

`(185)` is divisible by `(37)`, `(185)` is less than or equal to bound `(200)`, and `(185)` is > `0`.
```
<!-- markdownlint-enable MD013 -->
[Source](https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python)