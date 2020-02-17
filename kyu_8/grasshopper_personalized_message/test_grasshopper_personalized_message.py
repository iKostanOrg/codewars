#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS CONDITIONAL STATEMENTS CONTROL FLOW

import unittest
import allure
from utils.log_func import print_log
from kyu_8.grasshopper_personalized_message.grasshopper_personalized_message import greet


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Control Flow")
@allure.sub_suite("Unit Tests")
@allure.feature("Conditions")
@allure.story('Personalized greeting')
@allure.tag('FUNDAMENTALS', 'CONDITIONAL STATEMENTS', 'CONTROL FLOW')
@allure.link(url='https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python',
             name='Source/Kata')
class GreetTestCase(unittest.TestCase):
    """
    Testing greet function
    """

    def test_greet(self):
        """
        Use conditionals to to verify that greet
        function returns the proper message.
        :return:
        """

        allure.dynamic.title("Verify that greet function "
                             "returns the proper message")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        # name equals owner
        with allure.step("Test name equals owner"):
            name = 'Daniel'
            owner = 'Daniel'
            expected = 'Hello boss'

            print_log(name=name,
                      owner=owner,
                      expected=expected)

        self.assertEqual(greet(name, owner), expected)

        # otherwise
        with allure.step("Test name not equals owner"):
            name = 'Greg'
            owner = 'Daniel'
            expected = 'Hello guest'

            print_log(name=name,
                      owner=owner,
                      expected=expected)

        self.assertEqual(greet(name, owner), expected)
