# -----------------------------------------------
# 🕹️ Hangman Game (CLI) using OOP & File Handling
# -----------------------------------------------

import random
import os

# -----------------------------------------------
# 🧑 Player Class - Tracks player data
# -----------------------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.attempts = 0
        self.won = False


# -----------------------------------------------
# 🎮 Game Class - Manages the entire Hangman game logic
# -----------------------------------------------

class HangmanGame:
    def __init__(self):
        # Word list can be easily modified or loaded from a file
        self.word_list = ['elephant', 'python', 'laptop', 'programming', 'hangman']
        self.max_attempts = 6
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.display_word = ""
        self.player = None

    def choose_random_word(self):
        """Select a random word from the list."""
        self.word_to_guess = random.choice(self.word_list)
        self.display_word = "_" * len(self.word_to_guess)

    def get_player(self):
        """Get player name from input and create Player object."""
        name = input("Enter your name: ")
        self.player = Player(name)

    def update_display_word(self, letter):
        """Update the word display with correctly guessed letters."""
        updated = list(self.display_word)
        for idx, char in enumerate(self.word_to_guess):
            if char == letter:
                updated[idx] = letter
        self.display_word = "".join(updated)

    def display_status(self):
        """Show the current progress of the game."""
        print("\n🔤 Word:", " ".join(self.display_word))
        print(f"❌ Wrong Attempts Left: {self.max_attempts - self.player.attempts}")
        print(f"📜 Letters Guessed: {', '.join(sorted(self.guessed_letters))}")

    def play_turn(self):
        """Take input and process one turn."""
        guess = input("🔡 Guess a letter: ").lower()

        # Validate single character
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet.")
            return

        # Check for repeated guesses
        if guess in self.guessed_letters:
            print("⚠️ You've already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        # Check if guess is correct
        if guess in self.word_to_guess:
            self.update_display_word(guess)
            print("✅ Correct!")
        else:
            self.player.attempts += 1
            print("❌ Incorrect!")

    def check_game_status(self):
        """Check if the game has been won or lost."""
        if "_" not in self.display_word:
            self.player.won = True
            return True
        elif self.player.attempts >= self.max_attempts:
            return True
        return False

    def save_result(self):
        """Save the result of the game to a file."""
        try:
            with open("hangman_log.txt", "a") as file:
                result = "WON" if self.player.won else "LOST"
                file.write(f"{self.player.name} {result} - Word: {self.word_to_guess}\n")
        except Exception as e:
            print(f"❌ Could not save game result: {e}")

    def play(self):
        """Main loop of the game."""
        self.get_player()
        self.choose_random_word()

        print("\n🎮 Welcome to Hangman!")
        print("📌 Guess the word, one letter at a time.")
        print(f"💡 You have {self.max_attempts} incorrect attempts.\n")

        while not self.check_game_status():
            self.display_status()
            self.play_turn()

        self.display_status()
        if self.player.won:
            print(f"🎉 Congratulations {self.player.name}! You guessed the word!")
        else:
            print(f"😢 Game Over! The correct word was: {self.word_to_guess}")

        self.save_result()


# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------

if __name__ == "__main__":
    while True:
        game = HangmanGame()
        game.play()

        again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing Hangman!")
            break
        
# -----------------------------------------------
# End of Hangman Game Program