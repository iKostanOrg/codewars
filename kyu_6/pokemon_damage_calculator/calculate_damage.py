"""
Solution for -> Pokemon Damage Calculator
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import Dict

TYPES: Dict[str, list] = \
    {'fire': [['grass'], ['electric'], ['water']],
     'grass': [['water'], ['electric'], ['fire']],
     'water': [['fire'], [], ['electric', 'grass']],
     'electric': [['water'], ['grass', 'fire'], []]}


def calculate_damage(your_type: str, opponent_type: str, attack, defense) -> int:
    """
    It's a Pokemon battle! Your task is to calculate the damage that a
    particular move would do using the following formula
    (not the actual one from the game):

        damage = 50 * (attack / defense) * effectiveness

    :param your_type:
    :param opponent_type:
    :param attack:
    :param defense:
    :return:
    """
    return 50 * (attack / defense) * effectiveness(your_type, opponent_type)


def effectiveness(your_type: str, opponent_type: str) -> float:
    """
    Effectiveness:

        Super effective: 2x damage
        Neutral: 1x damage
        Not very effective: 0.5x damage

    To prevent this kata from being tedious, you'll only be
    dealing with four types: fire, water, grass, and electric.
    Here is the effectiveness of each match-up:

        fire > grass
        fire < water
        fire = electric
        water < grass
        water < electric
        grass = electric

    :param your_type:
    :param opponent_type:
    :return:
    """
    if opponent_type in TYPES[your_type][0]:
        return 2.0

    if opponent_type in TYPES[your_type][1]:
        return 1.0

    return 0.5
