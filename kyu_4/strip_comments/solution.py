"""
Solution for -> Strip Comments.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def solution(string: str, markers: list) -> str:
    """
    Strip comments solution.

    The solution strips all text that follows any of a set
    of comment markers passed in. Any whitespace at the end
    of the line will be stripped out as well.

    :param string: str
    :param markers: list
    :return: str
    """
    strings: list = string.split('\n')
    for marker in markers:
        strings = [(s.strip() if marker not in s else s[:s.index(marker)].strip()) for s in strings]
    return '\n'.join(strings)
