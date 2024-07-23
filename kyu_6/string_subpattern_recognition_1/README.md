# String subpattern recognition I

In this kata you need to build a function to return either `true/True`
or `false/False` if a string can be seen as the repetition of a
simpler/shorter subpattern or not.

## For example
<!-- markdownlint-disable MD013 -->
> has_subpattern("a") == False #no repeated pattern
>
> has_subpattern("aaaa") == True #created repeating "a"
>
> has_subpattern("abcd") == False #no repeated pattern
>
> has_subpattern("abababab") == True #created repeating "ab"
>
> has_subpattern("ababababa") == False #cannot be entirely reproduced repeating a pattern
<!-- markdownlint-enable MD013 -->

Strings will never be empty and can be composed of any character
(just consider upper- and lowercase letters as different entities)
and can be pretty long (keep an eye on performances!).

[Source](https://www.codewars.com/kata/5a49f074b3bfa89b4c00002b/train/python)