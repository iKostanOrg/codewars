"""
Animal class implementation for -> Make Class
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class Animal:
    """
    Animal class implementation
    """
    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._species = kwargs['species']
        self._age = kwargs['age']
        self._health = kwargs['health']
        self._weight = kwargs['weight']
        self._color = kwargs['color']

    @property
    def name(self) -> str:
        """
        Get name
        :return:
        """
        return self._name

    @name.setter
    def name(self, val: str) -> None:
        """
        Set name
        :param val:
        :return:
        """
        self._name = val

    @property
    def species(self) -> str:
        """
        Get species
        :return:
        """
        return self._species

    @species.setter
    def species(self, val: str) -> None:
        """
        Set species
        :param val:
        :return:
        """
        self._species = val

    @property
    def age(self) -> str:
        """
        Get age
        :return:
        """
        return self._age

    @age.setter
    def age(self, val: str) -> None:
        """
        Set age
        :param val:
        :return:
        """
        self._age = val

    @property
    def health(self) -> str:
        """
        Get health
        :return:
        """
        return self._health

    @health.setter
    def health(self, val: str) -> None:
        """
        Set health
        :param val:
        :return:
        """
        self._health = val

    @property
    def weight(self) -> str:
        """
        Get weight
        :return:
        """
        return self._weight

    @weight.setter
    def weight(self, val: str) -> None:
        """
        Set weight
        :param val:
        :return:
        """
        self._weight = val

    @property
    def color(self) -> str:
        """
        Get color
        :return:
        """
        return self._color

    @color.setter
    def color(self, val: str) -> None:
        """
        Set color
        :param val:
        :return:
        """
        self._color = val
