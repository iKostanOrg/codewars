# Where my anagrams at

What is an anagram? Well, two words are anagrams of each other if
they both contain the same letters. For example:

```bash
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should
return an array of all the anagrams or an empty array if there are none.
For example:

<!-- markdownlint-disable MD013 -->
```bash
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```
<!-- markdownlint-enable MD013 -->

[Source](https://www.codewars.com/kata/523a86aa4230ebb5420001e1)