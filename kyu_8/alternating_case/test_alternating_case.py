#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.alternating_case.alternating_case import to_alternating_case


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('altERnaTIng cAsE <=> ALTerNAtiNG CaSe')
class AlternatingCaseTestCase(unittest.TestCase):
	"""
	Testing to_alternating_case function
	"""

	def test_alternating_case(self):
		"""
		Testing to_alternating_case function
		:return:
		"""


		self.assertEqual(to_alternating_case("hello world"), "HELLO WORLD")


		self.assertEqual(to_alternating_case("HELLO WORLD"), "hello world")


		self.assertEqual(to_alternating_case("hello WORLD"), "HELLO world")


		self.assertEqual(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")


		self.assertEqual(to_alternating_case("12345"), "12345")


		self.assertEqual(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")


		self.assertEqual(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")


		self.assertEqual(to_alternating_case(to_alternating_case("Hello World")), "Hello World")


		title = "altERnaTIng cAsE"
		title = to_alternating_case(title)
		self.assertEqual(title, "ALTerNAtiNG CaSe")
