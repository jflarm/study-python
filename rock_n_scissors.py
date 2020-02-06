#!/usr/bin/python3.7
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using \
# input), compare them, print out a message of congratulations to the winner, \
# and ask if the players want to start a new game)
# Rock > Scissors
# Scissors > Paper
# Paper > Rock

sel1 =""
sel2 =""

while sel1 == sel2:
    sel1 = input("Rock, Paper or Scissors: ")
    sel2 = input("Rock, Paper or Scissors: ")
    if sel1 == sel2:
        print("Draw, play again!")

if sel1=="Rock" and sel2=="Scissors":
    print("Player 1 wins")
elif sel1=="Paper" and sel2=="Rock":
    print("Player 1 wins")
elif sel1=="Scissors" and sel2=="Paper":
    print("Player 1 wins")
else:
    print("Player 2 wins")

