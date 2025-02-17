"""
Test for -> print_log function.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import unittest
from unittest.mock import patch
import allure  # pylint: disable=import-error
from utils.log_func import print_log


# pylint: disable=R0801
@allure.epic('No kyu')
@allure.parent_suite('Helper methods')
@allure.suite("No kyu helper methods")
@allure.sub_suite("Unit Tests")
@allure.feature("Utils")
@allure.story('Testing print_log util')
@allure.tag('UTILS')
@allure.link(
    url='https://github.com/ikostan/codewars/tree/master/utils',
    name='Source')
# pylint: enable=R0801
class LogFuncTestCase(unittest.TestCase):
	"""Test for print_log function."""

	@patch('builtins.print')
	def test_log_func(self, mock_print):
		"""
		Testing print_log function.

		:param mock_print:
		:return:
		"""
		# pylint: disable=R0801
		allure.dynamic.title(
			"Positive test cases for print_log function testing")
		allure.dynamic.severity(allure.severity_level.CRITICAL)
		allure.dynamic.description_html(
			'<h3>Codewars badge:</h3>'
			'<img src="https://www.codewars.com/users/myFirstCode'
			'/badges/large">'
			'<h3>Test Description:</h3>'
			"<p></p>")
		# pylint: enable=R0801
		with allure.step("Compare expected print with the actual result."):
			print_log(str="Hello World!")
			mock_print.assert_called_with('\nLOG =>\nstr: Hello World!\n')
