"""
Test for -> Disemvowel Trolls
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS, STRINGS, REGULAR EXPRESSIONS,
# DECLARATIVE PROGRAMMING, ADVANCED LANGUAGE FEATURES

import unittest
import allure
from utils.log_func import print_log
from kyu_7.disemvowel_trolls.disemvowel_trolls import disemvowel


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Disemvowel Trolls')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES')
@allure.link(
    url='https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class DisemvowelTestCase(unittest.TestCase):
    """
    Testing disemvowel function
    """
    def test_disemvowel(self):
        """
        The string "This website is for losers LOL!"
        should become "Ths wbst s fr lsrs LL!"
        :return:
        """
        global input_data
        allure.dynamic.title("a and b are equal")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        test_data: tuple = (
            ("This website is for losers LOL!",
             "Ths wbst s fr lsrs LL!"),
            ("No offense but, Your writing is among the worst I've ever read",
             "N ffns bt, Yr wrtng s mng th wrst 'v vr rd"),
            ("What are you, a communist?",
             "Wht r y,  cmmnst?"),
            ("IeiIvp EIfgoIh,d(kaM]A>EuiGzEooOoW oK f&uswtee pKAUI<ZuuEi\\g)aIAOU !_Lu",
             "vp fgh,d(kM]>GzW K f&swt pK<Z\\g) !_L"),
            ("Nt/I'OvegOI*UdAaEobaE{Gi} I^@*Ieua\\uU}d%AoUII}ue>*"
             "]IkEI GqrjOal`E\" eeAeSuaTdAu-FISac",
             "Nt/'vg*db{G} ^@*\\}d%}>*]k Gqrjl`\" STd-FSc"))

        for data in test_data:
            input_data, expected = data

            with allure.step("Enter test data ans assert the result"):
                print_log(input=input_data,
                          expected=expected)
                self.assertEqual(disemvowel(input_data),
                                 expected)
