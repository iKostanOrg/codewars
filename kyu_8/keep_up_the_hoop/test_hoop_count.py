#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import allure
import unittest
from utils.log_func import print_log
from kyu_8.keep_up_the_hoop.hoop_count import hoop_count


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Conditions")
@allure.story('Keep up the hoop')
class HoopCountTestCase(unittest.TestCase):

	def test_hoop_count_positive(self):

		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step(""):
			n = 11
			expected = "Great, now move on to tricks"
			print_log(n=n, expected=expected)
			self.assertEqual(hoop_count(n), expected)

	def test_hoop_count_negative(self):

		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step(""):
			n = 3
			expected = "Keep at it until you get it"
			print_log(n=n, expected=expected)
			self.assertEqual(hoop_count(n), expected)
