"""
Test for -> Vasya - Clerk.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS GAMES

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.vasya_clerk.tickets import tickets


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Vasya - Clerk')
@allure.tag('FUNDAMENTALS',
            'MATHEMATICS',
            'ALGORITHMS',
            'NUMBERS',
            'GAMES')
@allure.link(
    url='https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8',
    name='Source/Kata')
class TicketsTestCase(unittest.TestCase):
    """Testing tickets function."""

    @parameterized.expand([
        ([25, 25, 50], 'YES', 'All good'),
        ([25, 100], 'NO',
         'Vasya will not have enough money '
         'to give change to 100 dollars'),
        ([25, 25, 50, 50, 100], 'NO',
         'Vasya will not have the right bills '
         'to give 75 dollars of change (you can\'t '
         'make two bills of 25 from one of 50)'),
        ([25, 50, 25, 100, 25, 25, 50, 100, 25, 25, 25,
          100, 25, 25, 50, 100, 25, 50, 25, 100, 25, 50,
          50, 50], 'NO', 'N/A'),
        ([25, 25, 25, 100, 25, 25, 25, 100, 25,
          25, 50, 100, 25, 25, 50, 100, 50, 50],
         'NO', 'N/A')])
    def test_tickets(self, arr, expected, msg):
        """
        Testing tickets function with various test inputs.

        The new "Avengers" movie has just been released!
        There are a lot of people at the cinema box office
        standing in a huge line. Each of them has a single
        100, 50 or 25 dollar bill. An "Avengers" ticket
        costs 25 dollars.

        Vasya is currently working as a clerk.
        He wants to sell a ticket to every single person
        in this line.

        Can Vasya sell a ticket to every person and give change
        if he initially has no money and sells the tickets strictly
        in the order people queue?

        The function should return YES, if Vasya can sell
        a ticket to every person and give change with the
        bills he has at hand at that moment. Otherwise return NO.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing tickets function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter test input (list) and verify the output"):
            print_log(people=arr, expected=expected, msg=msg)
            self.assertEqual(expected, tickets(arr), msg)
