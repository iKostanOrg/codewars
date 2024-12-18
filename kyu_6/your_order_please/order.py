"""
Solution for -> Your order, please.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def order(sentence: str) -> str:
    """
    Sort a given string by following rules:

        1. Each word in the string will contain a single number.
           This number is the position the word should have in the result.

        2. Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

        3. If the input string is empty, return an empty string. The words in the
           input String will only contain valid consecutive numbers.

    :param sentence: Each word in the string will contain a single number
    :return: sorted string
    """
    results: list = []
    words: list = sentence.split()
    for i in range(1, 10):
        for word in words:
            if str(i) in word:
                results.append(word)
                break
    return ' '.join(results)
