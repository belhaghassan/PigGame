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

from .player import Player
from .dice import Die
import time

class PigGame:
    def __init__(self, 
        numOfPlayers=2, 
        player1=Player("Cortana"),
        player2=Player("Skynet")):
        self.player1 = player1
        self.player2 = player2

        self.numOfPlayers = int(input("\nHow many players? "))
        self.players = {}


        self.die = Die()

        

    def gameStats(self):
        for key, val in self.players:
            print(f"\nPlayer {key} has a score of {val}.")

    def roll(self):
        return self.die.roll()
    
    def rollOrHold(self, player):
        decision = input("Hold or Roll? (Enter: h for hold /r for roll)")
        if decision == "r":
            self.players[player] += self.roll()

    # def turnOrder(self):
    #     for players

    def run(self):

        print("""\n\tWelcome to Pig game!
        This is a game of Dice that can be played
        with at least 2 to 4 players\n""")
    

        print(f"""\tPlease enter player names and hit enter
        leave player name blank for AI or no player
        after player 2 name)\n""")
        
        for plyr in range(0,self.numOfPlayers):
            playerName =  input(f"Player {plyr + 1} name: ")
            if playerName and plyr < 2:
                playerName = f"self.player{plyr}"
                self.players[f"self.player{plyr}"] = 0
            else:
                Player(playerName)
                self.players[f"self.player{plyr}"] = 0

        playersTurn = [players for players in self.players]   


        # turn = playersTurn % self.numOfPlayers

        current_player_index = 0
        top_score = 0
        while(top_score < 30):
            
            print(f"{playersTurn[current_player_index]}'s turn")
            print(f"{playersTurn[current_player_index]}playersTurn[current_player_index] rolled {self.die.roll()}")
            
            
            time.sleep(2)

            current_player_index = current_player_index + 1 % self.numOfPlayers
