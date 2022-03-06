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

"""Game class for our Pig Game."""

import random
import time
from pig_game import dice, player


class PigGame:
    """PigGame class"""

    def __init__(self):
        self._players = []
        self._turn_score = 0
        welcome = """
        ***************************************************************\n
                            WELCOME TO PIG GAME!
                                A GAME OF DICE

                    **********************************
                    *             _______            *
                    *           /\\       \\           *
                    *          /()\\   ()  \\          *
                    *         /    \\_______\\         *
                    *         \\    /()     /         *
                    *          \\()/   ()  /          *
                    *           \\/_____()/           *
                    *                                *
                    *       Art by Joan G. Stark     *
                    **********************************

                 PACKED WITH RISK, FUN, AND A LITTLE BIT OF LUCK
                        PLAY WITH UP TO 4 PLAYERS!\n
        ***************************************************************\n
        """
        print(welcome)

    def opponent_score(self, opponent):
        """Opponent score getter"""
        for player in self._players:
            if opponent != player:
                return player.score

    @property
    def turn_score(self):
        """Current turn score property"""
        return self._turn_score

    @turn_score.setter
    def turn_score(self, new_turn_score):
        self._turn_score = new_turn_score

    def game_state(self):
        """Game state method"""
        print(
            "\n\t*********************************************************",
            "******\n\t\t\t\tGAME STATE",
        )
        for plyr in self._players:
            print(f"\n\t\t\tPlayer {plyr.name} has a score of {plyr.score}.")
        print("\n\t*********************************************************",
              "******")

    def run(self):
        """Main piggame run function"""

        # Ask user how many players are going to play?
        print("\tHow many players would like to play? ", end=" ")
        num_of_players = int(f"{input()}")

        # Create Die class instance to use for gameplay
        die = dice.Die()

        for plyr in range(num_of_players):
            player_name = input(f"\n\tEnter Player {plyr + 1}'s name: ")
            self._players.append(player.Player(player_name, die.roll))

        if num_of_players < 2:
            num_of_players = 2
            ai_players = ["Optimus Prime", "Megatron", "Zora", "Skynet"]
            ai = random.choice(ai_players)
            self._players.append(
                player.ComputerPlayer(die.roll, ai, self)
            )
            print(
                f"\n\t{self._players[0].name}, you will be playing against ",
                f"AI {self._players[1].name}",
                "!\n\n\n\t**************************************************",
                "*************\n"
            )
            time.sleep(2)

        else:
            print("\n\tWelcome Players: ", end="")
            for plyr in self._players:
                print(f"{plyr.name.upper()} ", end="")
            print(
                f"\n\tThis will be a {num_of_players} player game\n",
                "\n\tFirst player to 30 or more points wins!\n",
            )
        time.sleep(2)
        # Sort players in list by order of die.roll (highest goes first)
        self._players.sort(key=lambda p: p.order, reverse=True)

        # Current player in list to roll the dice.
        current_player_index = 0

        # Top score to end game when a player's score surpasses 30
        top_score = 0
        current_player = self._players[current_player_index]

        print(f"\t\t\t     {current_player.name.upper()} WILL GO FIRST!")
        time.sleep(1)
        while top_score < 30:

            # Current players score for their turn
            self.turn_score = 0

            print(f"\n\t\t\t     ****{current_player.name.upper()}'S TURN***",
                  "*\n")

            time.sleep(1)
            roll = die.roll
            print(f"\t{current_player} rolled a {roll}")
            if roll == 1:
                time.sleep(1)
                print(f"\t{current_player} loses turn!\n")

            else:
                self.turn_score += roll

            print(
                f"\n\tIf {current_player} holds they will have ",
                current_player.score + self.turn_score,
                "\n",
            )

            # Checks to see if player wants to roll or hold
            if self.turn_score != 1 and self.turn_score != 0:
                while current_player.roll_or_hold():
                    next_roll = die.roll
                    print(f"\n\t{current_player} rolled a {next_roll}")
                    time.sleep(1)
                    if next_roll == 1:
                        print(f"\t{current_player} loses turn!")
                        self.turn_score = 0
                        break
                    self.turn_score += next_roll
                    print(
                        f"\n\tIf {current_player} holds they will have ",
                        current_player.score + self.turn_score,
                        "\n",
                    )

            if self.turn_score != 1 and self.turn_score != 0:
                current_player.score = current_player.score + self.turn_score

            if current_player.score > top_score:
                top_score = current_player.score

            current_player_index = (current_player_index + 1) % num_of_players
            current_player = self._players[current_player_index]
            self.turn_score = 0
            self.game_state()

        winner_index = (current_player_index - 1) % num_of_players
        current_player = self._players[winner_index]
        print(
            "\n\n\n\t*******************************************************",
            "*******\n\n\n"
            f"\n\t\t\t\t****{current_player.name.upper()} Wins!****\n",
            "\n\n\n\t*******************************************************",
            "*******\n\n\n"
        )
