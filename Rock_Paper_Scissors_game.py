# This is rock, paper, and scissors game
# The game is between player and computer
# The player will enter a choice and the computer will randomly choose a choice
# The result will be displayed on the screen
# The game will continue until the player decides to quit
# The player can quit by pressing "q" or "Q"
# The player can enter "rock", "paper", or "scissors" to play the game
# Rules: rock beats scissors, scissors beats paper, paper beats rock
# Date created: 2024-12-28

 
# python library
import random

# variables & functions
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose: {player}, Computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "You win!"
    elif player == "rock" and computer == "paper":
        return "Computer wins!"
    elif player == "paper" and computer == "scissors":
        return "Computer wins!"
    elif player == "paper" and computer == "rock":
        return "You win!"  
    elif player == "scissors" and computer == "rock":
        return "Computer wins!"
    elif player == "scissors" and computer == "paper":
        return "You win!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again." 
    

while True:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thank you for playing!")
        break
