"""
Test for -> Holiday VI - Shark Pontoon
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS NUMBERS STRINGS MATHEMATICS ALGORITHMS

import unittest
import allure
from kyu_8.holiday_vi_shark_pontoon.shark import shark


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite('Math')
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Holiday VI - Shark Pontoon')
@allure.tag('FUNDAMENTALS',
            'NUMBERS',
            'STRINGS',
            'MATHEMATICS',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/57e921d8b36340f1fd000059',
    name='Source/Kata')
class SharkTestCase(unittest.TestCase):
    """
    Testing shark function
    """

    def test_shark_alive_1(self):
        """
        Testing shark function -> positive
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing shark function (positive)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>You are given 5 variables:</p>"
            "<p>shark_distance = distance the shark needs to cover to "
            "eat you in metres,</p>"
            "<p>shark_speed = how fast it can move in metres/second,</p>"
            "<p>pontoonDistance = how far you need to swim to safety "
            "in metres,</p>"
            "<p>you_speed = how fast you can swim in metres/second,</p>"
            "<p>dolphin = a boolean, if true, you can half the swimming "
            "speed of the shark "
            "as the dolphin will attack it.</p>"
            "<p>If you make it, return \"Alive!\", if not, "
            "return \"Shark Bait!\".</p>")
        # pylint: enable=R0801
        with allure.step("Enter test data and verify the output"):
            self.assertEqual(shark(12,
                                   50,
                                   4,
                                   8,
                                   True),
                             "Alive!")

    def test_shark_alive_2(self):
        """
        Testing shark function -> positive
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing shark function (positive)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>You are given 5 variables:</p>"
            "<p>shark_distance = distance the shark needs to cover to "
            "eat you in metres,</p>"
            "<p>shark_speed = how fast it can move in metres/second,</p>"
            "<p>pontoonDistance = how far you need to swim to safety in "
            "metres,</p>"
            "<p>you_speed = how fast you can swim in metres/second,</p>"
            "<p>dolphin = a boolean, if true, you can half the swimming "
            "speed of the shark "
            "as the dolphin will attack it.</p>"
            "<p>If you make it, return \"Alive!\", if not, "
            "return \"Shark Bait!\".</p>")
        # pylint: enable=R0801
        with allure.step("Enter test data and verify the output"):
            self.assertEqual(shark(7,
                                   55,
                                   4,
                                   16,
                                   True),
                             "Alive!")

    def test_shark_bait(self):
        """
        Testing shark function -> negative
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing shark function (negative)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>You are given 5 variables:</p>"
            "<p>shark_distance = distance the shark needs to cover to "
            "eat you in metres,</p>"
            "<p>shark_speed = how fast it can move in metres/second,</p>"
            "<p>pontoonDistance = how far you need to swim to safety "
            "in metres,</p>"
            "<p>you_speed = how fast you can swim in metres/second,</p>"
            "<p>dolphin = a boolean, if true, you can half the swimming "
            "speed of the shark "
            "as the dolphin will attack it.</p>"
            "<p>If you make it, return \"Alive!\", if not, "
            "return \"Shark Bait!\".</p>")
        # pylint: enable=R0801
        with allure.step("Enter test data and verify the output"):
            self.assertEqual(shark(24,
                                   0,
                                   4,
                                   8,
                                   True),
                             "Shark Bait!")
