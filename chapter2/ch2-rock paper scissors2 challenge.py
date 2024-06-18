import random

def get_user_choice():
    return input("Choose Rock, Paper, or Scissors: ")

def get_computer_choice(options):
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def display_winning_message():
    winning_messages = [
        "Great job!",
        "You're on fire!",
        "Victory is yours!",
        "Keep it up!",
        "You're unstoppable!"
    ]
    return random.choice(winning_messages)

def main():
    options = ["Rock", "Paper", "Scissors"]
    play_again = True

    while play_again:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice(options)
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            print(display_winning_message())

        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"

if __name__ == "__main__":
    main()