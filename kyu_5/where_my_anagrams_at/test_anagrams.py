#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS STRINGS

import unittest
import allure
from kyu_5.where_my_anagrams_at.anagrams import anagrams
from utils.log_func import print_log


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Where my anagrams at?')
@allure.tag('ALGORITHMS', 'STRINGS')
@allure.link(url='https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python',
             name='Source/Kata')
class AnagramsTestCase(unittest.TestCase):
    """
    Testing anagrams function
    """

    def test_anagrams(self):
        """
        Test a function that will find all the anagrams of a word from a list.
        You will be given two inputs a word and an array with words. You should
        return an array of all the anagrams or an empty array if there are none.

        For example:

        anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
        anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
        anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
        :return:
        """

        allure.dynamic.title("Testing anagrams function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter test data (list of strings)"
                         " and verify the output"):
            test_data = [
                ('abba', ['aabb', 'abcd', 'bbaa', 'dada'], ['aabb', 'bbaa']),
                ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'], ['carer', 'racer'])
            ]

            for d in test_data:
                string = d[0]
                array = d[1]
                expected = d[2]
                print_log(array=array, expected=expected)
                self.assertListEqual(expected, anagrams(string, array))
