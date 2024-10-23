"""
Test for -> DefaultList
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS CLASSES BASIC LANGUAGE FEATURES
# OBJECT-ORIENTED PROGRAMMING

import unittest
import allure
from utils.log_func import print_log
from kyu_6.default_list.default_list import DefaultList


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Object-Oriented Programming")
@allure.sub_suite("Unit Tests")
@allure.feature("Classes")
@allure.story('DefaultList')
@allure.tag('FUNDAMENTALS',
            'CLASSES',
            'BASIC LANGUAGE FEATURES',
            'OBJECT-ORIENTED PROGRAMMING')
@allure.link(
    url='https://www.codewars.com/kata/5e882048999e6c0023412908',
    name='Source/Kata')
class DefaultListTestCase(unittest.TestCase):
    """
    Testing 'DefaultList' class

    Your job is to create a class (or a function which
    returns an object) called DefaultList. The class will
    have two parameters to be given: a list, and a default
    value. The list will obviously be the list that
    corresponds to that object. The default value will be
    returned any time an index of the list is called in the
    code that would normally raise an error
    (i.e. i > len(list) - 1 or i < -len(list)).

    This class must also support the regular list functions
    extend, append, insert, remove, and pop.
    """

    def test_default_list_basic(self):
        """
        Testing 'DefaultList' class: __getitem__

        Called to implement evaluation of self[key]. For sequence
        types, the accepted keys should be integers and slice objects.
        Note that the special interpretation of negative indexes
        (if the class wishes to emulate a sequence type) is up to the
        __getitem__() method.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Testing 'DefaultList' class: __getitem__")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing __getitem__ method.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Create a list"):
            lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

        with allure.step("Get list item by index and verify the results"):
            i: int = 1
            expected = 3
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected, actual=actual)
            self.assertEqual(expected, actual)

        with allure.step("Get list item by index and verify the results"):
            i = 333000
            expected_str = 'def'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected, actual)

        with allure.step("Get list item by index and verify the results"):
            i = 23
            expected_str = 'def'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected, actual)

    def test_default_list_extend(self):
        """
        Testing 'DefaultList' class: extend
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'DefaultList' class: extend")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing extend method.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Create a list"):
            lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

        with allure.step("Extend the list list"):
            lst.extend([3, 23, 'hello', 'lists', 'word', 344])

        with allure.step("Get list item by index and verify the results"):
            i = 9
            expected_str = 'lists'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected_str, actual)

        with allure.step("Get list item by index and verify the results"):
            i = 11
            expected = 344
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected, actual=actual)
            self.assertEqual(expected, actual)

        with allure.step("Get list item by index and verify the results"):
            i = 12
            expected_str = 'def'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected, actual)

    def test_default_list_append(self):
        """
        Testing 'DefaultList' class: append
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'DefaultList' class: append")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing append method.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Create a list"):
            lst = DefaultList(
                [1, 3, 4, 7, 2, 34, 3, 23, 'hello', 'lists', 'word', 344],
                'def')

        with allure.step("Append the list"):
            lst.append(233344455)

        with allure.step("Get list item by index and verify the results"):
            i = 12
            expected = 233344455
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected, actual=actual)
            self.assertEqual(expected, actual)

        with allure.step("Get list item by index and verify the results"):
            i = 100
            expected_str = 'def'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected, actual)

    def test_default_list_remove(self):
        """
        Testing 'DefaultList' class: remove
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'DefaultList' class: remove")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing remove method.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Create a list"):
            lst = DefaultList(
                [1, 3, 4, 7, 2, 34, 3, 23, 'hello', 'lists', 'word', 344, 233344455],
                'def')

        with allure.step("Remove items from the list"):
            lst.remove(2)
            lst.remove(1)
            lst.remove(3)

        with allure.step("Get list item by index and verify the results"):
            i = 1
            expected = 7
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected, actual=actual)
            self.assertEqual(expected, actual)

        with allure.step("Get list item by index and verify the results"):
            i = 9
            expected = 233344455
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected, actual=actual)
            self.assertEqual(expected, actual)

    def test_default_list_insert(self):
        """
        Testing 'DefaultList' class: insert
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'DefaultList' class: insert")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing insert method.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Create a list"):
            lst = DefaultList(
                [4, 7, 34, 3, 23, 'hello', 'lists', 'word', 344, 233344455],
                'def')

        with allure.step("Insert items to the list"):
            lst.insert(-3, 34.34)

        with allure.step("Get list item by index and verify the results"):
            i = 8
            expected_str = 'word'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected_str, actual)

        with allure.step("Get list item by index and verify the results"):
            i = 10
            expected = 233344455
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected, actual=actual)
            self.assertEqual(expected, actual)

    def test_default_list_pop(self):
        """
        Testing 'DefaultList' class: pop
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'DefaultList' class: pop")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing pop method.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Create a list"):
            lst = DefaultList(
                [4, 7, 34, 3, 23, 'hello', 'lists', 'word', 344, 233344455],
                'def')

        with allure.step("Pop an item and verify the result"):
            i = 5
            expected_str = 'hello'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected_str, actual)

        with allure.step("Pop an item and verify the result"):
            i = 6
            expected_str = 'lists'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected_str, actual)

        with allure.step("Pop an un-existing item and verify the result"):
            i = 45
            expected_str = 'def'
            actual = lst[i]
            print_log(lst=lst, i=i, expected=expected_str, actual=actual)
            self.assertEqual(expected_str, actual)
