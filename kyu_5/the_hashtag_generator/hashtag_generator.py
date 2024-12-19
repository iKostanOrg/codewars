"""
Solution for -> The Hashtag Generator.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def generate_hashtag(word: str) -> bool | str:
    """
    Hashtag Generator.

    1. It must start with a hashtag (#).
    2. All words must have their first letter capitalized.
    3. If final result is longer than 140 chars it must return false.
    4. Input or result must return false when empty.

    :param word: str
    :return:
    """
    if len(word.strip()) < 1:
        return False

    result: str = ''.join(string.capitalize() for string in word.split(' ')
                          if string.strip() != '')
    result = '#' + result
    return False if len(result) > 140 else result
