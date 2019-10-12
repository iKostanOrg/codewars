import unittest
from first_character_that_repeats.first_character_that_repeats import first_dup

# ALGORITHMS


class FirstDupTestCase(unittest.TestCase):
	"""
	Testing first_dup function
	"""

	def test_first_dup_none(self):
		"""
		Test string with no duplicate chars
		:return:
		"""
		self.assertEqual(first_dup('like'), None)
		self.assertEqual(first_dup('bar'), None)

	def test_first_dup_mixed(self):
		"""
		Test string with mixed type of chars
		:return:
		"""
		self.assertEqual(first_dup('1a2b3a3c'), 'a')

	def test_first_alpha_only(self):
		"""
		Test string with alphabet chars only
		:return:
		"""
		self.assertEqual(first_dup('tweet'), 't')
		self.assertEqual(first_dup('Ode to Joy'), ' ')
		self.assertEqual(first_dup('ode to joy'), 'o')

	def test_first_no_alpha(self):
		"""
		Test string with no alphabet chars
		:return:
		"""
		self.assertEqual(first_dup('123123'), '1')
		self.assertEqual(first_dup('!@#$!@#$'), '!')
