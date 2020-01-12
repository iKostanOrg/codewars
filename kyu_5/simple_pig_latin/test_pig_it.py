#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS

import allure
import unittest
from utils.log_func import print_log
from kyu_5.simple_pig_latin.pig_it import pig_it


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Simple Pig Latin')
@allure.tag('ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python',
             name='Source/Kata')
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

        allure.dynamic.title("Testing pig_it function")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Enter test string and verify the output"):

            data = [
                ('Pig latin is cool', 'igPay atinlay siay oolcay'),
                ('This is my string', 'hisTay siay ymay tringsay'),
                ('Hello world !', 'elloHay orldway !'),
                ("O tempora o mores !", 'Oay emporatay oay oresmay !')
            ]

            for text, expected in data:
                print_log(expected=expected, text=text)
                self.assertEqual(expected, pig_it(text))
