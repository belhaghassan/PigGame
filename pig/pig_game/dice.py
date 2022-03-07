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

"""Dice class for our Pig Game."""

from random import randrange


class Die:
    """This is a Die class"""

    def __init__(self):
        self._roll = 0

    def roll_die(self):
        """This is a method that rolls the die"""
        self._roll = randrange(1, 6)

    @property
    def roll(self):
        """A method print roll number"""
        return self._roll
