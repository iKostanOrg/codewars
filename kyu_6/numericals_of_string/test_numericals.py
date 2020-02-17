#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS GAMES PUZZLES PERFORMANCE

import unittest
import allure
from utils.log_func import print_log
from kyu_6.numericals_of_string.numericals import numericals


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Numericals of a String')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class NumericalsTestCase(unittest.TestCase):
    """
    Testing 'numericals' function
    """

    def test_numericals(self):
        """
        Testing 'numericals' function
        :return:
        """

        allure.dynamic.title("Testing 'numericals' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass the string and verify the output"):
            string = "Hello, World!"
            expected = "1112111121311"

            print_log(string=string, expected=expected)

            self.assertEqual(numericals(string), expected)

        with allure.step("Pass the string and verify the output"):
            string = "Hello, World! It's me, JomoPipi!"
            expected = "11121111213112111131224132411122"

            print_log(string=string, expected=expected)

            self.assertEqual(numericals(string), expected)

        with allure.step("Pass the string and verify the output"):
            string = "hello hello"
            expected = "11121122342"

            print_log(string=string, expected=expected)

            self.assertEqual(numericals(string), expected)

        with allure.step("Pass the string and verify the output"):
            string = "Hello"
            expected = "11121"

            print_log(string=string, expected=expected)

            self.assertEqual(numericals(string), expected)

        with allure.step("Pass the string and verify the output"):
            string = "aaaaaaaaaaaa"
            expected = "123456789101112"

            print_log(string=string, expected=expected)

            self.assertEqual(numericals(string), expected)
