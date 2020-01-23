#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def solution(args: list) -> str:
    current = [args[0], args[0], False]
    result = ''

    for i, a in enumerate(args):

        if current[1] == a:
            continue
        elif a == current[1] + 1:
            current[1] = a
            current[2] = False
        else:
            if abs(current[1] - current[0]) >= 2 and i != 1:
                result += str(current[0]) + '-' + str(current[1]) + ','
                current[2] = True
            elif abs(current[0] - current[1]) >= 2 and i == 1:
                current[0] = a
                current[1] = a
                continue
            else:
                if current[0] != current[1]:
                    result += str(current[0]) + ',' + str(current[1]) + ','
                    current[2] = True
                else:
                    result += str(current[0]) + ','
                    current[2] = True
            current[0] = a
            current[1] = a

        if i == len(args) - 1 and current[2] is False:

            if current[1] + 1 == a:
                current[1] = a

            if abs(current[1] - current[0]) >= 2:
                result += str(current[0]) + '-' + str(current[1])
            else:
                if current[0] != current[1]:
                    result += str(current[0]) + ',' + str(current[1])
                else:
                    result += str(current[0])

        if i == len(args) - 1 and current[-1] != a and current[2] is True:
            result += str(a)

    return result
