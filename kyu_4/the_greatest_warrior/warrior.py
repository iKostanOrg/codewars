"""The Greatest Warrior"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

RANKS = ("Pushover",
         "Novice",
         "Fighter",
         "Warrior",
         "Veteran",
         "Sage",
         "Elite",
         "Conqueror",
         "Champion",
         "Master",
         "Greatest")

# A warrior's experience starts from 100.
BASIC_EXPERIENCE = 100

MAX_EXPERIENCE = 10000

# Fight messages
FIGHT_MESSAGES = ["Easy fight",
                  "A good fight",
                  "An intense fight",
                  "You've been defeated"]


class Warrior:
    """
    A class called Warrior which calculates and
    keeps track of level and skills, and ranks.
    """

    def __init__(self):
        # A warrior's experience starts from 100
        self.__experience = BASIC_EXPERIENCE
        # A warrior starts at level 1
        self.__level = self.__set_level()
        # A warrior starts at rank "Pushover"
        self.__rank = self.__set_rank()
        #
        self.__achievements = list()

    def __set_rank(self) -> str:
        """
        :return: warrior's experience
        """
        return RANKS[(self.level // 10)]

    def __set_level(self) -> int:
        """
        A warrior starts at level 1 and
        can progress all the way to 100.

        A warrior cannot progress beyond level 100.

        Each time the warrior's experience increases
        by another 100, the warrior's level rises to
        the next level.

        :return:
        """
        new_level = self.experience // BASIC_EXPERIENCE
        return new_level if new_level <= 100 else 100

    def __update_experience(self, experience: int):
        """
        A warrior's experience is cumulative, and does not
        reset with each rise of level. The only exception
        is when the warrior reaches level 100, with which
        the experience stops at 10000.
        :return:
        """

        if self.level == 100:
            self.__experience = MAX_EXPERIENCE
        elif self.experience + experience > MAX_EXPERIENCE:
            self.__experience = MAX_EXPERIENCE
        else:
            self.__experience += experience

        self.__level = self.__set_level()
        self.__rank = self.__set_rank()

    @property
    def level(self) -> int:
        """
        A warrior's level

        :return: A warrior's level
        """
        return self.__level

    @property
    def rank(self) -> str:
        """
        A warrior starts at rank "Pushover" and
        can progress all the way to "Greatest"

        :return: warrior's rank
        """
        return self.__rank

    @property
    def experience(self) -> int:
        return self.__experience

    @property
    def achievements(self) -> list:
        return self.__achievements

    def battle(self, enemy_level: int):
        # If an enemy level does not fall in the range of 1 to 100,
        # the battle cannot happen and should return "Invalid level".
        if 1 > enemy_level or enemy_level > 100:
            return "Invalid level"

        # Completing a battle against an enemy with the same level
        # as your warrior will be worth 10 experience points.
        if enemy_level == self.level:
            self.__update_experience(10)
            return FIGHT_MESSAGES[1]

        # Completing a battle against an enemy who is one level lower
        # than your warrior will be worth 5 experience points.
        if enemy_level == self.level - 1:
            self.__update_experience(5)
            return FIGHT_MESSAGES[1]

        # Completing a battle against an enemy who is two levels lower
        # or more than your warrior will give 0 experience points.
        if enemy_level <= self.level - 2:
            self.__update_experience(0)
            return FIGHT_MESSAGES[0]

        # Completing a battle against an enemy who is one level higher
        # or more than your warrior will accelarate your experience gaining.
        # The greater the difference between levels, the more experinece
        # your warrior will gain. The formula is 20 * diff * diff where diff
        # equals the difference in levels between the enemy and your warrior.
        if enemy_level > self.level:
            diff = enemy_level - self.level
            if diff >= 5 and (enemy_level // 10) - (self.level // 10) >= 1:
                return FIGHT_MESSAGES[-1]
            self.__update_experience(20 * diff * diff)
            return FIGHT_MESSAGES[2]

    def training(self, params: list) -> str:
        """
        Training will accept an array of three elements:
            the description,
            the experience points your warrior earns,
            and the minimum level requirement.

        :param params:
        :return:
        """
        # If the warrior's level meets the minimum level requirement,
        # the warrior will receive the experience points from it and
        # store the description of the training. It should end up
        # returning that description as well.
        if self.level >= params[2]:
            self.__achievements.append(params[0])
            self.__update_experience(params[1])
            return params[0]
        # If the warrior's level does not meet the minimum level requirement,
        # the warrior does not receive the experience points and description
        # and instead returns "Not strong enough", without any archiving of
        # the result.
        else:
            return "Not strong enough"
