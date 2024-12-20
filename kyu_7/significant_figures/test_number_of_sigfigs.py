"""
Test for -> Significant Figures.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS MATHEMATICS NUMBERS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.significant_figures.number_of_sigfigs import number_of_sigfigs


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Significant Figures')
@allure.tag('ALGORITHMS',
            'MATHEMATICS',
            'NUMBERS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/5d9fe0ace0aad7001290acb7',
    name='Source/Kata')
class NumberOfSigFigsTestCase(unittest.TestCase):
    """Testing number_of_sigfigs function."""

    @parameterized.expand([
        (1, "1"),
        (0, "0"),
        (1, "0003"),
        (1, "3000"),
        (3, "404"),
        (7, "050030210"),
        (1, "0.1"),
        (2, '1.0'),
        (3, '4.40'),
        (4, '90.00'),
        (1, "0.0"),
        (9, '03.27310000'),
        (10, '23625700.00'),
        (10, '09.971730000'),
        (10, '0000.0673560000')])
    def test_number_of_sigfigs(self, exp, inp):
        """
        Testing 'number_of_sigfigs' function with various test inputs.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            'Testing number_of_sigfigs function')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Pass a number: {inp} "
                         f"and verify the expected output: {exp}."):
            print_log(inp=inp, expected=exp)
            self.assertEqual(exp, number_of_sigfigs(inp))
