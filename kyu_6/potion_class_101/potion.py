"""
Solution for -> Potion Class 101.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


import math
from typing import Tuple


class Potion:
    """
    Potion.

    This is your first potion class in Hogwarts and professor
    gave you a homework to figure out what color potion will
    turn into if he'll mix it with some other potion. All potions
    have some color that written down as RGB color from [0, 0, 0]
    to [255, 255, 255]. To make task more complicated teacher will
    do few mixing and after will ask you for final color. Besides
    color, you also need to figure out what volume will have potion
    after final mix.
    """

    def __init__(self, color: Tuple[int, int, int], volume: int):
        """
        Create a new Potion instance.

        :param color:
        :param volume:
        """
        self._color: Tuple[int, int, int] = color
        self._volume: int = volume

    def mix(self, other) -> object:
        """
        Mix.

        Based on your programming background you managed to figure
        that after mixing two potions colors will mix as if mix
        two RGB colors.

        Note: Use ceiling when calculating the resulting potion's color.
        :param other:
        :return:
        """
        new_volume = self.volume + other.volume

        r = math.ceil((other.color[0] * other.volume + self.color[0]
                       * self.volume) / (other.volume + self.volume))
        g = math.ceil((other.color[1] * other.volume + self.color[1]
                       * self.volume) / (other.volume + self.volume))
        b = math.ceil((other.color[2] * other.volume + self.color[2]
                       * self.volume) / (other.volume + self.volume))

        return Potion((r, g, b), new_volume)

    @property
    def volume(self) -> int:
        """
        Return volume value.

        :return: int
        """
        return self._volume

    @volume.setter
    def volume(self, value: int) -> None:
        """
        Set volume value.

        :param value: int
        :return:
        """
        self._volume = value

    @property
    def color(self) -> tuple:
        """
        Get color value.

        :return: tuple
        """
        return self._color

    @color.setter
    def color(self, value: Tuple[int, int, int]) -> None:
        """
        Set color value.

        :param value: tuple
        :return:
        """
        self._color = value
