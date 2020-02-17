#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.remove_string_spaces.remove_string_spaces import no_space


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Remove String Spaces')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class NoSpaceTestCase(unittest.TestCase):
    """
    Testing no_space function
    """

    def test_something(self):
        """
        Test that no_space function removes the spaces
        from the string, then return the resultant string.
        :return:
        """
        allure.dynamic.title("Test that no_space function "
                             "removes the spaces")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass string with spaces "
                         "and verify the result"):
            string = '8 j 8   mBliB8g  imjB8B8  jl  B'
            expected = '8j8mBliB8gimjB8B8jlB'

            print_log(string=string, expected=expected)

            self.assertEqual(no_space(string), expected)

        with allure.step("Pass string with spaces "
                         "and verify the result"):
            string = '8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'
            expected = '88Bifk8hB8BB8BBBB888chl8BhBfd'

            print_log(string=string, expected=expected)

            self.assertEqual(no_space(string), expected)

        with allure.step("Pass string with spaces "
                         "and verify the result"):
            string = '8aaaaa dddd r     '
            expected = '8aaaaaddddr'

            print_log(string=string, expected=expected)

            self.assertEqual(no_space(string), expected)

        with allure.step("Pass string with spaces "
                         "and verify the result"):
            string = 'jfBm  gk lf8hg  88lbe8 '
            expected = 'jfBmgklf8hg88lbe8'

            print_log(string=string, expected=expected)

            self.assertEqual(no_space(string), expected)

        with allure.step("Pass string with spaces "
                         "and verify the result"):
            string = '8j aam'
            expected = '8jaam'

            print_log(string=string, expected=expected)

            self.assertEqual(no_space(string), expected)
