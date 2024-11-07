# String subpattern recognition II

You will need to return a boolean value if the base string can
be expressed as the repetition of one subpattern.

This time there are two small changes:

*   if a subpattern has been used, it will be repeated at least
* twice, meaning the subpattern has to be shorter than the original string;
*   the strings you will be given might or might not be created
* repeating a given subpattern, then shuffling the result.

**For example:**
<!-- markdownlint-disable MD013 -->
> has_subpattern("a") == False #no repeated shorter sub-pattern, just one character
>
> has_subpattern("aaaa") == True #just one character repeated
>
> has_subpattern("abcd") == False #no repetitions
>
> has_subpattern("babababababababa") == True #repeated "ba"
>
> has_subpattern("bbabbaaabbaaaabb") == True #same as above, just shuffled
<!-- markdownlint-enable MD013 -->

Strings will never be empty and can be composed of any character
(just consider upper- and lowercase letters as different entities) and
can be pretty long (keep an eye on performances!).

[Source](https://www.codewars.com/kata/5a4a391ad8e145cdee0000c4)