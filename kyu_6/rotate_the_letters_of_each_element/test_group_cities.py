#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# PUZZLES LISTS DATA STRUCTURES STRINGS SORTING ALGORITHMS

import allure
import unittest
from utils.log_func import print_log
from kyu_6.rotate_the_letters_of_each_element.group_cities import group_cities


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('ROTATE THE LETTERS OF EACH ELEMENT')
@allure.tag('PUZZLES', 'LISTS', 'DATA STRUCTURES', 'STRINGS', 'SORTING ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/5e98712b7de14f0026ef1cc1/train/python',
             name='Source/Kata')
class GroupCitiesTestCase(unittest.TestCase):
    """
    Testing 'group_cities' function
    """

    def test_group_cities(self):
        """
        Test that a function that given a sequence of strings, groups the elements
        that can be obtained by rotating others, ignoring upper or lower cases.

        In the event that an element appears more than once in the input sequence,
        only one of them will be taken into account for the result, discarding the rest.
        :return:
        """

        allure.dynamic.title("Testing the 'group_cities' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Test that a function that given a sequence of strings, "
                                        "groups the elements that can be obtained by rotating others, "
                                        "ignoring upper or lower cases. In the event that an element "
                                        "appears more than once in the input sequence, only one of them "
                                        "will be taken into account for the result, discarding the rest.</p>")

        test_data = (
            (['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'],
             [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']]),
            (['Tokyo', 'London', 'Rome', 'Donlon'],
             [['Donlon', 'London'], ['Rome'], ['Tokyo']]),
            (['Rome', 'Rome', 'Rome', 'Donlon', 'London'],
             [['Donlon', 'London'], ['Rome']]),
            (['Ab', 'Aa'],
             [['Aa'], ['Ab']]),
            ([], []),
            (['Bb', 'Cbacb', 'Bacaa', 'C', 'A', 'Bccab', 'Ba'],
             [['A'], ['Ba'], ['Bacaa'], ['Bb'], ['Bccab'], ['C'], ['Cbacb']]),
            (['Abaa', 'Bc', 'Ca', 'Bbcac', 'Caca', 'Ba', 'Cab', 'Cbbcc', 'A', 'C', 'Cba', 'Baa', 'Abc'],
             [['Abc', 'Cab'], ['A'], ['Abaa'], ['Ba'], ['Baa'], ['Bbcac'], ['Bc'],
              ['C'], ['Ca'], ['Caca'], ['Cba'], ['Cbbcc']]),
            (['Ab', 'Aba', 'A', 'Bbab', 'Baa', 'B', 'Cac', 'A', 'Baa', 'Bbbb', 'Ac', 'Bcbaa', 'Ab'],
             [['Aba', 'Baa'], ['A'], ['Ab'], ['Ac'], ['B'], ['Bbab'], ['Bbbb'], ['Bcbaa'], ['Cac']])
        )

        for data in test_data:
            seq: list = data[0]
            expected: list = data[1]
            actual_result: list = group_cities(seq)

            with allure.step("Enter a list and verify the "
                             "expected output vs actual result"):
                print_log(seq=seq,
                          expected=expected,
                          result=actual_result)

                self.assertListEqual(expected, actual_result)
