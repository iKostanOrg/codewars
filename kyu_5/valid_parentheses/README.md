# Valid Parentheses

Write a function called that takes a string of parentheses, and determines
if the order of the parentheses is valid. The function should return true
if the string is valid, and false if it's invalid.

## Examples

```text
> "()"              =>  true
>
> ")(()))"          =>  false
>
> "("               =>  false
>
> "(())((()())())"  =>  true
```

## Constraints

```text
> 0 <= input.length <= 100
```

Along with opening `(()` and closing `())` parenthesis, input may contain any
valid ASCII characters. Furthermore, the input string may be empty and/or not
contain any parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. `[]`, `{}`, `<>`).

[Source](https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python)
