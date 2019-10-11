import unittest
from multiply.multiply import multiply


class MultiplyTestCase(unittest.TestCase):
	def test_multiply(self):
		a = 1
		b = 2
		expected = a * b
		self.assertEqual(expected, multiply(a, b))
