# Valid Braces

## Description

Write a function that takes a string of braces, and determines if the order
of the braces is valid. It should return true if the string is valid, and
false if it's invalid.

This Kata is similar to the [Valid Parentheses Kata](https://www.codewars.com/kata/valid-parentheses-1),
but introduces new characters: `brackets []`, and curly `braces {}`.

All input strings will be nonempty, and will only consist of parentheses,
brackets and curly braces: `()[]{}`.

## What is considered Valid?

A string of braces is considered valid if all braces are matched with the
correct brace.

Examples:

```bash
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
```

[Source](https://www.codewars.com/kata/5277c8a221e209d3f6000b56)