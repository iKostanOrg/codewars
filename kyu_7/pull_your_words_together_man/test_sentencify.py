"""
Test for -> Pull your words together, man!
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS FORMATTING

import unittest
import allure
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
    url='https://www.codewars.com/kata/59ad7d2e07157af687000070/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SentencifyTestCase(unittest.TestCase):
    """
    Testing 'sentencify' function
    """

    def test_sentencify(self):
        """
        Testing 'sentencify' function.

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
        with allure.step("Enter a list of strings"
                         " and verify the result"):
            test_data = [
                (["i", "am", "an", "AI"],
                 "I am an AI."),
                (["yes"],
                 "Yes."),
                (["FIELDS", "of", "CORN", "are", "to", "be", "sown"],
                 "FIELDS of CORN are to be sown."),
                (["i'm", "afraid", "I", "can't", "let", "you", "do", "that"],
                 "I'm afraid I can't let you do that."),
            ]

            for words, expected in test_data:
                print_log(expected=expected,
                          words=words)

                self.assertEqual(expected,
                                 sentencify(words))
