#!/usr/bin/env python3
# Bilal El-haghassan
# CPSC 386-4
# 2022-02-28
# bilalelhaghassan@csu.fullerton.edu
# @belhaghassan
#
# Lab 00-02
#

"""Player class for our Pig Game."""

class Player:
    def __init__(self, name, order):
        self._name = name
        self._score = 0
        self._order = order

    @property
    def name(self):
        return self._name

    @property
    def order(self):
        return self._order

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score  

    def rollOrHold(self):
        decision = input(f"\t\t\tWould {self.name} like to Hold or Roll ? \n"
        "\t(Enter 'roll' or 'r' to roll the die, or just ENTER for hold)\n\t")
        if decision == "r" or decision == "roll":
            return True
        print(f"\t{self.name} will Hold\n")
        return False       

    def am_i_human(self):
        return True

    def are_you_real(self):
        return '\tYes, I am a human being.'

    def __str__(self):
        return self._name

    def __repr__(self):
        return f'\t{self._name} has a score of {self._score}'

class ComputerPlayer(Player):
    def __init__(self, order, game):
        super().__init__("Zora", order)
        self._game = game

    def rollOrHold(self):
        opponent_score = self._game.opponent_score(self)
        if opponent_score > self.score and opponent_score > 20:
            return True
        print(f"\t{self.name} will Hold\n")
        return False
