#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS LISTS DATA STRUCTURES

import allure
import unittest
from utils.log_func import print_log
from kyu_7.fun_with_lists_length.node import Node
from kyu_7.fun_with_lists_length.length import length


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Fun with lists: length')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class LengthTestCase(unittest.TestCase):
    """
    Testing length function
    """
    def test_length_none(self):
        """
        Testing length function
        where head = None

        The method length, which accepts a linked list
        (head), and returns the length of the list.
        :return:
        """

        allure.dynamic.title('Testing length function where head = None')
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step('Enter test node and verify the output'):

            head = None
            self.assertEqual(length(head), 0)

    def test_length(self):
        """
        Testing length function

        The method length, which accepts a linked list
        (head), and returns the length of the list.
        :return:
        """

        allure.dynamic.title('Testing length function')
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step('Enter test node and verify the output'):

            n1 = Node(1)
            n2 = Node(2, n1)
            n3 = Node(3, n2)
            head = Node(4, n3)
            expected = 4

            print_log(node=head, expected=expected)
            self.assertEqual(expected, length(head))
