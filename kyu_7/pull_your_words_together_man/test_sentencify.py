"""
Test for -> Pull your words together, man!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS FORMATTING

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.pull_your_words_together_man.sentencify import sentencify


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Pull your words together, man!')
@allure.tag('ALGORITHMS',
            'STRINGS',
            'FORMATTING')
@allure.link(
    url='https://www.codewars.com/kata/59ad7d2e07157af687000070',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SentencifyTestCase(unittest.TestCase):
    """Testing 'sentencify' function."""

    @parameterized.expand([
        (["i", "am", "an", "AI"],
         "I am an AI."),
        (["yes"],
         "Yes."),
        (["FIELDS", "of", "CORN", "are", "to", "be", "sown"],
         "FIELDS of CORN are to be sown."),
        ([r"i'm", "afraid", "I", "can't", "let", "you", "do", "that"],
         r"I'm afraid I can't let you do that.")])
    def test_sentencify(self, words, expected):
        """
        Testing 'sentencify' function with various test data.

        The function should:
        1. Capitalise the first letter of the first word.
        2. Add a period (.) to the end of the sentence.
        3. Join the words into a complete string, with spaces.
        4. Do no other manipulation on the words.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'solution' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter a list of strings: {words}"
                         f" and verify the expected result: {expected}."):
            print_log(expected=expected, words=words)
            self.assertEqual(expected, sentencify(words))
