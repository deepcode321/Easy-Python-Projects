#!/usr/bin/env python
# coding: utf-8

import random

print("Rock Paper Scissors Game!!!")
print("Rock beats scissors, scissors beats paper, and paper beats rock.")
print("You choose 1 of the options and the computer will also choose one")
print("The First player to win 3 times wins the game!!!")
print("Ready to play here we go Rock Paper Scissors Shoot")

options = ['Rock', 'Paper', 'Scissors']
Player_Score = 0
Computer_Score = 0

WIN_SCORE = 3 
game_count = 0

while (Player_Score<WIN_SCORE)and(Computer_Score<WIN_SCORE):
    player_option = input("Enter your choice! 'Rock', 'Paper', 'Scissors'")
    computer_option = random.choice(options)
    print("Your PIcked", player_option)
    print("Computer Picked", computer_option)
    if player_option == computer_option:
        print("Its a tie")
    elif player_option == 'Rock'and computer_option == 'Scissors':
        Player_Score+=1
        print("you win!")
    elif player_option == 'Paper'and computer_option == 'Scissors':
        Computer_Score+=1
        print("Computer Wins")
    elif player_option == 'Rock'and computer_option == 'Paper':
        Computer_Score+=1
        print("Computer Wins")
    elif player_option == 'Scissors'and computer_option == 'Paper':
        Player_Score+=1
        print("you win!")
    elif player_option == 'Paper'and computer_option == 'Rock':
        Player_Score+=1
        print("you win!")
    elif player_option == 'Scissors' and computer_option == 'Rock':
        Computer_Score+=1
        
    game_count+=1
    print("Your Score", Player_Score, "Computer Score", Computer_Score)
if(Player_Score == WIN_SCORE):
    print("You Won the game:)")
else:
    print("You lost the game :(")

    
