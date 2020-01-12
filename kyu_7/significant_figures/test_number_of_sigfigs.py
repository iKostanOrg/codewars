#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS MATHEMATICS NUMBERS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.significant_figures.number_of_sigfigs import number_of_sigfigs


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Significant Figures')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class NumberOfSigFigsTestCase(unittest.TestCase):
    """
    Testing number_of_sigfigs function
    """

    def test_number_of_sigfigs(self):
        """
        Testing number_of_sigfigs function
        with various test inputs
        :return:
        """

        allure.dynamic.title('Testing number_of_sigfigs function')
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Pass string and verify the output"):
            TESTS = [
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
                (10, '0000.0673560000')
            ]

            for exp, inp in TESTS:
                print_log(inp=inp, expected=exp)
                self.assertEqual(exp, number_of_sigfigs(inp))
