"""
Test for -> Sum of powers of 2
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS FUNDAMENTALS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.sum_of_powers_of_2.sum_of_powers_of_2 import powers


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Sum of powers of 2')
@allure.tag('ALGORITHMS',
            'FUNDAMENTALS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/5d9f95424a336600278a9632/train/python',
    name='Source/Kata')
class SumOfPowerOfTwoTestCase(unittest.TestCase):
    """
    Testing 'powers' function
    """
    def test_powers(self):
        """
        The function powers takes a single parameter,
        the number n, and should return an array of
        unique numbers.
        :return:
        """
        allure.dynamic.title("powers function should return "
                             "an array of unique numbers")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Pass n = 1 and verify the output"):
            number = 1
            expected = [1]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 2 and verify the output"):
            number = 2
            expected = [2]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 4 and verify the output"):
            number = 4
            expected = [4]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 6 and verify the output"):
            number = 6
            expected = [2, 4]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 14 and verify the output"):
            number = 14
            expected = [2, 4, 8]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 32 and verify the output"):
            number = 32
            expected = [32]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 128 and verify the output"):
            number = 128
            expected = [128]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 512 and verify the output"):
            number = 512
            expected = [512]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 514 and verify the output"):
            number = 514
            expected = [2, 512]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 688 and verify the output"):
            number = 688
            expected = [16, 32, 128, 512]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 8197 and verify the output"):
            number = 8197
            expected = [1, 4, 8192]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 1966 and verify the output"):
            number = 1966
            expected = [2, 4, 8, 32, 128, 256, 512, 1024]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 134217736 and verify the output"):
            number = 134217736
            expected = [8, 134217728]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 140737488355330 and verify the output"):
            number = 140737488355330
            expected = [2, 140737488355328]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 35184372088896 and verify the output"):
            number = 35184372088896
            expected = [64, 35184372088832]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)

        with allure.step("Pass n = 9007199254740991 and verify the output"):
            number = 9007199254740991
            expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,
                        16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152,
                        4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
                        536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184,
                        34359738368, 68719476736, 137438953472, 274877906944, 549755813888,
                        1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416,
                        35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312,
                        1125899906842624, 2251799813685248, 4503599627370496]

            print_log(n=number, expected=expected)
            self.assertEqual(powers(number), expected)
