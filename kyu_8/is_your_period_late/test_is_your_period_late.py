#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from datetime import date
from utils.log_func import print_log
from kyu_8.is_your_period_late.is_your_period_late import period_is_late


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Date")
@allure.story('Is your period late')
class PeriodIsLateTestCase(unittest.TestCase):
	"""
	Testing period_is_late function
	"""

	def test_period_is_late_positive(self):
		"""
		Positive tests
		:return:
		"""

		allure.dynamic.title("Testing period_is_late function (positive)")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass last, today and period length"):
			last = date(2016, 6, 13)
			today = date(2016, 7, 16)
			cycle_length = 28

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=True)

			self.assertTrue(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 7, 12)
			today = date(2016, 8, 10)
			cycle_length = 28

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=True)

			self.assertTrue(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 7, 1)
			today = date(2016, 8, 1)
			cycle_length = 30

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=True)

			self.assertTrue(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 1, 1)
			today = date(2016, 2, 1)
			cycle_length = 30

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=True)

			self.assertTrue(period_is_late(last, today, cycle_length))

	def test_period_is_late_negative(self):
		"""
		Negative tests
		:return:
		"""

		allure.dynamic.title("Testing period_is_late function (negative)")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass last, today and period length"):
			last = date(2016, 6, 13)
			today = date(2016, 7, 16)
			cycle_length = 35

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=False)
			self.assertFalse(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 6, 13)
			today = date(2016, 7, 16)
			cycle_length = 35

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=False)
			self.assertFalse(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 6, 13)
			today = date(2016, 6, 29)
			cycle_length = 28

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=False)
			self.assertFalse(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 7, 12)
			today = date(2016, 8, 9)
			cycle_length = 28

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=False)
			self.assertFalse(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 6, 1)
			today = date(2016, 6, 30)
			cycle_length = 30

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=False)
			self.assertFalse(period_is_late(last, today, cycle_length))

		with allure.step("Pass last, today and period length"):
			last = date(2016, 1, 1)
			today = date(2016, 1, 31)
			cycle_length = 30

			print_log(last=last,
			          today=today,
			          cycle_length=cycle_length,
			          expected=False)
			self.assertFalse(period_is_late(last, today, cycle_length))
