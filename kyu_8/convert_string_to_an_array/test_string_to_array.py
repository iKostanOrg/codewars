#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from utils.log_func import print_log
from kyu_8.convert_string_to_an_array.string_to_array import string_to_array


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Convert a string to an array')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class StringToArrayTestCase(unittest.TestCase):
    """
    Testing string_to_array function.
    """

    def test_string_to_array(self):
        """
        Testing string_to_array function.

        A function to split a string and
        convert it into an array of words.
        :return:
        """

        allure.dynamic.title("Testing string_to_array function")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Enter a test string and verify the output"):

            data = [
                ("Robin Singh", ["Robin", "Singh"]),
                ("CodeWars", ["CodeWars"]),
                ("I love arrays they are my favorite",
                 ["I", "love", "arrays", "they", "are", "my", "favorite"]),
                ("1 2 3", ["1", "2", "3"]),
                ("", [""]),
            ]

            for s, expected in data:
                print_log(s=s, expected=expected)
                self.assertEqual(expected, string_to_array(s))
