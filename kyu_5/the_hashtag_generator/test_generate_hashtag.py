"""
Test for ->  'generate_hashtag' function.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_5.the_hashtag_generator.hashtag_generator \
    import generate_hashtag


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('The Hashtag Generator')
@allure.tag('ALGORITHMS',
            'SORTING')
@allure.link(
    url='https://www.codewars.com/kata/52449b062fb80683ec000024',
    name='Source/Kata')
# pylint: enable-msg=R0801
class GenerateHashtagTestCase(unittest.TestCase):
    """Testing generate_hashtag function."""

    @parameterized.expand(
        [('', False,
           'Expected an empty string to return False'),
          ('Codewars',
           '#Codewars',
           'Should handle a single word.'),
          ('Codewars      ',
           '#Codewars',
           'Should handle trailing whitespace.'),
          ('Codewars Is Nice',
           '#CodewarsIsNice',
           'Should remove spaces.'),
          ('codewars is nice',
           '#CodewarsIsNice',
           'Should capitalize first letters of words.'),
          ('CodeWars is nice',
           '#CodewarsIsNice',
           'Should capitalize all letters of words - '
           'all lower case but the first.'),
          ('c i n',
           '#CIN',
           'Should capitalize first letters of words even '
           'when single letters.'),
          ('codewars  is  nice',
           '#CodewarsIsNice',
           'Should deal with unnecessary middle spaces.'),
          ('Loooooooooooooooooooooooooooooooooooo'
           'oooooooooooooooooooooooooooooooooooooo'
           'oooooooooooooooooooooooooooooooooooooo'
           'ooooooooooooooooooooooooooooooooooooo'
           'oooooong Cat', False,
           'Should return False if the final word is '
           'longer than 140 chars.')])
    def test_generate_hashtag(self, string, expected, message):
        """
        Testing 'generate_hashtag' function with various test data.

        :return:
        """
        allure.dynamic.title("Testing 'generate_hashtag' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src='
            '"https://www.codewars.com/users/myFirstCode/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The function should do the following:"
            "<br/>1. It must start with a hashtag (#)."
            "<br/>2. "
            "All words must have their first letter capitalized."
            "<br/>3. "
            "If the final result is longer than 140 chars it "
            "must return false."
            "<br/>4. "
            "If the input or the result is an empty string it "
            "must return false."
            "</p>")

        with allure.step("Enter a test string and verify the output:"):
            actual_result = generate_hashtag(string)
            print_log(string=string,
                      message=message,
                      expected=expected,
                      actual_result=actual_result)
            self.assertEqual(expected, actual_result, message)
