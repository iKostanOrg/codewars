"""
Solution for -> Snail

Returns the array elements arranged from outermost elements
to the middle element, traveling clockwise.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def snail(snail_map: list) -> list:
    """
    Returns the array elements arranged from outermost elements
    to the middle element, traveling clockwise.

    :param snail_map: n x n array
    :return:  list of elements arranged from outermost elements to
             the middle element, traveling clockwise
    """
    if not snail_map:
        return []

    result: list = []

    while snail_map:
        try:
            # 1 left to right
            for i in snail_map[0]:
                result.append(i)
            del snail_map[0]

            # 2 top to bottom
            for i, row in enumerate(snail_map):
                result.append(row[-1])
                del snail_map[i][-1]

            # 3 right to left
            for i in range(-1, -1 * len(snail_map[-1]) - 1, -1):
                result.append(snail_map[-1][i])
            del snail_map[-1]

            # 4 bottom to top
            for i in range(1, len(snail_map) + 1):
                result.append(snail_map[i * -1][0])
                del snail_map[i * -1][0]

        except IndexError:
            break

    return result
