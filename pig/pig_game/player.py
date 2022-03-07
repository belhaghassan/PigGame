#!/usr/bin/env python3
# Bilal El-haghassan
# CPSC 386-04
# 2022-02-28
# bilalelhaghassan@csu.fullerton.edu
# @belhaghassan
#
# Lab 02-00
#
# This is PigGame, a game of DICE and Chance
#

"""Player class for our Pig Game."""

import time


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
        print(
            f"\n\t\t\tWould {self.name} like to Hold or Roll ? \n",
        )
        time.sleep(0.5)
        print(
            "\t(Enter 'roll' or 'r' to roll the die, or just",
            "ENTER anykey for hold)\n\t",
        )
        decision = input("\t")
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

    def __init__(self, order, name, game):
        super().__init__(name, order)
        self._game = game

    def roll_or_hold(self):
        """Roll or hold methed"""
        opponent_score = self._game.opponent_score(self)
        if self.score < 20 or opponent_score > 20:
            if self._game.turn_score < 10:
                return True
        print(f"\t{self.name} will Hold\n")
        return False
