#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ARRAYS LOOPS CONTROL FLOW

import unittest
import allure
from utils.log_func import print_log
from kyu_8.wolf_in_sheep_clothing.wolf_in_sheep_clothing import warn_the_sheep


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Control Flow")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('A wolf in sheep\'s clothing')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class WarnTheSheepTestCase(unittest.TestCase):
    """
    Testing warn_the_sheep function
    """

    def test_warn_the_sheep_wolf_at_start(self):
        """
        If the wolf is the closest animal to you,
        return "Pls go away and stop eating my sheep".
        :return:
        """

        allure.dynamic.title("Wolf at the beginning of the queue")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        lst = ['wolf', 'sheep', 'sheep',
               'sheep', 'sheep', 'sheep',
               'sheep']
        expected = 'Oi! Sheep number 6! You are ' \
                   'about to be eaten by a wolf!'

        print_log(list=lst, expected=expected)
        self.assertEqual(warn_the_sheep(lst), expected)

    def test_warn_the_sheep_wolf_in_middle(self):
        """
        If the wolf is the closest animal to you,
        return "Pls go away and stop eating my sheep".
        :return:
        """

        allure.dynamic.title("Wolf in the middle of the queue")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        # 1
        lst = ['sheep', 'sheep', 'sheep',
               'sheep', 'sheep', 'wolf',
               'sheep', 'sheep']
        expected = 'Oi! Sheep number 2! You are about ' \
                   'to be eaten by a wolf!'

        print_log(list=lst, expected=expected)
        self.assertEqual(warn_the_sheep(lst), expected)

        # 2
        lst = ['sheep', 'wolf', 'sheep',
               'sheep', 'sheep', 'sheep',
               'sheep']
        expected = 'Oi! Sheep number 5! You are ' \
                   'about to be eaten by a wolf!'

        print_log(list=lst, expected=expected)
        self.assertEqual(warn_the_sheep(lst), expected)

        # 3
        lst = ['sheep', 'wolf', 'sheep']
        expected = 'Oi! Sheep number 1! You are ' \
                   'about to be eaten by a wolf!'

        print_log(list=lst, expected=expected)
        self.assertEqual(warn_the_sheep(lst), expected)

    def test_warn_the_sheep_wolf_at_end(self):
        """
        If the wolf is not the closest animal to you,
        return "Oi! Sheep number N! You are about to be eaten by a wolf!"
        where N is the sheep's position in the queue.
        :return:
        """

        allure.dynamic.title("Wolf at the end of the queue")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        lst = ['sheep', 'sheep', 'wolf']
        expected = 'Pls go away and stop eating my sheep'

        print_log(list=lst, expected=expected)
        self.assertEqual(warn_the_sheep(lst), expected)
