# ROTATE THE LETTERS OF EACH ELEMENT

## Task

Create a function that given a sequence of strings, groups the
elements that can be obtained by rotating others, ignoring upper
or lower cases.

In the event that an element appears more than once in the input
sequence, only one of them will be taken into account for the result,
discarding the rest.

### Input

Sequence of strings. Valid characters for those strings are uppercase
and lowercase characters from the alphabet and whitespaces.

### Output

Sequence of elements. Each element is the group of inputs that can
be obtained by rotating the strings.

Sort the elements of each group alphabetically.

Sort the groups descendingly by size and in the case of a tie, by the
first element of the group alphabetically.

### Examples
<!-- markdownlint-disable MD013 -->
```text
['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'] --> [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']]

['Rome', 'Rome', 'Rome', 'Donlon', 'London'] --> [['Donlon', 'London'], ['Rome']]

[] --> []
```
<!-- markdownlint-enable MD013 -->

[Source](https://www.codewars.com/kata/5e98712b7de14f0026ef1cc1)