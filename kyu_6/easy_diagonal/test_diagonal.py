#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure
import pytest
from kyu_6.easy_diagonal.diagonal import diagonal


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Easy Diagonal')
@allure.tag("FUNDAMENTALS", "ALGORITHMS")
@allure.link(url='https://www.codewars.com/kata/'
                 '559b8e46fa060b2c6a0000bf/train/python',
             name='Source/Kata')
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
