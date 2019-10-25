#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from kyu_7.fun_with_lists_length.node import Node


def length(head) -> int:
    """
    The method length, which accepts a linked list
    (head), and returns the length of the list.
    :param head:
    :return:
    """
    i = 0

    if head is None:
        return 0

    while head.next is not None:
        head = head.next
        i += 1

    return i + 1
