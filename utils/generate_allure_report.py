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
    path_results: str = ''
    path_report: str = ''

    if platform.system() == 'Linux':
        path_results = current_dir + 'allure-results/'
        path_report = current_dir + 'allure-report/'

    if platform.system() == 'Windows':
        path_results = current_dir + 'allure-results\\'
        path_report = current_dir + 'allure-report\\'

    copy_allure_history()

    generate_clean_report = f'allure generate {path_results} -o {path_report} --clean'
    os.system(generate_clean_report)

    OPEN_REPORT = f'allure open {path_report}'
    os.system(OPEN_REPORT)
