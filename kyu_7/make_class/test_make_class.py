#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS GAMES OBJECT-ORIENTED PROGRAMMING

import unittest
import allure
from utils.log_func import print_log
from kyu_7.make_class.animal import Animal
from kyu_7.make_class.make_class import make_class


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("OOP")
@allure.sub_suite("Unit Tests")
@allure.feature("Classes")
@allure.story('Make Class')
@pytest.mark.skip(reason="The solution is not ready")
class MakeClassTestCase(unittest.TestCase):
	"""
	Testing make_class function
	"""

	def test_make_class(self):
		"""
		Testing make_class function
		:return:
		"""

		allure.dynamic.title("Testing make_class function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Test class creation by using a function"):

			Animel = make_class("name", "species", "age", "health", "weight", "color")

			dog1 = Animal("Bob", "Dog", 5, "good", "50lb", "brown")
			dog2 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")

			self.assertEqual(dog1.name, dog2.name)
			self.assertEqual(dog1.species, dog2.species)
			self.assertEqual(dog1.age, dog2.age)
			self.assertEqual(dog1.health, dog2.health)
			self.assertEqual(dog1.weight, dog2.weight)
			self.assertEqual(dog1.color, dog2.color)
