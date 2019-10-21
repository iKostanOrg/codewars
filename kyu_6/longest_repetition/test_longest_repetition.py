#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS STRINGS FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.longest_repetition.longest_repetition import longest_repetition


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('First character that repeats')
class LongestRepetitionTestCase(unittest.TestCase):
	"""
	Testing longest_repetition function
	"""

	def test_longest_repetition(self):
		"""
		For a given string s find the character c (or C) with
		longest consecutive repetition and return: (c, l)
		where l (or L) is the length of the repetition.

		For empty string return: ('', 0)
		:return:
		"""

		allure.dynamic.title("Testing 'longest_repetition' function")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Pass string and verify the output"):
			tests = [
				# [input, expected],
				["aaaabb", ('a', 4)],
				["bbbaaabaaaa", ('a', 4)],
				["cbdeuuu900", ('u', 3)],
				["abbbbb", ('b', 5)],
				["aabb", ('a', 2)],
				["ba", ('b', 1)],
				["", ('', 0)],
			]

			for t in tests:
				print_log(string=t[0], expected=t[1])
				self.assertEqual(t[1], longest_repetition(t[0]))
