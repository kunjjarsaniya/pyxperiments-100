# -----------------------------------------------
# Rock-Paper-Scissors Game
# -----------------------------------------------

# Description: This is a simple command-line Rock-Paper-Scissors game where the user plays against the computer.
# The user can type 'rock', 'paper', or 'scissors' to play, and 'exit' to quit the game.
# The game randomly generates the computer's choice and determines the winner based on the rules of the game.
# Import necessary libraries
# Importing the random library to generate random choices for the computer


import random  # To allow the computer to make a random choice
import sys     # To allow the user to exit the game easily

# Define the choices available in the game
choices = ["rock", "paper", "scissors"]

# Display a welcome message
print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("👉 Type 'rock', 'paper', or 'scissors' to play.")
print("❌ Type 'exit' anytime to quit the game.\n")

# Start the game loop
while True:
    # Get the player's choice
    player_choice = input("Your move: ").lower()

    # Allow the user to exit
    if player_choice == "exit":
        print("👋 Thanks for playing! Goodbye!")
        sys.exit()

    # Validate the player's input
    if player_choice not in choices:
        print("⚠️ Invalid input! Please type rock, paper, or scissors.\n")
        continue

    # Generate the computer's choice randomly
    computer_choice = random.choice(choices)

    # Show the choices
    print(f"\n🧍 You chose: {player_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    # Determine the result
    if player_choice == computer_choice:
        print("🤝 It's a draw!\n")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!\n")
    else:
        print("😞 You lose!\n")
