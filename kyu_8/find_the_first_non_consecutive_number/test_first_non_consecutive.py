#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.find_the_first_non_consecutive_number.first_non_consecutive import first_non_consecutive


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Find the first non-consecutive number')
@allure.tag('FUNDAMENTALS', 'ARRAYS')
@allure.link(url='https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python',
             name='Source/Kata')
class FirstNonConsecutiveTestCase(unittest.TestCase):
    """
    Testing first_non_consecutive function
    """

    def test_first_non_consecutive_none(self):
        """
        If the whole array is consecutive then return
        null or Nothing or None.
        :return:
        """

        allure.dynamic.title("Non is expected")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass a list with no non consecutive numbers"):
            lst = [1, 2, 3, 4, 5, 6, 7, 8]
            expected = None

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a list with no non consecutive numbers"):
            lst = [31, 32]
            expected = None

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

    def test_first_non_consecutive_large_list(self):
        """
        Large lists
        :return:
        """

        allure.dynamic.title("Large lists")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass a large list with no non consecutive numbers"):
            lst = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                   47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                   58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
                   69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                   80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
                   91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                   102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119]
            expected = None

            print_log(list=lst,
                      expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a large list with no non consecutive numbers"):
            lst = [98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
                   108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
                   118, 119, 120, 121, 122, 123, 124, 125, 126, 127,
                   128, 129, 130, 131, 132, 133, 134, 135, 136, 137,
                   138, 139, 140, 141, 142, 143, 144, 145, 146, 147,
                   148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]
            expected = None

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a large list with non consecutive number"):
            lst = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
                   74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                   87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
                   101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
                   112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,
                   123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133,
                   134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
                   145, 146, 147, 148, 149]
            expected = 101

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

    def test_first_non_consecutive_positive(self):
        """
        If we have an array [1,2,3,4,6,7,8] then 1 then 2
        then 3 then 4 are all consecutive but 6 is not,
        so that's the first non-consecutive number.
        :return:
        """

        allure.dynamic.title("Non consecutive number should be returned")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass a list with positive non consecutive number"):
            lst = [1, 2, 3, 4, 6, 7, 8]
            expected = 6

            print_log(list=lst,
                      expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a list with positive non consecutive number"):
            lst = [4, 6, 7, 8, 9, 11]
            expected = 6

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a list with positive non consecutive number"):
            lst = [4, 5, 6, 7, 8, 9, 11]
            expected = 11

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a list with positive non consecutive number"):
            lst = [-3, -2, 0, 1]
            expected = 0

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a list with positive non consecutive number"):
            lst = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 25, 26, 27]
            expected = 25

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

        with allure.step("Pass a list with positive non consecutive number"):
            lst = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39,
                   40, 41, 42, 43, 44, 45]
            expected = 39

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)

    def test_first_non_consecutive_negative(self):
        """
        non-consecutive is a negative number.
        :return:
        """

        allure.dynamic.title("Negative non consecutive number should be returned")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass a list with negative non consecutive number"):
            lst = [-5, -4, -3, -1]
            expected = -1

            print_log(list=lst, expected=expected)
            self.assertEqual(first_non_consecutive(lst), expected)
