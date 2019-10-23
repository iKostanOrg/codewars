#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# PUZZLES GAMES

import unittest
import allure
from utils.log_func import print_log
from kyu_7.simple_fun_152.invite_more_women import invite_more_women


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Simple Fun #152: Invite More Women?')
class InviteMoreWomenTestCase(unittest.TestCase):
	"""
	Simple Fun #152: Invite More Women?
	Testing invite_more_women function
	"""

	def test_invite_more_women_positive(self):
		"""
		Simple Fun #152: Invite More Women?
		Testing invite_more_women function (positive)
		:return:
		"""

		allure.dynamic.title('Testing invite_more_women function (positive)')
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step('Enter test data and verify the output'):
			data = [
				([-1, -1, -1], False),
				([1, -1], False),
				([], False)
			]

			for d in data:

				arr = d[0]
				expected = d[1]

				print_log(arr=arr, expected=expected)
				self.assertEqual(invite_more_women(arr), expected)

	def test_invite_more_women_negative(self):
		"""
		Simple Fun #152: Invite More Women?
		Testing invite_more_women function (negative)
		:return:
		"""

		allure.dynamic.title('Testing invite_more_women function (negative)')
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step('Enter test data and verify the output'):
			data = [
				([1, -1, 1], True),
				([1, 1, 1], True)
			]

			for d in data:
				arr = d[0]
				expected = d[1]

				print_log(arr=arr, expected=expected)
				self.assertEqual(invite_more_women(arr), expected)
