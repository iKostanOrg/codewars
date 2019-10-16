#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def well(x) -> str:

    counter = sum(1 for i in x if i.lower() == 'good')

    if counter == 0:
        return 'Fail!'

    if 0 < counter < 3:
        return 'Publish!'

    if counter > 2:
        return 'I smell a series!'
