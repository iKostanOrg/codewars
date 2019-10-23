#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS ARRAYS LISTS DATA STRUCTURES

import unittest
import allure
from utils.log_func import print_log
from kyu_8.my_head_is_at_the_wrong_end.fix_the_meerkat import fix_the_meerkat


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('My head is at the wrong end!')
@pytest.mark.skip(reason="The solution is not ready")
class FixTheMeerkatTestCase(unittest.TestCase):
	"""
	Testing fix_the_meerkat function
	"""
	def test_fix_the_meerkat(self):
		pass
