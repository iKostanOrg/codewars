"""
Test for -> Simple Fun #152: Invite More Women?.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# PUZZLES GAMES

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.simple_fun_152.invite_more_women import invite_more_women


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Simple Fun #152: Invite More Women?')
@allure.tag('PUZZLES',
            'GAMES')
@allure.link(
    url='https://www.codewars.com/kata/58acfe4ae0201e1708000075',
    name='Source/Kata')
# pylint: enable-msg=R0801
class InviteMoreWomenTestCase(unittest.TestCase):
    """Testing invite_more_women function."""

    @parameterized.expand([
        ([-1, -1, -1], False),
        ([1, -1], False),
        ([], False)])
    def test_invite_more_women_positive(self, arr, expected):
        """
        Testing invite_more_women function (positive).

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title('Testing invite_more_women function (positive)')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f'Enter test data: {arr} '
                         f'and verify the expected output: {expected}.'):
            print_log(arr=arr, expected=expected)
            self.assertEqual(invite_more_women(arr), expected)

    @parameterized.expand([
        ([1, -1, 1], True),
        ([1, 1, 1], True)])
    def test_invite_more_women_negative(self, arr, expected):
        """
        Testing invite_more_women function (negative).

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title('Testing invite_more_women function (negative)')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f'Enter test data: {arr} '
                         f'and verify the expected output: {expected}.'):
            print_log(arr=arr, expected=expected)
            self.assertEqual(invite_more_women(arr), expected)
