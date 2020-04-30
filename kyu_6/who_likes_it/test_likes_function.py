"""
Testing likes function
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS FORMATTING ALGORITHMS STRINGS

import allure
import unittest
from utils.log_func import print_log
from kyu_6.who_likes_it.likes_function import likes


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature('String')
@allure.story('Who likes it?')
@allure.tag('FUNDAMENTALS', 'FORMATTING', 'ALGORITHMS', 'STRINGS')
@allure.link(url='https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python',
             name='Source/Kata')
class LikesTestCase(unittest.TestCase):
    """
    Testing likes function

    The function should take in input array, containing the names
    of people who like an item. It must return the display text.
    For 4 or more names, the number in and 2 others simply increases.
    """

    def test_likes_function(self):
        allure.dynamic.title("Testing likes function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>The function should take in input array, containing "
                                        "the names of people who like an item. It must return the "
                                        "display text. For 4 or more names, the number in and 2 "
                                        "others simply increases.</p>")

        test_data = (
            ([], 'no one likes this'),
            (['Peter'], 'Peter likes this'),
            (['Jacob', 'Alex'], 'Jacob and Alex like this'),
            (['Max', 'John', 'Mark'], 'Max, John and Mark like this'),
            (['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this'),
        )

        with allure.step("Enter a test data and verify the expected output vs actual result"):
            for names, expected in test_data:
                actual_result = likes(names)
                print_log(exp=expected, res=actual_result)
                self.assertEqual(expected, actual_result)
