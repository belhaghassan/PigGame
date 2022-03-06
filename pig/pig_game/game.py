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

import time
from pig_game import dice, player


class PigGame:
    """PigGame class"""
    def __init__(self):
        self._players = []
        self._players_turn_score = 0
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
        self._winner = """\n
        **************************************************************
        **************************************************************
        **************************************************************\n"""

    def opponent_score(self, opponent):
        """Opponent score getter"""
        for plyr in self._players:
            if opponent != plyr:
                opponent_score = plyr.score
        return opponent_score

    @property
    def turn_score(self):
        """Current turn score property"""
        return self._players_turn_score

    def game_state(self):
        """Game state method"""
        print("\n\t***************************************************************")
        print("\t\t\t\tGame Stats\n")
        for plyr in self._players:
            print(f"\n\t\t      Player {plyr.name} has a score of {plyr.score}.")
        print("\n\t***************************************************************")

    def run(self):
        """Main piggame run function"""

        # Ask user how many players are going to play?
        print("\tHow many players would like to play? ", end=" ")
        num_of_players = int(f"{input()}")

        # Create Die class instance to use for gameplay
        die = dice.Die()

        for plyr in range(num_of_players):
            player_name = input(f"\n\tEnter Player {plyr + 1}'s name: ")
            self._players.append(player.Player(player_name, die.roll()))

        if num_of_players == 1:
            num_of_players = 2
            self._players.append(player.ComputerPlayer(die.roll(), self))

            print(
                f"\n\t{self._players[0].name}, you will be playing against AI Zora!\n"
            )
            print(
                "\n\t***************************************************************\n"
            )

        else:
            print("\n\tWelcome Players: ", end="")
            for plyr in self._players:
                print(f"{plyr.name.upper()} ", end="")
            print(f"\n\tThis will be a {num_of_players} player game")
            print("\n\tFirst player to 30 or more points wins!\n")
        # Sort players in list by order of die.roll (highest goes first)
        self._players.sort(key=lambda p: p.order, reverse=True)

        # Current player in list to roll the dice.
        current_player_index = 0

        # Top score to end game when a player's score surpasses 30
        top_score = 0
        current_player = self._players[current_player_index]

        print(f"\t\t\t     {current_player.name.upper()} WILL GO FIRST!")
        while top_score < 30:

            # Current players score for their turn
            self._players_turn_score = 0

            print(
                ""
                "\n\t---------------------------------------------------------------\n"
                f"\t\t\t\t{current_player.name.upper()}'S TURN\n"
                "\t---------------------------------------------------------------\n"
            )

            roll = die.roll()
            print(f"\t{current_player} rolled a {roll}")
            if roll == 1:
                print(f"\t{current_player} loses turn!\n")

            else:
                self._players_turn_score += roll

            print(f"\tIf {current_player} holds they will have\
            {current_player.score + self._players_turn_score}\n")

            # Checks to see if player wants to roll or hold
            if self._players_turn_score != 1 and self._players_turn_score != 0:
                while current_player.roll_or_hold():
                    next_roll = die.roll()
                    print(f"\n\t{current_player} rolled {next_roll}")

                    if next_roll == 1:
                        print(f"\t{current_player} loses turn!")
                        self._players_turn_score = 0
                        break
                    self._players_turn_score += next_roll
                    print(
                        {current_player.score + self._players_turn_score}, "\n"
                    )

            if self._players_turn_score != 1 and self._players_turn_score != 0:
                current_player.score = current_player.score + self._players_turn_score

            if current_player.score > top_score:
                top_score = current_player.score

            time.sleep(2)
            current_player_index = (current_player_index + 1) % num_of_players
            current_player = self._players[current_player_index]
            self._players_turn_score = 0
            self.game_state()

        current_player = self._players[(current_player_index - 1) % num_of_players]
        print(self._winner, f"\n\t\t\t\t{current_player.name.upper()} Wins!\n", self._winner)
