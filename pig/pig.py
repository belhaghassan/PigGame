#!/usr/bin/env python3
# Bilal El-haghassan
# CPSC 386-4
# 2022-02-28
# bilalelhaghassan@csu.fullerton.edu
# @belhaghassan
#
# Lab 00-02
#
"""
This is a game of Dice with 1 - 4 players playing up to 30
"""

from pig_game import game

if __name__ == "__main__":
    playgame = game.PigGame()
    playgame.run()
