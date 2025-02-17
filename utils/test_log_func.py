"""
Test for -> print_log function.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import unittest
from unittest.mock import patch
from utils.log_func import print_log


class LogFuncTestCase(unittest.TestCase):

	@patch('builtins.print')
	def test_log_func(self, mock_print):

		print_log(str="Hello World!")
		mock_print.assert_called_with('\nLOG =>\nstr: Hello World!\n')


if __name__ == '__main__':
	unittest.main()
