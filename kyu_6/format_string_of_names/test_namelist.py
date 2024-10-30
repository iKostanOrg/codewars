"""
Test for -> Format a string of names like \'Bart, Lisa & Maggie\'.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS FORMATTING ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.format_string_of_names.solution import namelist

# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Format a string of names like \'Bart, Lisa & Maggie\'.')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'FORMATTING',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/53368a47e38700bd8300030d',
    name='Source/Kata')
# pylint: enable-msg=R0801
class NamelistTestCase(unittest.TestCase):
    """
    Testing namelist function
    """
    def test_namelist(self):
        """
        Test namelist

        Given:
        an array containing hashes of names

        Return:
        a string formatted as a list of names separated by commas
        except for the last two names, which should be separated
        by an ampersand.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("String with no duplicate chars")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Should a string formatted as a list of names separated "
            "by commas except for the last two names, which should be "
            "separated by an ampersand.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},
              {'name': 'Homer'}, {'name': 'Marge'}],
             'Bart, Lisa, Maggie, Homer & Marge',
             "Must work with many names"),
            ([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}],
             'Bart, Lisa & Maggie',
             "Must work with many names"),
            ([{'name': 'Bart'}, {'name': 'Lisa'}],
             'Bart & Lisa',
             "Must work with two names"),
            ([{'name': 'Bart'}],
             'Bart',
             "Wrong output for a single name"),
            ([],
             '',
             "Must work with no names"))

        for names, expected, message in test_data:
            result: str = namelist(names)
            print_log(names=names,
                      expected=expected,
                      result=result,
                      message=message)
            self.assertEqual(expected, result)
