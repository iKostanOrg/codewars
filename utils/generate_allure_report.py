#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import platform
from utils.copy_allure_history import copy_allure_history


if __name__ == "__main__":

	CURRENT_DIR: str = str(os.getcwd()).replace("utils", '')
	PATH_RESULTS: str = ''
	PATH_REPORT: str = ''

	if platform.system() == 'Linux':
		PATH_RESULTS = CURRENT_DIR + 'allure-results/'
		PATH_REPORT = CURRENT_DIR + 'allure-report/'

	if platform.system() == 'Windows':
		PATH_RESULTS = CURRENT_DIR + 'allure-results\\'
		PATH_REPORT = CURRENT_DIR + 'allure-report\\'

	copy_allure_history()

	GENERATE_CLEAN_REPORT = 'allure generate {} -o {} --clean'.format(PATH_RESULTS,
	                                                                  PATH_REPORT)
	OPEN_REPORT = 'allure open {}'.format(PATH_REPORT)

	os.system(GENERATE_CLEAN_REPORT)
	os.system(OPEN_REPORT)
