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

"""Dice class for our Pig Game."""

from random import randrange


class Die:  # pylint: disable=too-few-public-methods
    """This is a Die class"""

    def __init__(self):
        pass

    @property
    def roll(self):
        """This is a method that rolls the die"""
        return randrange(1, 6)
