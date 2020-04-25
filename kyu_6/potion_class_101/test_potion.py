#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS

import unittest
import allure
from kyu_6.potion_class_101.potion import Potion


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite('Classes')
@allure.sub_suite("Unit Tests")
@allure.feature('Algorithms')
@allure.story('Potion Class 101')
@allure.tag('ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/5981ff1daf72e8747d000091/train/python',
             name='Source/Kata')
class PotionTestCase(unittest.TestCase):
    def test_potion(self):
        allure.dynamic.title("Testing Potion class")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Test Potion class that mix between 2 RGB colors.</p>")

        potions = [
            Potion((153, 210, 199), 32),
            Potion((135, 34, 0), 17),
            Potion((18, 19, 20), 25),
            Potion((174, 211, 13), 4),
            Potion((255, 23, 148), 19),
            Potion((51, 102, 51), 6)
        ]

        a = potions[0].mix(potions[1])
        b = potions[0].mix(potions[2]).mix(potions[4])
        c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
        d = potions[0].mix(potions[1]).mix(
            potions[2]).mix(potions[4]).mix(potions[5])
        e = potions[0].mix(potions[1]).mix(potions[2]).mix(
            potions[3]).mix(potions[4]).mix(potions[5])

        with allure.step("Mix between RGB colors and verify the output"):
            self.assertEqual((147, 149, 130), a.color)
            self.assertEqual(49, a.volume)

            self.assertEqual((135, 101, 128), b.color)
            self.assertEqual(76, b.volume)

            self.assertEqual((74, 50, 18), c.color)
            self.assertEqual(52, c.volume)

            self.assertEqual((130, 91, 102), d.color)
            self.assertEqual(99, d.volume)

            self.assertEqual((132, 96, 99), e.color)
            self.assertEqual(103, e.volume)
