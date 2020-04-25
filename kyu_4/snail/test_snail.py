#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS ARRAYS

import allure
import unittest
from utils.log_func import print_log
from kyu_4.snail.snail_sort import snail


@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story("Snail")
@allure.tag('ALGORITHMS', 'ARRAYS', 'LISTS')
@allure.link(url='https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python',
             name='Source/Kata')
class SnailTestCase(unittest.TestCase):

    def test_snail(self):
        """
        Testing 'snail' function

        Given an n x n array, 'snail' function should return the array
        elements arranged from outermost elements to the middle element,
        traveling clockwise.
        """

        allure.dynamic.title("Testing 'snail' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Verify that 'snail' function returns the array elements "
                                        "arranged from outermost elements to the middle element, "
                                        "traveling clockwise</p>")

        test_data = (
            ([[]], []),
            ([[1]], [1]),
            ([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
             [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3],
              [8, 9, 4],
              [7, 6, 5]],
             [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([[12, 849, 763, 672, 927, 562, 633, 243],
              [215, 121, 825, 295, 741, 124, 1, 657],
              [705, 179, 76, 684, 268, 480, 437, 219],
              [484, 371, 568, 92, 107, 256, 987, 162],
              [83, 122, 458, 884, 552, 168, 431, 969],
              [102, 383, 173, 169, 672, 805, 949, 900],
              [732, 200, 846, 132, 182, 466, 675, 692],
              [310, 519, 31, 783, 258, 386, 551, 245]],
             [12, 849, 763, 672, 927, 562, 633, 243, 657,
              219, 162, 969, 900, 692, 245, 551, 386, 258,
              783, 31, 519, 310, 732, 102, 83, 484, 705,
              215, 121, 825, 295, 741, 124, 1, 437, 987,
              431, 949, 675, 466, 182, 132, 846, 200, 383,
              122, 371, 179, 76, 684, 268, 480, 256, 168,
              805, 672, 169, 173, 458, 568, 92, 107, 552, 884])
        )

        for snail_map, expected in test_data:
            actual_result: list = snail(snail_map)
            print_log(snail_mapg=snail_map,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test array and "
                             "verify the output vs "
                             "expected result"):
                self.assertListEqual(expected, actual_result)
