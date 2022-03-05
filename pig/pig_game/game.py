#!/usr/bin/env python3
# Bilal El-haghassan
# CPSC 386-4
# 2022-02-28
# bilalelhaghassan@csu.fullerton.edu
# @belhaghassan
#
# Lab 00-02
#

"""Game class for our Pig Game."""

from unicodedata import name
from .player import ComputerPlayer, Player
from .dice import Die
import time

class PigGame:
    def __init__(self):
        self._players = []

    def opponent_score(self, opponent):   
        for player in self._players:
            if opponent != player:
                return player.score

    def gameStats(self):
        print("\t------------------------------------------------------------")
        for player in self._players:
            print(f"\n\t\tPlayer {player.name} has a score of {player.score}.")
        print("\t------------------------------------------------------------")

    def run(self):
        CONSOLE_WIDTH = os.get_terminal_size().columns
        welcome = """
        ***************************************************************\n
                            WELCOME TO PIG GAME!
                               A GAME OF DICE 

                    **********************************            
                    *             _______            * 
                    *           /\       \           * 
                    *          /()\   ()  \          * 
                    *         /    \_______\         * 
                    *         \    /()     /         * 
                    *          \()/   ()  /          *
                    *           \/_____()/           *
                    *                                *
                    *       Art by Joan G. Stark     *
                    **********************************

                 PACKED WITH RISK, FUN, AND A LITTLE BIT OF LUCK
                        PLAY WITH UP TO 4 PLAYERS!\n
        ***************************************************************\n
        """
        print(welcome)
        
        # Ask user how many players are going to play?
        print(f"\tHow many players would like to play? ", end = " ")
        numOfPlayers = int(f"{input()}")

        # loop to 
        while (numOfPlayers > 4 or numOfPlayers < 1) and numOfPlayers.isdigit():
            print("\n\tInvalid number of players Entered\n\n", end="")
            print(f"\tHow many players would like to play? ", end = " ")
            numOfPlayers = int(f"{input()}")

        # Create Die class instance to use for gameplay
        die = Die()

        for plyr in range(numOfPlayers):
            playerName =  input(f"\n\tEnter Player {plyr + 1}'s name: ")
            self._players.append(Player(playerName, die.roll()))
        
        if numOfPlayers == 1:
            numOfPlayers = 2
            self._players.append(ComputerPlayer(die.roll(), self))

            print(f"\n\t{self._players[0].name}, you will be playing against AI Zora!\n")
            print("\n\t***************************************************************\n")

        else:       
            print("\n\tWelcome Players: ", end="")
            for player in self._players:
                print(f"{player.name.upper()} ", end="")
            print(f"\n\tThis will be a {numOfPlayers} player game")
            print("\n\tFirst player to 30 or more points wins!\n")
        # Sort players in list by order of die.roll (highest goes first)
        self._players.sort(key=lambda p: p.order, reverse=True)

        # Current player in list to roll the dice.
        current_player_index = 0

        # Top score to end game when a player's score surpasses 30
        top_score = 0
        currentPlayer = self._players[current_player_index]
        
        print(f"\t\t\t     {currentPlayer.name.upper()} WILL GO FIRST!")
        while(top_score < 30):
            
            # Current players score for their turn
            playersTurnScore = 0

            print(""
            "\n\t---------------------------------------------------------------\n"
            f"\t\t\t\t{currentPlayer.name.upper()}'S TURN\n"
            f"\t\t    {currentPlayer.__repr__()}"
            "\n\t---------------------------------------------------------------\n")

            roll = die.roll()
            print(f"\t{currentPlayer} rolled a {roll}")
            if roll != 1:
                playersTurnScore += roll
                print(f"\t{currentPlayer} currently has {currentPlayer.score + playersTurnScore} points\n")
            else:
                print(f"\t{currentPlayer} loses turn!\n")
                playersTurnScore = 0
                print(f"\t\t\t{repr(currentPlayer)}\n")

            # Checks to see if player wants to roll or hold
            while playersTurnScore != 1 and currentPlayer.rollOrHold():
                nextRoll = die.roll()
                print(f"\n\t{currentPlayer} rolled {nextRoll}")

                if nextRoll != 1:
                    playersTurnScore += roll
                    print(f"\t{currentPlayer} currently has {currentPlayer.score + playersTurnScore} points\n")
                else:
                    print(f"\t{currentPlayer} loses turn!")
                    playersTurnScore = 0
                    break

            currentPlayer.score = currentPlayer.score + playersTurnScore

            if currentPlayer.score > top_score:
                top_score = currentPlayer.score
                      
            time.sleep(2)
            current_player_index = (current_player_index + 1) % numOfPlayers

            print("\n\t**************************************************************"
            f"\n\t\t     {repr(currentPlayer)}"
            "\n\t**************************************************************")

            currentPlayer = self._players[current_player_index]

            self.gameStats()

        print("\t**************************************************************"
        "\t**************************************************************"
        "\t**************************************************************\n\n"
        f"\t\t      {currentPlayer.name.upper()} Wins!\n\n"
        "\t**************************************************************"
        "\t**************************************************************"
        "\t**************************************************************")
