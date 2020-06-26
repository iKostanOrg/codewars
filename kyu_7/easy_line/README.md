## Easy Line

In the drawing below we have a part of the Pascal's triangle, lines are numbered from zero (top).

We want to calculate the sum of the squares of the binomial coefficients on a given line with a function called easyline (or easyLine or easy-line).

Can you write a program which calculate `easyline(n)` where n is the line number?

The function will take `n (with: n>= 0)` as parameter and will return the sum of the squares of the binomial coefficients on line `n`.

### Examples

```text
easyline(0) => 1
easyline(1) => 2
easyline(4) => 70
easyline(50) => 100891344545564193334812497256
```

[Reference](http://mathworld.wolfram.com/BinomialCoefficient.html)

<img src="https://github.com/ikostan/codewars/tree/master/kyu_7/easy_line/eUGaNvIm.jpg" alt="alternative text"><br/>

### Note

In Javascript, Coffeescript, Typescript, C++, PHP, C, R, Nim, Fortran to get around the fact that we have no big integers the function easyLine(n) will in fact return `round(log(easyline(n)))` and not the `easyline(n)` of the other languages.

```text
easyLine(0) => 0
easyLine(1) => 1
easyLine(4) => 70
easyLine(50) => 100891344545564193334812497256
```

### Video tutorials

-   [Binomial Theorem - Why do we need it? - CBSE 11](https://www.youtube.com/watch?v=nYO2DqoZdd4&list=PLmdFyQYShrjf2BlDFvO-kHT2ftf05yxfR&index=1)
-   [Pascal's Triangle and the Binomial Theorem - CBSE 11](https://www.youtube.com/watch?v=LurI8AYY18E)
-   [Binomial Theorem - General Formula - CBSE 11](https://www.youtube.com/watch?v=MDaHBKx1IyE&list=PLmdFyQYShrjf2BlDFvO-kHT2ftf05yxfR&index=2)
-   [Pascal's triangle for binomial expansion | Algebra II | Khan Academy](https://www.youtube.com/watch?v=v9Evg2tBdRk)

[Source](https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python)