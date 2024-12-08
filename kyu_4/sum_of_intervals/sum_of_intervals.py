"""
Solution for -> Sum of Intervals.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def sum_of_intervals(intervals: list) -> int:
    """
    Sum of intervals.

    Accept an array of intervals, and returns
    the sum of all the interval lengths.
    Overlapping intervals should only be counted once.
    :param intervals: list
    :return: int
    """

    intervals = remove_overlaps(intervals)
    results: list = [(i[1] - i[0]) for i in intervals]
    return sum(results)


def remove_overlaps(intervals: list) -> list:
    """
    Remove overlaps and duplicates.

    :param intervals: list
    :return: int
    """
    is_clean: bool = False

    while not is_clean:
        is_clean = True
        for index_i, i in enumerate(intervals):
            for index_b, b in enumerate(intervals):
                if index_b != index_i:
                    is_clean = clean_interval(intervals, i, b)
                    if not is_clean:
                        break

    return intervals


def clean_interval(intervals: list,
                   i: tuple,
                   b: tuple) -> bool:
    """
    Remove intervals.

    :param intervals: list
    :param i: tuple
    :param b: tuple
    :return: bool
    """
    result: bool = True

    if i[0] == b[0] and i[1] == b[1]:
        intervals.remove(b)
        result = False

    if i[0] < b[0] < i[1] <= b[1]:
        intervals.append((i[0], b[1]))
        intervals.remove(i)
        intervals.remove(b)
        result = False

    if b[0] < i[0] < b[1] <= i[1]:
        intervals.append((b[0], i[1]))
        intervals.remove(i)
        intervals.remove(b)
        result = False

    if b[0] < i[0] < i[1] < b[1]:
        intervals.remove(i)
        result = False

    if i[0] < b[0] < b[1] < i[1]:
        intervals.remove(b)
        result = False

    if i[0] == b[0] and b[1] < i[1]:
        intervals.remove(b)
        result = False

    if i[0] == b[0] and i[1] < b[1]:
        intervals.remove(i)
        result = False

    return result
