#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import pytest
from kyu_6.easy_diagonal.diagonal import diagonal


@pytest.mark.skip(reason="The solution is not ready")
class DiagonalTestCase(unittest.TestCase):
	def test_diagonal(self):

		test_data = (
			(7, 0, 8),
			(7, 1, 28),
			(100, 0, 101),
			(7, 2, 56),
			(20, 3, 5985),
			(20, 4, 20349),
			(20, 15, 20349),
			(1291, 5, 6385476296235036),
			(129100, 5, 6429758786797926366807779220)
		)

		for td in test_data:

			n = td[0]
			p = td[1]
			expected = td[2]

			result = diagonal(n, p)
			self.assertEqual(expected, result)
