"""
Solution for -> Complete The Pattern #5 - Even Ladder.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

def pattern(n: int) -> str:
    """
    'pattern' function.

    Create the pattern up to n/2 number of lines.
    :param n:
    :return:
    """
    # If n <= 1 then it should return "" (i.e. empty string).
    if n < 2:
        return ''
    # If any odd number is passed as argument then the pattern
    # should last up to the largest even number which is smaller
    # than the passed odd number.
    lines: list = []
    for i in range(2, n + 1, 2):
        # Note: There are no spaces in the pattern.
        lines.append(f'{i}' * i)
    # Use \n in string to jump to next line.
    return '\n'.join(lines)
