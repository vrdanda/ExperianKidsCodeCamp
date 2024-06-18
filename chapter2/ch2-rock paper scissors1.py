# Rock, Paper, Scissors Game

# Import the random module
import random

# Define the options
options = ["Rock", "Paper", "Scissors"]

# Get user's choice
user_choice = input("Choose Rock, Paper, or Scissors: ")

# Get computer's choice
computer_choice = random.choice(options)

# Print user and computer choices
print("You chose:", user_choice)
print("Computer chose:", computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")
else:
    print("Computer wins!")


# More Coding Ideas For This Game​

# Add code to play the game endlessly!​

# Add code to ask user after each play if they would like to play again!​

# Make different winning messages and display one randomly after each win​

# Make a main menu where user can select one of the playing modes (endless, ask to continue)