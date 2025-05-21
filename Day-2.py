# -----------------------------------------------
# Number Guessing Game in Python
# -----------------------------------------------

import random  # To generate a random number

def display_welcome_message():
    """Display a welcome message for the player."""
    print("=" * 50)
    print("🎯 Welcome to the Number Guessing Game! 🎯".center(50))
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!\n")


def get_user_guess():
    """Prompt the user to enter a guess and validate input."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("⚠️ Please enter a number between 1 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def play_game():
    """Main logic of the number guessing game."""
    target_number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  # Count number of guesses

    while True:
        guess = get_user_guess()  # Get the user's guess
        attempts += 1

        # Check the guess against the target number
        if guess < target_number:
            print("🔼 Too low! Try a higher number.\n")
        elif guess > target_number:
            print("🔽 Too high! Try a lower number.\n")
        else:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            break  # Exit the loop when the number is guessed


def ask_to_play_again():
    """Ask the user if they want to play another round."""
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("❓ Please enter 'y' for yes or 'n' for no.")


def main():
    """Entry point of the game."""
    display_welcome_message()

    while True:
        play_game()
        if not ask_to_play_again():
            print("\n👋 Thanks for playing! Goodbye!")
            break


# Run the game
if __name__ == "__main__":
    main()
