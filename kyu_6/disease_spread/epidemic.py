"""
Solution for -> Disease Spread.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import List


def epidemic(**kwargs) -> int:
    """
    Epidemic function.

    We want to study the spread of the disease through the population of this school.
    The total population may be divided into three:
    - the infecteds (i)
    - those who have recovered (r), and those who are still susceptible (s)
    to get the disease

    We will study the disease on a period of tm days.

    The interval [0, tm] will be divided in n small intervals of length dt = tm/n.
    Initial conditions here could be : S0 = 999, I0 = 1, R0 = 0 Whatever S0 and I0,
    R0 (number of recovered at time 0) is always 0.

    The function epidemic will return the maximum number of infecteds as an
    integer (truncate to integer the result of max(I)).

    tm: the disease on a period of days
    n: small intervals of length
    s0: those who are still susceptible to get the disease (Initial conditions)
    i0: the infected (Initial conditions)
    b: representing a number of contacts which can spread the disease
    a: fraction of the infected that will recover

    :return: the maximum number of infected as an integer
            (truncate to integer the result of max(I)).
    """
    dt: float = float(kwargs['tm']) / kwargs['n']
    # susceptible, infected, recovered at time t
    # Whatever S0 and I0, R0 (number of recovered at time 0) is always 0.
    susceptible: List[float] = [kwargs['s0']]
    infecteds: List[float] = [kwargs['i0']]

    for k in range(kwargs['n']):
        calc_susceptible: float = (
            susceptible[k] - dt * kwargs['b'] * susceptible[k] * infecteds[k]
        )
        susceptible.append(calc_susceptible)

        calc_infecteds: float = (
            infecteds[k] + dt * (
                kwargs['b'] * susceptible[k] * infecteds[k] - kwargs['a'] * infecteds[k]
        ))
        infecteds.append(calc_infecteds)

    return int(max(infecteds))
