"""
Solution for -> DefaultList.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class DefaultList:
    """A class called DefaultList."""

    def __init__(self, lst: list, default_value: str):
        """
        Create a new DefaultList instance.

        :param lst:
        :param default_value:
        """
        # The class will have two parameters to be given:
        # a list, and a default value.
        self.__lst: list = lst
        self.__default_value: str = default_value

    def __getitem__(self, i: int):
        """
        Get item.

        The default value will be returned any time an index of the list
        is called in the code that would normally raise an error:
        (i.e. i > len(list) - 1 or i < -len(list)).
        :param i:
        :return:
        """
        if i >= len(self.__lst) or i < -len(self.__lst):
            return self.__default_value
        return self.__lst[i]

    def extend(self, items: list) -> None:
        """
        Support the regular list functions: extend.

        :param items: iterable
        :return:
        """
        self.__lst.extend(items)

    def append(self, item) -> None:
        """
        Support the regular list functions: append.

        :param item:
        :return:
        """
        self.__lst.append(item)

    def pop(self, index=None):
        """
        Support the regular list functions: pop.

        :param index:
        :return:
        """
        # Return default value when list is empty or None
        if not self.__lst:
            return self.__default_value

        # Return default value when no index is 0 and list is not empty
        if index == 0 and self.__lst:
            return self.__lst.pop(index)

        # Return default value when no index + list is not empty
        if not index and self.__lst:
            return self.__lst.pop(-1)

        return self.__lst.pop(index)

    def remove(self, item) -> None:
        """
        Support the regular list functions: remove.

        :param item:
        :return:
        """
        self.__lst.remove(item)

    def insert(self, index: int, item) -> None:
        """
        Support the regular list functions: insert.

        :param index:
        :param item:
        :return:
        """
        self.__lst.insert(index, item)

    def __repr__(self) -> str:
        """
        Provide a readable, human-friendly string representation of the object.

        :return:
        """
        return f"lst: {self.__lst}, default: {self.__default_value}"
