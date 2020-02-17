#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, STRINGS, REGULAR EXPRESSIONS, DECLARATIVE PROGRAMMING, ADVANCED LANGUAGE FEATURES

import unittest
import allure
from utils.log_func import print_log
from kyu_7.disemvowel_trolls.disemvowel_trolls import disemvowel


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Disemvowel Trolls')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES')
@allure.link(url='',
             name='Source/Kata')
class DisemvowelTestCase(unittest.TestCase):
    """
    Testing disemvowel function
    """

    def test_disemvowel(self):
        """
        The string "This website is for losers LOL!"
        should become "Ths wbst s fr lsrs LL!"
        :return:
        """

        allure.dynamic.title("a and b are equal")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Assert the result"):
            input_data = "This website is for losers LOL!"
            expected = "Ths wbst s fr lsrs LL!"

            print_log(input=input_data,
                      expected=expected)

            self.assertEqual(disemvowel(input_data),
                             expected)
