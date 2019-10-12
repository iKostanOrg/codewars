import unittest
from disemvowel_trolls.disemvowel_trolls import disemvowel

# FUNDAMENTALS, STRINGS, REGULAR EXPRESSIONS, DECLARATIVE PROGRAMMING, ADVANCED LANGUAGE FEATURES


class MdisemvowelTestCase(unittest.TestCase):
	"""
	Testing disemvowel function
	"""

	def test_disemvowel(self):
		"""
		The string "This website is for losers LOL!"
		should become "Ths wbst s fr lsrs LL!"
		:return:
		"""
		self.assertEqual(disemvowel("This website is for losers LOL!"),
		                 "Ths wbst s fr lsrs LL!")
