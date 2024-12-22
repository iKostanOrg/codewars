"""
Test for -> Fun with lists: length.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS LISTS DATA STRUCTURES

import unittest
import allure
from utils.log_func import print_log
from kyu_7.fun_with_lists_length.node import Node
from kyu_7.fun_with_lists_length.length import length


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Fun with lists: length')
@allure.tag('FUNDAMENTALS',
            'LISTS',
            'DATA STRUCTURES')
@allure.link(
    url='https://www.codewars.com/kata/581e476d5f59408553000a4b',
    name='Source/Kata')
# pylint: enable-msg=R0801
class LengthTestCase(unittest.TestCase):
    """Testing length function."""

    def test_length_none(self):
        """
        Testing length function where head = None.

        The method length, which accepts a linked list
        (head), and returns the length of the list.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title('Testing length function where head = None')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step('Enter test node and verify the output'):
            head = None
            self.assertEqual(length(head), 0)

    def test_length(self):
        """
        Testing length function.

        The method length, which accepts a linked list
        (head), and returns the length of the list.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title('Testing length function')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step('Enter test node and verify the output'):
            n1 = Node(1)
            n2 = Node(2, n1)
            n3 = Node(3, n2)
            head = Node(4, n3)
            expected: int = 4

            print_log(node=head, expected=expected)
            self.assertEqual(expected, length(head))
