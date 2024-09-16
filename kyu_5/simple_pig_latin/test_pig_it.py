"""
Test for -> Simple Pig Latin
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_5.simple_pig_latin.pig_it import pig_it


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Simple Pig Latin')
@allure.tag('ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python',
             name='Source/Kata')
# pylint: enable-msg=R0801
class PigItTestCase(unittest.TestCase):
    """
    Testing pig_it function
    """

    def test_pig_it(self):
        """
        Testing pig_it function

        The function should mpve the first letter of each
        word to the end of it, then add "ay" to the end
        of the word. Leave punctuation marks untouched.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing pig_it function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter test string and verify the output"):
            test_data = [
                ('Pig latin is cool', 'igPay atinlay siay oolcay'),
                ('This is my string', 'hisTay siay ymay tringsay'),
                ('Hello world !', 'elloHay orldway !'),
                ("O tempora o mores !", 'Oay emporatay oay oresmay !')
            ]

            for text, expected in test_data:
                print_log(expected=expected, text=text)
                self.assertEqual(expected, pig_it(text))
