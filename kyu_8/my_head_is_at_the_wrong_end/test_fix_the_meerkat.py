"""
Test for -> My head is at the wrong end!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS ARRAYS LISTS DATA STRUCTURES

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.my_head_is_at_the_wrong_end.fix_the_meerkat \
    import fix_the_meerkat


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('My head is at the wrong end!')
@allure.tag('ALGORITHMS',
            'ARRAYS',
            'LISTS',
            'DATA STRUCTURES')
@allure.link(
    url='https://www.codewars.com/kata/56f699cd9400f5b7d8000b55',
    name='Source/Kata')
# pylint: enable=R0801
# @pytest.mark.skip(reason="The solution is not ready")
class FixTheMeerkatTestCase(unittest.TestCase):
    """Testing fix_the_meerkat function."""

    @parameterized.expand([
        (["tail", "body", "head"], ["head", "body", "tail"]),
        (["tails", "body", "heads"], ["heads", "body", "tails"]),
        (["bottom", "middle", "top"], ["top", "middle", "bottom"]),
        (["lower legs", "torso", "upper legs"],
         ["upper legs", "torso", "lower legs"]),
        (["ground", "rainbow", "sky"], ["sky", "rainbow", "ground"])])
    def test_fix_the_meerkat(self, arr, expected):
        """
        Testing fix_the_meerkat function with various test data.

        You will be given an array which will have
        three values (tail, body, head).
        It is your job to re-arrange the array so
        that the animal is the right way round
        (head, body, tail).
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "fix_the_meerkat function function verification")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Save the animals by switching them back. "
            "You will be given an array which will have three values "
            "(tail, body, head). It is your job to re-arrange the array "
            "so that the animal is the right way round (head, body, tail)."
            "</p>")
        # pylint: disable=R0801
        result: list = fix_the_meerkat(arr)
        with allure.step(f"Enter test data: {arr} "
                         f"and assert actual result: {result} "
                         f"vs expected: {expected}"):
            print_log(arr=arr, result=result, expected=expected)
            self.assertEqual(expected, result)
