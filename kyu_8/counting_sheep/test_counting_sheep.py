"""
Test for -> Counting sheep...

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.counting_sheep.counting_sheep import count_sheep


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Counting sheep...')
@allure.tag('FUNDAMENTALS',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/54edbc7200b811e956000556',
    name='Source/Kata')
# pylint: enable=R0801
class CountingSheepTestCase(unittest.TestCase):
    """Testing 'count_sheep' function."""

    def test_counting_sheep(self):
        """
        Testing 'count_sheep' function.

        Consider an array of sheep where some sheep
        may be missing from their place.
        We need a function that counts the
        number of sheep present in the array
        (true means present).
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Testing 'count_sheep' function: positive flow")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        lst: list = [True, True, True, False,
                     True, True, True, True,
                     True, False, True, False,
                     True, False, False, True,
                     True, True, True, True,
                     False, False, True, True]
        expected: int = 17
        print_log(list=lst, expected=expected)
        self.assertEqual(expected,
                         count_sheep(lst),
                         f"There are 17 sheep in total, "
                         f"not {count_sheep(lst)}")

    def test_counting_sheep_bad_input(self):
        """
        Testing 'count_sheep' function, invalid values.

        Hint: Don't forget to check for
        bad values like null/undefined
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Testing 'count_sheeps' function: bad input")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        lst: list = []
        expected: int = 0
        print_log(list=lst, expected=expected)
        self.assertEqual(expected,
                         count_sheep(lst),
                         f"There are 0 sheep in total, "
                         f"not {count_sheep(lst)}")

    def test_counting_sheep_empty_list(self):
        """
        Testing 'count_sheep' function, empty list.

        Hint: Don't forget to check for
        bad values like empty list
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Testing 'count_sheep' function: empty list")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        lst: list = []
        expected: int = 0
        print_log(list=lst, expected=expected)
        self.assertEqual(expected,
                         count_sheep(lst),
                         f"There are 0 sheep in total, "
                         f"not {count_sheep(lst)}")

    def test_counting_sheep_mixed_list(self):
        """
        Testing 'count_sheep' function, null value.

        Hint: Don't forget to check for
        bad values like mixed list
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Testing 'count_sheep' function: mixed list")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        lst: list = [True, False, None]
        expected: int = 1
        print_log(list=lst, expected=expected)
        self.assertEqual(expected,
                         count_sheep(lst),
                         f"There are 0 sheep in total, "
                         f"not {count_sheep(lst)}")
