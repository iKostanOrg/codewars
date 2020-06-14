#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def encrypt_this(text: str) -> str:
    """
    Encrypts each word in the message using the following rules:
     * The first letter needs to be converted to its ASCII code.
     * The second letter needs to be switched with the last letter

    Keepin' it simple: There are no special characters in input.

    :param text: a string containing space separated words
    :return: secret messages which can be deciphered by the "Decipher this!" kata
    """

    if not text:
        return ""

    results = list()
    for word in text.split(' '):
        if len(word) == 1:
            results.append("{}".format(ord(word[0])))
        elif len(word) == 2:
            results.append("{}{}".format(ord(word[0]), word[-1]))
        else:
            results.append("{}{}{}{}".format(
                ord(word[0]), word[-1], word[2:-1], word[1]))

    return ' '.join(results)
