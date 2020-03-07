#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from typing import List


def pig_it(text: str) -> str:
    """
    Move the first letter of each word to the end of it,
    then add "ay" to the end of the word. Leave
    punctuation marks untouched.
    :param text:
    :return:
    """
    result: List[str] = list()
    for word in text.split(' '):
        word_processor(word, result)

    return ' '.join(result)


def word_processor(word: str, result: list) -> None:
    """
    Processing a single word for the requested pattern
    :param word:
    :param result:
    :return:
    """
    if len(word) > 1:
        result.append('{}ay'.format(word[1:] + word[0]))
    elif len(word) == 1 and word.isalpha():
        result.append('{}ay'.format(word))
    else:
        result.append(word)
