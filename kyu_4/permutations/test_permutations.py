#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS PERMUTATIONS STRINGS

import allure
import unittest
import pytest
from utils.log_func import print_log
from kyu_4.permutations.permutations import permutations


@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story("Permutations")
@pytest.mark.skip(reason="The solution is not ready")
class PermutationsTestCase(unittest.TestCase):

	def test_permutations(self):
		"""
		Testing permutations function

		Test that permutations function creates all
		permutations of an input string and
	    remove duplicates, if present. This means, you
	    have to shuffle all letters from the input in all
	    possible orders.
		"""

		allure.dynamic.title("Testing permutations function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Enter a test string and verify the output"):
			test_data = [
				('a', ['a']),
				('ab', ['ab', 'ba']),
				('aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']),
				('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
				('abcd', ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
				          'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
				          'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
				          'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']),
				('dcba', ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
				          'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
				          'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
				          'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
			]

			for string, expected in test_data:

				print_log(string=string,
				          expected=expected)

				self.assertListEqual(sorted(expected),
				                     sorted(permutations(string)))
