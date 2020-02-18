#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import math


class Potion:
	"""
	This is your first potion class in Hogwarts and professor
	gave you a homework to figure out what color potion will
	turn into if he'll mix it with some other potion. All potions
	have some color that written down as RGB color from [0, 0, 0]
	to [255, 255, 255]. To make task more complicated teacher will
	do few mixing and after will ask you for final color. Besides
	color you also need to figure out what volume will have potion
	after final mix.
	"""
	def __init__(self, color: tuple, volume: int):
		self._color = color
		self._volume = volume

	def mix(self, other):
		"""
		Based on your programming background you managed to figure
		that after mixing two potions colors will mix as if mix
		two RGB colors.

		Note: Use ceiling when calculating the resulting potion's color.
		:param other:
		:return:
		"""
		new_volume = self._volume + other.volume

		r = math.ceil((other.color[0] * other.volume + self.color[0] * self.volume) / (other.volume + self.volume))
		g = math.ceil((other.color[1] * other.volume + self.color[1] * self.volume) / (other.volume + self.volume))
		b = math.ceil((other.color[2] * other.volume + self.color[2] * self.volume) / (other.volume + self.volume))

		return Potion((r, g, b), new_volume)

	@property
	def color(self):
		return self._color

	@property
	def volume(self):
		return self._volume

	@volume.setter
	def volume(self, value):
		self._volume = value

	@color.setter
	def color(self, value):
		self._color = value
