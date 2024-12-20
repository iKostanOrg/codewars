"""
Solution for -> Pull your words together, man!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def sentencify(words: list) -> str:
    """
    'Sentencify' function.

    The function should:

    1. Capitalise the first letter of the first word.
    2. Add a period (.) to the end of the sentence.
    3. Join the words into a complete string, with spaces.
    4. Do no other manipulation on the words.
    :param words: list
    :return: str
    """
    return words[0][0].upper() + ' '.join(words)[1:] + '.'
