#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.counting_sheep.counting_sheep import count_sheeps


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Counting sheep...')
@allure.tag('FUNDAMENTALS', 'ARRAYS')
@allure.link(url='',
             name='Source/Kata')
class CountingSheepTestCase(unittest.TestCase):
    """
    Testing 'count_sheeps' function
    """

    def test_counting_sheep(self):
        """
        Testing 'count_sheeps' function
        Consider an array of sheep where some sheep
        may be missing from their place.
        We need a function that counts the
        number of sheep present in the array
        (true means present).
        :return:
        """

        allure.dynamic.title("Testing 'count_sheeps' function: positive flow")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        lst = [True, True, True, False,
               True, True, True, True,
               True, False, True, False,
               True, False, False, True,
               True, True, True, True,
               False, False, True, True]

        expected = 17

        print_log(list=lst,
                  expected=expected)

        self.assertEqual(expected,
                         count_sheeps(lst),
                         "There are 17 sheep in total, "
                         "not %s" % count_sheeps(lst))

    def test_counting_sheep_bad_input(self):
        """
        Testing 'count_sheeps' function
        Hint: Don't forget to check for
        bad values like null/undefined
        :return:
        """

        allure.dynamic.title("Testing 'count_sheeps' function: bad input")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        lst = list()

        expected = 0

        print_log(list=lst,
                  expected=expected)

        self.assertEqual(expected,
                         count_sheeps(lst),
                         "There are 0 sheep in total, "
                         "not %s" % count_sheeps(lst))

    def test_counting_sheep_empty_list(self):
        """
        Testing 'count_sheeps' function
        Hint: Don't forget to check for
        bad values like empty list
        :return:
        """

        allure.dynamic.title("Testing 'count_sheeps' function: empty list")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        lst = []

        expected = 0

        print_log(list=lst,
                  expected=expected)

        self.assertEqual(expected,
                         count_sheeps(lst),
                         "There are 0 sheep in total, "
                         "not %s" % count_sheeps(lst))

    def test_counting_sheep_mixed_list(self):
        """
        Testing 'count_sheeps' function
        Hint: Don't forget to check for
        bad values like mixed list
        :return:
        """

        allure.dynamic.title("Testing 'count_sheeps' function: mixed list")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        lst = [True, False, None]

        expected = 1

        print_log(list=lst,
                  expected=expected)

        self.assertEqual(expected,
                         count_sheeps(lst),
                         "There are 0 sheep in total, "
                         "not %s" % count_sheeps(lst))

