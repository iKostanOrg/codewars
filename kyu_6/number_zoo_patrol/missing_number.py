"""
Solution for -> Number Zoo Patrol.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def find_missing_number(numbers: list) -> int:
    """
    Find missing number.

    A function that takes a shuffled list of unique numbers
    from 1 to n with one element missing (which can be any
    number including n). Return this missing number.

    :param numbers: a shuffled list of unique numbers
                    from 1 to n with one element missing
    :return: a missing number
    """
    # 1 - one is missing
    if 1 not in numbers:
        return 1

    # 2 - the range is ok, next number (the one comes after last one) is missing
    max_num: int = max(numbers)
    length: int = len(numbers)
    if length == max_num:
        return max_num + 1

    # 3 - some number inside the range is missing
    total: int = sum(numbers)
    return sum(range(1, max_num + 1)) - total
