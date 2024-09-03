"""
Test for -> Alphabet wars - nuclear strike
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS
# DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES

import unittest
import allure
from utils.log_func import print_log
from kyu_5.alphabet_wars_nuclear_strike.alphabet_war import alphabet_war


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Alphabet wars - nuclear strike')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'REGULAR',
            'EXPRESSIONS',
            'DECLARATIVE',
            'PROGRAMMING',
            'ADVANCED',
            'LANGUAGE',
            'FEATURES')
@allure.link(url='https://www.codewars.com/kata/alphabet-wars-nuclear-strike/train/python',
             name='Source/Kata')
# pylint: enable-msg=R0801
class AlphabetWarTestCase(unittest.TestCase):
    """
    Testing alphabet_war function
    """

    def test_alphabet_war(self):
        """
        Testing alphabet_war function

        Introduction
        There is a war and nobody knows - the alphabet war!
        The letters hide in their nuclear shelters. The
        nuclear strikes hit the battlefield and killed a
        lot of them.

        Task
        Write a function that accepts battlefield string
        and returns letters that survived the nuclear strike.

        1. The battlefield string consists of only small letters, #,[ and ].

        2. The nuclear shelter is represented by square brackets [].
        The letters inside the square brackets represent letters
        inside the shelter.

        3. The # means a place where nuclear strike hit the battlefield.
        If there is at least one # on the battlefield, all letters outside
        of shelter die. When there is no any # on the battlefield, all letters
        survive (but do not expect such scenario too often ;-P ).

        4. The shelters have some durability. When 2 or more # hit close to
        the shelter, the shelter is destroyed and all letters inside evaporate.
        The 'close to the shelter' means on the ground between the shelter and
        the next shelter (or beginning/end of battlefield). The below samples
        make it clear for you.
        :return:
        """

        allure.dynamic.title("Testing alphabet_war function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a function that accepts battlefield string and "
            "returns letters that survived the nuclear strike.</p>")

        test_data = [
            ('[a]#[b]#[c]', 'ac'),
            ('[a]#b#[c][d]', 'd'),
            ('[a][b][c]', 'abc'),
            ('##a[a]b[c]#', 'c'),
            ('abde[fgh]ijk', 'abdefghijk'),
            ('ab#de[fgh]ijk', 'fgh'),
            ('ab#de[fgh]ij#k', ''),
            ('##abde[fgh]ijk', ''),
            ('##abde[fgh]', ''),
            ('##abcde[fgh]', ''),
            ('abcde[fgh]', 'abcdefgh'),
            ('##abde[fgh]ijk[mn]op', 'mn'),
            ('#abde[fgh]i#jk[mn]op', 'mn'),
            ('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#', 'abijk'),
        ]

        for battlefield, expected in test_data:
            result = alphabet_war(battlefield)

            with allure.step(f"Enter test string ({battlefield}) "
                             f"and verify the output ({result}) "
                             f"vs expected ({expected})"):
                print_log(battlefield=battlefield,
                          result=result,
                          expected=expected)

                self.assertEqual(expected, result)
