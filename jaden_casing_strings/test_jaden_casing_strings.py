import unittest
from jaden_casing_strings.jaden_casing_strings import toJadenCase

# FUNDAMENTALS, STRINGS, ARRAYS


class JadenCasingStringsTestCase(unittest.TestCase):
	"""
	Testing toJadenCase function
	"""

	def test_to_jaden_case_positive(self):
		"""
		Simple positive test
		:return:
		"""

		quote = "How can mirrors be real if our eyes aren't real"
		expected = "How Can Mirrors Be Real If Our Eyes Aren't Real"
		self.assertEqual(toJadenCase(quote), expected)

	def test_to_jaden_case_negative(self):
		"""
		Simple negative test
		:return:
		"""

		quote = "How can mirrors be real if our eyes aren't real"
		self.assertNotEqual(toJadenCase(quote), quote)
