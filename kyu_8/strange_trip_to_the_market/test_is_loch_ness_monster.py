"""
Test for -> A Strange Trip to the Market.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# REGULAR EXPRESSIONS STRINGS FUNDAMENTALS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.strange_trip_to_the_market.solution import is_loch_ness_monster


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Strings")
@allure.story('L1: Set Alarm')
@allure.tag('FUNDAMENTALS',
            'REGULAR EXPRESSIONS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/55ccdf1512938ce3ac000056',
    name='Source/Kata')
# pylint: enable=R0801
class MyTestCase(unittest.TestCase):
    """Test 'is_loch_ness_monster' function."""

    @parameterized.expand([
        ("Your girlscout cookies are ready to ship. "
         "Your total comes to tree fiddy", True),
        ("Howdy Pardner. Name's Pete Lexington. I reckon "
         "you're the kinda stiff who carries about tree "
         "fiddy?", True),
        ("I'm from Scottland. I moved here to be with my "
         "family sir. Please, $3.50 would go a long way "
         "to help me find them", True),
        ("Yo, I heard you were on the lookout for Nessie. "
         "Let me know if you need assistance.", False),
        ("I will absolutely, positively, never give that darn "
         "Loch Ness Monster any of my three dollars and fifty "
         "cents", False),
        ("Did I ever tell you about my run with that paleolithic "
         "beast? He tried all sorts of ways to get at my three "
         "dolla and fitty cent? I told him 'this is MY 4 dolla!'. "
         "He just wouldn't listen.", False),
        ("Hello, I come from the year 3150 to bring you good news!",
         False),
        ("By 'tree fiddy' I mean 'three fifty'", True),
        ("I will be at the office by 3:50 or maybe a bit earlier, "
         "but definitely not before 3, to discuss with 50 clients",
         False),
        ("", False)])
    def test_is_loch_ness_monster(self, string, expected):
        """
        Test 'is_loch_ness_monster' function with various test data.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing 'is_loch_ness_monster' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "The function should return true if you're talking with "
            "'The Loch Ness Monster', false otherwise."
            "otherwise."
            '</p>'
            "<p>"
            "There are only 2 guaranteed ways to tell if you are "
            "speaking to The 'Loch Ness Monster':<br>"
            "A) it is a 400 foot tall beast from the paleolithic era;<br>"
            "B) it will ask you for tree fiddy."
            "</p>")
        # pylint: enable=R0801
        with allure.step(f"Enter test string: {string} "
                         f"and verify the expected output: {expected}."):
            result: bool = is_loch_ness_monster(string)
            print_log(string=string, expected=expected, result=result)
            self.assertEqual(expected, result)  # add assertion here
