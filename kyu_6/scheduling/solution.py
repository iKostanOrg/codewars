"""
Test for -> Scheduling (Shortest Job First or SJF)
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def SJF(jobs: list, index: int) -> int:
    """
    It takes in:
    1. "jobs" a non-empty array of positive integers.
        They represent the clock-cycles(cc) needed to finish the job.
    2. "index" a positive integer. That represents the job we're interested in.

    SJF returns:
    1. A positive integer representing the cc it takes to complete the job at index.

    :param jobs:
    :param index:
    :return:
    """
    cc: int = 0
    done: bool = False

    while not done:
        min_j = get_min_job(jobs)
        for i, j in enumerate(jobs):
            if j == 0:
                continue

            # Get to next job in que
            if j == min_j:
                cc += j
                jobs[i] = 0
                # Get to the scheduled job, final step
                if i == index:
                    done = True
                    break

    return cc


def get_min_job(jobs: list) -> int:
    """
    Get the smallest job value of jobs that is not equals to 0
    :param jobs:
    :return:
    """
    min_job = max(jobs)
    for j in jobs:
        if j <= min_job and j != 0:
            min_job = j

    return min_job
