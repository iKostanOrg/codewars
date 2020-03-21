#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import platform
import shutil


def copy_allure_history() -> None:
    """
    Copy '.\allure-report\history' folder
    into '.\allure-results\history'
    :return:
    """

    CURRENT_DIR: str = str(os.getcwd()).replace("utils", '')
    SOURCE_DIR: str = ''
    DESTINATION_DIR: str = ''

    if platform.system() == 'Linux':
        SOURCE_DIR = 'allure-report/history'
        DESTINATION_DIR = 'allure-results/history'

    if platform.system() == 'Windows':
        SOURCE_DIR = 'allure-report\history'
        DESTINATION_DIR = 'allure-results\history'

    if platform.system() == 'Darwin':
        raise OSError("MAC OS is not supported")

    print("\nGenerating Allure test report...",
          "\nCURRENT_DIR: {}, "
          "\nSOURCE_DIR: {}, "
          "\nDESTINATION_DIR: {}".format(CURRENT_DIR,
                                         SOURCE_DIR,
                                         DESTINATION_DIR))

    src_files = os.listdir(CURRENT_DIR + SOURCE_DIR)
    for file_name in src_files:

        source_file = os.path.join(CURRENT_DIR + SOURCE_DIR, file_name)
        destination_file = os.path.join(CURRENT_DIR + DESTINATION_DIR, file_name)

        if os.path.exists(destination_file):
            os.remove(destination_file)

        shutil.move(source_file, destination_file)
