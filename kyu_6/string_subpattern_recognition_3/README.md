# String subpattern recognition III

This time you need to operate with shuffled strings to identify
if they are composed repeating a subpattern

Since there is no deterministic way to tell which pattern was
really the original one among all the possible permutations of
a fitting subpattern, return a subpattern with sorted characters,
otherwise return the base string with sorted characters (you might
consider this case as an edge case, with the subpattern being
repeated only once and thus equalling the original input string).

**For example:**
<!-- markdownlint-disable MD013 -->
> has_subpattern("a") == "a"; #no repeated pattern, just one character
>
> has_subpattern("aaaa") == "a" #just one character repeated
>
> has_subpattern("abcd") == "abcd" #base pattern equals the string itself, no repetitions
>
> has_subpattern("babababababababa") == "ab" #remember to return the base string sorted"
>
> has_subpattern("bbabbaaabbaaaabb") == "ab" #same as above, just shuffled
<!-- markdownlint-enable MD013 -->

[Source](https://www.codewars.com/kata/5a4a2973d8e14586c700000a)