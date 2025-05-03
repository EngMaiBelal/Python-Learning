import random

def rock_paper_scissors():
    # Choices for the game
    choices = ["rock", "paper", "scissors"]

    # Get the user's choice
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    
    # Check if the user entered a valid choice
    if user_choice not in choices:
        print("Invalid choice, please enter 'rock', 'paper', or 'scissors'.")
        return

    # Get the computer's random choice
    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Play the game
rock_paper_scissors()
