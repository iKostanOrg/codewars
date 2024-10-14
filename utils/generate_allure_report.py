"""
Script for generating Allure report.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


import os
import platform
from utils.copy_allure_history import copy_allure_history


if __name__ == "__main__":

    current_dir: str = str(os.getcwd()).replace("utils", '')
    PATH_RESULTS: str = ''
    PATH_REPORT: str = ''

    if platform.system() == 'Linux':
        PATH_RESULTS = current_dir + 'allure-results/'
        PATH_REPORT = current_dir + 'allure-report/'

    if platform.system() == 'Windows':
        PATH_RESULTS = current_dir + 'allure-results\\'
        PATH_REPORT = current_dir + 'allure-report\\'

    copy_allure_history()

    generate_clean_report = f'allure generate {PATH_RESULTS} -o {PATH_REPORT} --clean'
    os.system(generate_clean_report)

    OPEN_REPORT = f'allure open {PATH_REPORT}'
    os.system(OPEN_REPORT)
