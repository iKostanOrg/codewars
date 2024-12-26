"""
Script in order to copy Allure history.
Created by Egor Kostan.
itHub: https://github.com/ikostan
"""

import os
import platform
import shutil
from utils.log_func import print_log


def copy_allure_history() -> None:
    """
    Copy '.\\allure-report\\history' folder
    into '.\\allure-results\\history'

    :return:
    """

    current_dir: str = str(os.getcwd()).replace("utils", '')
    source_dir: str = ''
    destination_dir: str = ''

    if platform.system() == 'Linux':
        source_dir = 'allure-report/history'
        destination_dir = 'allure-results/history'

    if platform.system() == 'Windows':
        source_dir = r'allure-report\history'
        destination_dir = r'allure-results\history'

    if platform.system() == 'Darwin':
        raise OSError("MAC OS is not supported")

    print("\nGenerating Allure test report...",
          f"\nCURRENT_DIR: {current_dir}, "
          f"\nSOURCE_DIR: {source_dir}, "
          f"\nDESTINATION_DIR: {destination_dir}")

    src_files = os.listdir(current_dir + source_dir)
    print_log(src_files=src_files)

    for file_name in src_files:

        source_file = os.path.join(
            current_dir + source_dir, file_name)

        destination_file = os.path.join(
            current_dir + destination_dir, file_name)

        if os.path.exists(destination_file):
            os.remove(destination_file)

        msg: str = (f"Moving: {source_file} "
                    f"to: {destination_file}")
        print_log(msg=msg)

        shutil.move(source_file, destination_file)


if __name__ == "__main__":
    copy_allure_history()
