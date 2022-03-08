
# Pig - A Die Game

![image](https://user-images.githubusercontent.com/51680128/157302191-77494deb-61d0-446e-9f4b-1066a5f1c597.png)

The game uses only one six sided die and is played with 2 or more players. Players take turns rolling the die and tabulating a score according to the rules. The first player to score 100 or more points wins.

In our version of the game, we shall make a few changes to the rules. Since it is a computer based game, the six-sided die is simulated by the computer. Additionally, the game can be played against the computer should there only be one player. If there is more than one player, the game is played as a [hotseat](https://en.wikipedia.org/wiki/Hotseat_(multiplayer_mode)) multiplayer game. And to win the game, a player must score 30 points.

## Rules

* There is at least two players playing the game and at most four.
* To start the game, a player can enter the number 1 through 4 to establish how many players there are. If a player enters 1, then the other player is a _computer AI_.
* When the player enteres 2 or more players, then the _computer AI_ is not used as a player.
* There is one six-sided die (simulated by the game using a psuedo-random number generator); the faces of the die are numbered 1, 2, 3, 4, 5, and 6.
* The game is turn based.
* All players have a name, including the _computer AI_.
* The player who goes first is selected by each player rolling the die once. The players are ordered in ascending order given the number they rolled. If there is a tie between two or more players, the computer can break the tie by arbitrarily assigning that player to a position not less than the position the player rolled.
* Once each player has had a turn in ascending order, the turn returns to the first player. (The process is a circular queue.)
* Each turn, a player rolls the die.
    * The current player rolls the die until their turn ends. All other players wait their turn. A turn ends when a player rolls a 1 or chooses to hold.
    * If the player rolls a 1, the player scores nothing that turn and it becomes the next player's turn. The player's overall score does not change because the player has lost the points accrued during their turn.
    * If the player rolls any other number, the value of the die is added to their turn's score as points and the player's turn may continue. The player's overall score does not change until their turn ends.
    * If a player chooses to hold, their turn score total is added to their score, and it becomes the next player's turn.
* The player may not choose to hold until after the die has been rolled at least once.
* The game ends when a player ends their turn with a score of 30 points or greater.
* At the beginning of every die roll, the game displays the current player's total score, current turn score, and how many times the player has rolled. Once the die is rolled, the computer displays the value of the die. If it is a 1, the computer ends the current player's turn and moves on to the next player.

## Requirements

To run this terminal based game:
1. `git clone https://github.com/belhaghassan/PigGame.git`
2. `cd pig`
3. `python pig.py`

