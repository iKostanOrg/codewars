"""
Test for -> Computer problem series #1: Fill the Hard Disk Drive.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS LISTS DATA STRUCTURES ARRAYS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.fill_the_hard_disk_drive.save import save


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Computer problem series #1: '
              'Fill the Hard Disk Drive')
@allure.tag('FUNDAMENTALS',
            'LISTS',
            'DATA STRUCTURES',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/5d49c93d089c6e000ff8428c',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SaveTestCase(unittest.TestCase):
    """Testing 'save' function."""

    @parameterized.expand([
        ([11, 13, 15, 17, 19], 8, 0),
        ([45], 12, 0)])
    def test_save_negative(self, sizes, hd, expected):
        """
        Testing 'save' function: negative.

        The function should determine how many
        files of the copy queue you will be able
        to save into your Hard Disk Drive.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'save' function: negative")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter sizes: {sizes}, "
                         f"hd: {hd} "
                         f"and verify the expected output: {expected}."):
            print_log(sizes=sizes, hd=hd, expected=expected)
            self.assertEqual(expected, save(sizes, hd))

    @parameterized.expand([
        ([4, 4, 4, 3, 3], 12, 3),
        ([4, 4, 4, 3, 3], 11, 2),
        ([4, 8, 15, 16, 23, 42], 108, 6),
        ([13], 13, 1),
        ([1, 2, 3, 4], 250, 4),
        ([100], 500, 1)])
    def test_save_positive(self, sizes, hd, expected):
        """
        Testing 'save' function: positive.

        The function should determine how many
        files of the copy queue you will be able
        to save into your Hard Disk Drive.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'save' function: positive")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter sizes: {sizes}, "
                         f"hd: {hd} "
                         f"and verify the expected output: {expected}."):
            print_log(sizes=sizes, hd=hd, expected=expected)
            self.assertEqual(expected, save(sizes, hd))
