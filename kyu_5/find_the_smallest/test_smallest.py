"""
Test for -> Find the smallest
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import pytest
import allure
from utils.log_func import print_log
from kyu_5.find_the_smallest.solution import smallest


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Find the smallest')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/573992c724fc289553000e95',
    name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
# pylint: enable-msg=R0801
class FindSmallestTestCase(unittest.TestCase):
    """
    Testing smallest function
    """

    def test_smallest(self):
        """
        Test a function `smallest` which will return an array or a tuple or a string
        depending on the language (see "Sample Tests").
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing smallest function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        test_data: tuple = ((261235, [126235, 2, 0]),
                            (209917, [29917, 0, 1]),
                            (285365, [238565, 3, 1]),
                            (269045, [26945, 3, 0]),
                            (296837, [239687, 4, 1]),
                            (346674147588841927, [134667414758884927, 14, 0]),
                            (352343279580894007, [35234327958089407, 15, 0]),
                            (633814808310045545, [63381480831045545, 11, 0]),
                            (935855753, [358557539, 0, 8]),
                            (71269954474326234, [12679954474326234, 0, 3]),
                            (400360725952391834, [3460725952391834, 0, 3]),
                            (914459749498173781, [144597494981737819, 0, 17]),
                            (113343536213382181, [111334353621338218, 17, 0]),
                            (614132919143656569, [141326919143656569, 0, 5]))

        for n, expected in test_data:
            result = smallest(n)
            with allure.step("Enter test data and verify the output vs expected"):
                print_log(n=n,
                          expected=expected,
                          result=result)

                self.assertListEqual(expected, result)
