"""
Test for -> Pointless Farmer.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.pointless_farmer.solution import buy_or_sell


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lista")
@allure.story('Password validator')
@allure.tag('FUNDAMENTALS',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/597ab747d1ba5b843f0000ca',
    name='Source/Kata')
# pylint: enable-msg=R0801
class PointlessFarmerTestCase(unittest.TestCase):
    """Test 'buy_or_sell' function."""

    @parameterized.expand([
        ([("apple", "orange"), ("orange", "pear"), ("apple", "pear")],
         "apple", ["buy", "buy", "sell"]),
        ([("orange", "apple"), ("orange", "pear"), ("pear", "apple")],
         "apple", ["sell", "buy", "buy"]),
        ([("apple", "orange"), ("pear", "orange"), ("apple", "pear")],
         "apple", ["buy", "sell", "sell"]),
        ([("orange", "apple"), ("pear", "orange"), ("pear", "apple")],
         "apple", ["sell", "sell", "buy"]),
        ([("orange", "apple"), ("orange", "pear"), ("apple", "pear")],
         "apple", ["sell", "buy", "sell"]),
        ([("apple", "orange"), ("pear", "orange"), ("pear", "apple")],
         "apple", ["buy", "sell", "buy"]),
        ([("apple", "orange"), ("orange", "pear"), ("pear", "apple")],
         "apple", ["buy", "buy", "buy"]),
        ([("orange", "apple"), ("pear", "orange"), ("apple", "pear")],
         "apple", ["sell", "sell", "sell"]),
        ([('Raspberry', 'Raspberry'), ('Jabuticaba', 'Raspberry'),
          ('Jabuticaba', 'Raspberry')], 'Raspberry', ['sell', 'sell', 'buy'])])
    def test_buy_or_sell_positive(self, market, harvested_fruit, expected):
        """
        Testing 'buy_or_sell' function, positive test case..

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'buy_or_sell' function -> positive.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p>"
            "When you visit the market, you are given three conversion "
            "offers, and for each conversion offer you must decide which "
            "direction to trade. A conversion offer is a pair of fruits, "
            "and to buy the second fruit for the first fruit, the action is 'buy'."
            "<br>"
            "The opposite direction is 'sell'."
            "</p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test data: {market} "
                         f"and verify the expected result: {expected}."):
            result: list = buy_or_sell(market, harvested_fruit)
            print_log(market=market,
                      harvested_fruit=harvested_fruit,
                      expected=expected,
                      result=result)
            self.assertEqual(expected, result)

    @parameterized.expand([
        ([("orange", "apple"), ("pear", "orange"), ("apple", "paer")],
          "apple", "ERROR"),
        ([('Jackfruit', 'Physalis'), ('Physalis', 'Prune'),
          ('Prune', 'Tamarind')],
         'Tamarind', 'ERROR'),
        ([('Mulberry', 'Strawberry'), ('Passionfruit', 'Mulberry'),
          ('Strawberry', 'Mulberry')],
         'Strawberry', 'ERROR'),
        ([('Cherry', 'Cucumber'), ('Cherry', 'Cherry'), ('Cucumber', 'Ugli fruit')],
         'Boysenberry', 'ERROR'),
        ([('Jackfruit', 'Purple mangosteen'), ('Purple mangosteen', 'Jackfruit'),
          ('Purple mangosteen', 'Jackfruit')],
         'Purple mangosteen', 'ERROR')])
    def test_buy_or_sell_negative(self, market, harvested_fruit, expected):
        """
        Testing 'buy_or_sell' function, negative test case.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'buy_or_sell' function -> negative.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p>"
            "If it is not possible to end up with the original kind "
            "of fruit again after the three conversions, return \"ERROR\" "
            "instead of the list of actions."
            "</p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test data: {market} "
                         f"and verify the expected result: {expected}."):
            result: list = buy_or_sell(market, harvested_fruit)
            print_log(market=market,
                      harvested_fruit=harvested_fruit,
                      expected=expected,
                      result=result)
            self.assertEqual(expected, result)



