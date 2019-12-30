#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS STRINGS SEARCH

import unittest
import allure
from utils.log_func import print_log
from kyu_5.first_non_repeating_character.first_non_repeating_letter import first_non_repeating_letter


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('First non-repeating character')
class FirstNonRepeatingLetterTestCase(unittest.TestCase):
	"""
	Testing first_non_repeating_letter function
	"""

	def test_first_non_repeating_letter(self):
		"""
		Testing a function named first_non_repeating_letter
		that takes a string input, and returns the first character
		that is not repeated anywhere in the string.

		For example, if given the input 'stress', the function
		should return 't', since the letter t only occurs once
		in the string, and occurs first in the string.

		As an added challenge, upper- and lowercase letters are
		considered the same character, but the function should
		return the correct case for the initial letter. For example,
		the input 'sTreSS' should return 'T'.

		If a string contains all repeating characters, it should
		return an empty string ("") or None -- see sample tests.
		:return:
		"""
		allure.dynamic.title("Testing first_non_repeating_letter function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Enter test string and verify the output"):
			test_data = [
				('a', 'a'),
				('stress', 't'),
				('moonmen', 'e'),
				('', ''),
				('abba', ''),
				('aa', ''),
				('~><#~><', '#'),
				('hello world, eh?', 'w'),
				('sTreSS', 'T'),
				('Go hang a salami, I\'m a lasagna hog!', ',')
			]

			for data in test_data:
				string = data[0]
				expected = data[1]
				print_log(string=string,
				          expected=expected)
				self.assertEqual(expected,
				                 first_non_repeating_letter(string))
