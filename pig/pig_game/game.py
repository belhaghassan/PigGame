#!/usr/bin/env python3
# Bilal El-haghassan
# CPSC 386-4
# 2022-02-28
# bilalelhaghassan@csu.fullerton.edu
# @belhaghassan
#
# Lab 00-02
#
# This is PigGame, a game of DICE and Chance
#

"""Game class for our Pig Game."""

from unicodedata import name
from .player import ComputerPlayer, Player
from .dice import Die
import time

class PigGame:
    def __init__(self):
        self._players = []
        self._playersTurnScore = 0

    def opponent_score(self, opponent):   
        for player in self._players:
            if opponent != player:
                return player.score
    
    def turnScore(self):
        return self._playersTurnScore

    def gameStats(self):
        print("\n\t***************************************************************")
        print("\t\t\t\tGame Stats\n")
        for player in self._players:
            print(f"\n\t\t      Player {player.name} has a score of {player.score}.")
        print("\n\t***************************************************************")

    def run(self):
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
            self._playersTurnScore = 0

            print(""
            "\n\t---------------------------------------------------------------\n"
            f"\t\t\t\t{currentPlayer.name.upper()}'S TURN\n"
            # f"\t\t     {currentPlayer.__repr__()}"
            "\t---------------------------------------------------------------\n")

            roll = die.roll()
            print(f"\t{currentPlayer} rolled a {roll}")
            print(f"\t{currentPlayer} Turn Score: ", self._playersTurnScore)
            if roll == 1:
                print(f"\t{currentPlayer} loses turn!\n")
                
            else:
                self._playersTurnScore += roll

            print(f"\t{currentPlayer} Turn Score after roll: ", self._playersTurnScore)
            print(f"\tIf {currentPlayer} holds they will have {currentPlayer.score + self._playersTurnScore}\n")

            # Checks to see if player wants to roll or hold
            if self._playersTurnScore != 1 and self._playersTurnScore != 0:
                while currentPlayer.rollOrHold():
                    nextRoll = die.roll()
                    print(f"\n\t{currentPlayer} rolled {nextRoll}")
                    print(f"\t{currentPlayer} Turn Score: ", self._playersTurnScore)

                    if nextRoll == 1:
                        print(f"\t{currentPlayer} loses turn!")
                        self._playersTurnScore = 0
                        break
                        
                    else:
                        self._playersTurnScore += nextRoll
                        # print(f"\t{currentPlayer} currently has {playersTurnScore} points this turn\n")
                    print(f"\t{currentPlayer} Turn Score after roll: ", self._playersTurnScore)
                    print(f"\tIf {currentPlayer} holds they will have {currentPlayer.score + self._playersTurnScore}\n")


            if self._playersTurnScore != 1 and self._playersTurnScore != 0:
                currentPlayer.score = currentPlayer.score + self._playersTurnScore

            if currentPlayer.score > top_score:
                top_score = currentPlayer.score
                      
            time.sleep(2)
            current_player_index = (current_player_index + 1) % numOfPlayers

            # print("\n\t**************************************************************"
            # # f"\n\t\t     {repr(currentPlayer)}"
            # "\n\t**************************************************************")

            currentPlayer = self._players[current_player_index]
            self._playersTurnScore = 0
            self.gameStats()

        currentPlayer = self._players[(current_player_index - 1) % numOfPlayers] 

        winner = """

        **************************************************************
        **************************************************************
        **************************************************************\n"""
        print(winner,f"\n\t\t\t\t{currentPlayer.name.upper()} Wins!\n", winner)

        
