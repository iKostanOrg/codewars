#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES

import unittest
import allure
import pytest
from utils.log_func import print_log
from kyu_6.string_subpattern_recognition_3.has_subpattern import has_subpattern


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('String subpattern recognition III')
@pytest.mark.skip(reason="The solution is not ready")
class HasSubpatternTestCase(unittest.TestCase):
	"""
	Testing 'has_subpattern' function
	"""

	def test_has_subpattern(self):
		"""
		Verify that 'has_subpattern' function to returns
        either true/True or false/False if a string can be
        seen as the repetition of a simpler/shorter subpattern or not.
		:return:
		"""

		allure.dynamic.title("Testing 'has_subpattern' (part 3) function")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Pass the string and verify the output"):
			data_set = [
				("a", "a"),
				("aaaa", "a"),
				("abcd", "abcd"),
				("babababababababa", "ab"),
				("bbabbaaabbaaaabb", "ab"),
				("123a123a123a", "123a"),
				("123A123a123a", "111222333Aaa"),
				("12aa13a21233", "123a"),
				("12aa13a21233A", "111222333Aaaa"),
				("abcdabcaccd", "aaabbccccdd"),
			]

			for data in data_set:
				print_log(string=data[0], expected=data[1])
				self.assertEqual(data[1], has_subpattern(data[0]))
