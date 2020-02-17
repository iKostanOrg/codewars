#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS BOOLEANS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.set_alarm.set_alarm import set_alarm


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Boolean")
@allure.story('L1: Set Alarm')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class SetAlarmTestCase(unittest.TestCase):
    """
    Testing set_alarm function
    """

    def test_set_alarm(self):
        """
        Testing set_alarm function with various test inputs.

        The function should return true if you are employed
        and not on vacation (because these are the circumstances
        under which you need to set an alarm). It should return
        false otherwise.

        Examples:

        setAlarm(true, true) -> false
        setAlarm(false, true) -> false
        setAlarm(false, false) -> false
        setAlarm(true, false) -> true
        :return:
        """

        allure.dynamic.title("Testing set_alarm function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter test data and verify the output"):

            test_data = [
                ((True, True),
                 False,
                 "Fails when input is True, True"),
                ((False, True),
                 False,
                 "Fails when input is False, True"),
                ((False, False),
                 False,
                 "Fails when input is False, False"),
                ((True, False),
                 True,
                 "Fails when input is True, False"),
            ]

            for test_input, expected, msg in test_data:

                employed = test_input[0]
                vacation = test_input[1]

                print_log(employed=employed,
                          vacation=vacation,
                          expected=expected)

                self.assertEqual(expected,
                                 set_alarm(employed, vacation),
                                 msg)
