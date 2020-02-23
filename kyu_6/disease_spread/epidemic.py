#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def epidemic(tm: int, n: int, s0: int, i0: int, b: float, a: float):
    """
    We want to study the spread of the disease through the population of this school.
    The total population may be divided into three:
        the infecteds (i),
        those who have recovered (r),
        and those who are still susceptible (s) to get the disease.

    We will study the disease on a period of tm days.

    The interval [0, tm] will be divided in n small intervals of length dt = tm/n.
    Initial conditions here could be : S0 = 999, I0 = 1, R0 = 0 Whatever S0 and I0,
    R0 (number of recovered at time 0) is always 0.

    The function epidemic will return the maximum number of infecteds as an
    integer (truncate to integer the result of max(I)).

    :param tm: the disease on a period of days
    :param n: small intervals of length
    :param s0: those who are still susceptible to get the disease (Initial conditions)
    :param i0: the infected (Initial conditions)
    :param b: representing a number of contacts which can spread the disease
    :param a: fraction of the infected that will recover
    :return: the maximum number of infected as an integer (truncate to integer the result of max(I)).
    """
    dt = float(tm) / n

    # susceptible, infected, recovered at time t
    # Whatever S0 and I0, R0 (number of recovered at time 0) is always 0.
    S = [s0] + [0] * n
    I = [i0] + [0] * n
    # R = [0] + [0] * n

    for k in range(n):
        S[k + 1] = S[k] - dt * b * S[k] * I[k]
        I[k + 1] = I[k] + dt * (b * S[k] * I[k] - a * I[k])
        # R[k + 1] = R[k] + dt * I[k] * a

    return int(max(I))
