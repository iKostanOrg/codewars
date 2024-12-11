"""
Solution for -> Sports League Table Ranking.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def compute_ranks(number: int, games: list) -> list:
    """
    compute_ranks function.

    Organize a sports league in a round-robin-system. Each team meets
    all other teams. In your league a win gives a team 2 points, a
    draw gives both teams 1 point. After some games you have to compute
    the order of the teams in your league. You use the following criteria
    to arrange the teams:

    Points
    Scoring differential (the difference between goals scored and those conceded)

    Goals scored
    First you sort the teams by their points. If two or more teams reached the same
    number of points, the second criteria comes into play and so on. Finally, if all
    criteria are the same, the teams share a place.

    :param number: int
    :param games: list
    :return: list
    """
    if not games:
        return [1] * number

    teams: dict = {}
    numbers: list = list(range(number))

    for scores in games:
        team_a = scores[0]
        team_b = scores[1]
        calc_teams_score(team_a, team_b, teams, scores, number)

    process_not_played_games(teams, number)
    calc_gd(teams)
    calc_rank(teams)

    return [teams[i]['Rank'] for i in numbers]


def process_not_played_games(teams: dict, number: int) -> None:
    """
    Set default values for teams who did not play a single game.

    :param teams:
    :param number:
    :return:
    """
    for num in range(number):
        if num not in teams:
            check_if_team_registered(num, teams, number)


def calc_teams_score(team_a, team_b, teams, team, number) -> None:
    """
    Calculate following:
        For : Against
        Points

    Set default values for team as well

    :param team_a:
    :param team_b:
    :param teams:
    :param team:
    :param number:
    :return:
    """
    check_if_team_registered(team_a, teams, number)
    calc_for_against(teams, team_a, team[2], team[3])
    calc_team_points(team_a, teams, team[2], team[3])

    check_if_team_registered(team_b, teams, number)
    calc_for_against(teams, team_b, team[3], team[2])
    calc_team_points(team_b, teams, team[3], team[2])


def check_if_team_registered(team, teams, number) -> None:
    """
    Check if team data was processed.
    Set default values otherwise.

    :param team:
    :param teams:
    :param number:
    :return:
    """
    if team not in teams:
        teams[team] = {}
        teams[team]["GD"] = 0
        teams[team]["For:Against"] = [0, 0]
        teams[team]["Points"] = 0
        teams[team]['Rank'] = number


def calc_team_points(team, teams, score_a, score_b) -> None:
    """
    Calculates team points.

    :param team:
    :param teams:
    :param score_a:
    :param score_b:
    :return:
    """
    if score_a > score_b:
        teams[team]['Points'] += 2
    elif score_a == score_b:
        teams[team]['Points'] += 1


def calc_for_against(teams, team, team_1, team_2) -> None:
    """
    Collect "For:Against" data.

    :param teams:
    :param team:
    :param team_1:
    :param team_2:
    :return:
    """
    teams[team]["For:Against"][0] += team_1
    teams[team]["For:Against"][1] += team_2


def calc_gd(teams) -> None:
    """
    Calculates "GD".

    :param teams:
    :return:
    """
    for team in teams:
        teams[team]["GD"] = (
            teams[team]["For:Against"][0] - teams[team]["For:Against"][1])


def calc_rank(teams: dict) -> None:
    """
    Calculates Rank.

    First you sort the teams by their points. If two or more
    teams reached the same number of points, the second criteria
    comes into play and so on. Finally, if all criteria are the
    same, the teams share a place.
    :param teams:
    :return:
    """
    for team_a in teams:
        for team_b in teams:
            if team_a != team_b:
                if teams[team_a]['Points'] > teams[team_b]['Points']:
                    teams[team_a]['Rank'] -= 1
                elif teams[team_a]['Points'] == teams[team_b]['Points'] and \
                        (teams[team_a]['GD'] > teams[team_b]['GD']):
                    teams[team_a]['Rank'] -= 1
                elif teams[team_a]['Points'] == teams[team_b]['Points'] and \
                        (teams[team_a]['GD'] == teams[team_b]['GD']) and \
                        (teams[team_a]["For:Against"][0] > teams[team_b]["For:Against"][0]):
                    teams[team_a]['Rank'] -= 1
                elif teams[team_a]['Points'] == teams[team_b]['Points'] and \
                        (teams[team_a]['GD'] == teams[team_b]['GD']) and \
                        (teams[team_a]["For:Against"][0] == teams[team_b]["For:Against"][0]):
                    teams[team_a]['Rank'] -= 1
