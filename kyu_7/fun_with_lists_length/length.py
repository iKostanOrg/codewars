"""
Solution for -> Fun with lists: length.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def length(head) -> int:
    """
    Length function.

    The method length, which accepts a linked list
    (head), and returns the length of the list.
    :param head:
    :return:
    """
    i: int = 0

    if head is None:
        return 0

    while head.next is not None:
        head = head.next
        i += 1

    return i + 1
