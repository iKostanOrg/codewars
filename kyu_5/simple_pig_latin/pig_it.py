"""
Solution for -> Simple Pig Latin.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import List


def pig_it(text: str) -> str:
    """
    pig_it function.

    Move the first letter of each word to the end of it,
    then add "ay" to the end of the word. Leave
    punctuation marks untouched.
    :param text: str
    :return: str
    """
    result: List[str] = []
    for word in text.split(' '):
        word_processor(word, result)

    return ' '.join(result)


def word_processor(word: str, result: list) -> None:
    """
    word_processor function.

    Processing a single word for the requested pattern.
    :param word: str
    :param result: list
    :return: None
    """
    if len(word) > 1:
        result.append(f'{word[1:] + word[0]}ay')
    elif len(word) == 1 and word.isalpha():
        result.append(f'{word}ay')
    else:
        result.append(word)
