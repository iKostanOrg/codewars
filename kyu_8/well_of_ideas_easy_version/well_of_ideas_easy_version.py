#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from typing import List


def well(x: List[str]) -> str:

    counter: int = sum(1 for i in x if i.lower() == 'good')
    result: str = ''

    if counter == 0:
        result = 'Fail!'

    if 0 < counter < 3:
        result = 'Publish!'

    if counter > 2:
        result = 'I smell a series!'

    return result
