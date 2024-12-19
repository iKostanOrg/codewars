"""
Solution for -> Encrypt this!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def encrypt_this(text: str) -> str:
    """
    Encrypt this.

    Encrypts each word in the message using the following rules:
     * The first letter needs to be converted to its ASCII code.
     * The second letter needs to be switched with the last letter

    Keepin' it simple: There are no special characters in input.

    :param text: a string containing space separated words
    :return: messages which can be deciphered by the "Decipher this!"
    """
    if not text:
        return ""

    results: list = []
    for word in text.split(' '):
        if len(word) == 1:
            # Python ord() Function:
            # return the integer that represents the character
            results.append(f"{ord(word[0])}")
        elif len(word) == 2:
            results.append(f"{ord(word[0])}{word[-1]}")
        else:
            results.append(f"{ord(word[0])}"
                           f"{word[-1]}"
                           f"{word[2:-1]}"
                           f"{word[1]}")

    return ' '.join(results)
