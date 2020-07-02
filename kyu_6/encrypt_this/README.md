# Encrypt this

## Description

You want to create secret messages which can be deciphered by the [Decipher this!](https://www.codewars.com/kata/decipher-this) kata. Here are the conditions:

1.  Your message is a string containing space separated words.
2.  You need to encrypt each word in the message using the following rules:
    *   The first letter needs to be converted to its ASCII code.
    *   The second letter needs to be switched with the last letter
    
3.  Keepin' it simple: There are no special characters in input.

## Examples

```text
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```

[Source](https://www.codewars.com/kata/5848565e273af816fb000449/train/python)