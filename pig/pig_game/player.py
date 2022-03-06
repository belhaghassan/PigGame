#!/usr/bin/env python3
# Bilal El-haghassan
# CPSC 386-04
# 2022-02-28
# bilalelhaghassan@csu.fullerton.edu
# @belhaghassan
#
# Lab 00-02
#
# This is PigGame, a game of DICE and Chance
#

"""Player class for our Pig Game."""


class Player:
    """Player class for Pig Game"""

    def __init__(self, name, order):
        self._name = name
        self._score = 0
        self._order = order

    @property
    def name(self):
        """Name property"""
        return self._name

    @property
    def order(self):
        """Order property"""
        return self._order

    @property
    def score(self):
        """Score property"""
        return self._score

    @score.setter
    def score(self, new_score):
        """Score setter"""
        self._score = new_score

    def roll_or_hold(self):
        """Roll or hold methed"""
        decision = input(
            f"\n\t\t\tWould {self.name} like to Hold or Roll ? \n"
            "\t(Enter 'roll' or 'r' to roll the die, or just ENTER for hold)\n\t"
        )
        if decision in ("r", "roll"):
            return True
        print(f"\t{self.name} will Hold\n")
        return False

    def __str__(self):
        """Instance string"""
        return self._name

    def __repr__(self):
        """Class representation as string"""
        return f"\t{self._name} has a score of {self._score}"


class ComputerPlayer(Player):
    """AI player class"""

    def __init__(self, order, game):
        super().__init__("Zora", order)
        self._game = game

    def roll_or_hold(self):
        """Roll or hold methed"""
        opponent_score = self._game.opponent_score(self)
        if self.score < 20 or opponent_score > 20:
            if self._game.turn_score < 10:
                return True
        print(f"\t{self.name} will Hold\n")
        return False
