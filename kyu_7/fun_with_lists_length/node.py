"""
Node class for -> Fun with lists: length.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class Node:
    """The linked list."""

    def __init__(self, data, n_next=None):
        """
        Create a new Node instance.

        :param data:
        :param n_next:
        """
        self._data = data
        self._next = n_next

    @property
    def next(self):
        """
        Get next.

        :return:
        """
        return self._next

    @next.setter
    def next(self, n_next=None) -> None:
        """
        Set next.

        :param n_next:
        :return:
        """
        self._next = n_next

    @property
    def data(self):
        """
        Get data.

        :return:
        """
        return self._data

    @data.setter
    def data(self, data) -> None:
        """
        Set data.

        :param data:
        :return:
        """
        self._data = data
