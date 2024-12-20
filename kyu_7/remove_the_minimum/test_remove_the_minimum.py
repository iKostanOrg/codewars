"""
Test for -> The museum of incredible dull things.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS, LISTS, DATA STRUCTURES, ARRAYS

import unittest
import allure
from numpy.random import randint
from kyu_7.remove_the_minimum.remove_the_minimum import remove_smallest


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('The museum of incredible dull things')
@allure.tag('FUNDAMENTALS',
            'LISTS',
            'DATA STRUCTURES',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/563cf89eb4747c5fb100001b',
    name='Source/Kata')
# pylint: enable-msg=R0801
class RemoveSmallestTestCase(unittest.TestCase):
    """Testing remove_smallest function."""

    @staticmethod
    def random_list():
        """
        Create random list helper function.

        :return:
        """
        with allure.step("Create a random list"):
            return list(randint(400, size=randint(1, 10)))

    def test_remove_smallest(self):
        """
        Test lists with multiple digits.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("'multiply' function verification: "
                             "lists with multiple digits")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Remove smallest value from "
                         "the start of the list"):
            self.assertEqual(remove_smallest([1, 2, 3, 4, 5]),
                             [2, 3, 4, 5],
                             "Wrong result for [1, 2, 3, 4, 5]")

        with allure.step("Remove smallest value from "
                         "near the end of the list"):
            self.assertEqual(remove_smallest([5, 3, 2, 1, 4]),
                             [5, 3, 2, 4],
                             "Wrong result for [5, 3, 2, 1, 4]")

        with allure.step("Remove smallest value from "
                         "the end of the list"):
            self.assertEqual(remove_smallest([1, 2, 3, 1, 1]),
                             [2, 3, 1, 1],
                             "Wrong result for [1, 2, 3, 1, 1]")

    def test_remove_smallest_empty_list(self):
        """
        Test with empty list.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("'multiply' function verification "
                             "with empty list")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Remove smallest value from the empty list"):
            self.assertEqual(remove_smallest([]),
                             [],
                             "Wrong result for []")

    def test_remove_smallest_one_element_list(self):
        """
        Returns [] if list has only one element.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("'multiply' function verification "
                             "with one element list")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Remove smallest value from "
                         "the empty list with one element only"):
            i: int = 0
            while i < 10:
                x = randint(1, 400)
                self.assertEqual(remove_smallest([x]),
                                 [],
                                 f"Wrong result for [{x}]")
                i += 1

    def test_remove_smallest_random_list(self):
        """
        Returns a list that misses only one element.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("'multiply' function verification "
                             "with random list")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Remove smallest value from the random list"):
            i: int = 0
            while i < 10:
                arr = self.random_list()
                self.assertEqual(len(remove_smallest(arr[:])),
                                 len(arr) - 1,
                                 f"Wrong sized result for {arr}")
                i += 1
