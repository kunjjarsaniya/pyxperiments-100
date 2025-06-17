# -----------------------------------------------
# 🐍🐉 Snake-Water-Gun Game (OOP, File Handling)
# -----------------------------------------------

import random
from datetime import datetime

class SnakeWaterGunGame:
    def __init__(self, rounds=5):
        """
        Initialize game settings.
        :param rounds: Number of rounds to play
        """
        self.choices = ['snake', 'water', 'gun']
        self.rounds = rounds
        self.player_score = 0
        self.computer_score = 0
        self.log_file = "snake_water_gun_log.txt"

    def get_computer_choice(self):
        """Randomly select choice for computer."""
        return random.choice(self.choices)

    def get_player_choice(self):
        """
        Prompt user for their choice with validation.
        Returns lowercase string of choice.
        """
        while True:
            choice = input("Choose Snake, Water, or Gun: ").strip().lower()
            if choice in self.choices:
                return choice
            print("⚠️ Invalid input! Please enter 'Snake', 'Water', or 'Gun'.")

    def decide_winner(self, player, computer):
        """
        Decide the winner of a round based on rules:
        Snake drinks Water → Snake wins
        Water douses Gun → Water wins
        Gun kills Snake → Gun wins
        If both same → Draw
        """
        if player == computer:
            return "draw"
        
        wins = {
            'snake': 'water',  # snake drinks water
            'water': 'gun',    # water douses gun
            'gun': 'snake'     # gun kills snake
        }

        if wins[player] == computer:
            return "player"
        else:
            return "computer"

    def log_result(self, round_num, player_choice, computer_choice, winner):
        """
        Log round result with timestamp to file.
        """
        try:
            # Open file with UTF-8 encoding to support special characters like arrows
            with open(self.log_file, "a", encoding="utf-8") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] Round {round_num}: Player chose {player_choice}, Computer chose {computer_choice} → Winner: {winner}\n")
        except Exception as e:
            print(f"❌ Error writing to log file: {e}")

    def play(self):
        """
        Main game loop handling rounds, scoring, and displaying results.
        """
        print(f"\n🎮 Welcome to Snake-Water-Gun! Best of {self.rounds} rounds.\n")

        for round_num in range(1, self.rounds + 1):
            print(f"--- Round {round_num} ---")
            player_choice = self.get_player_choice()
            computer_choice = self.get_computer_choice()
            print(f"🤖 Computer chose: {computer_choice}")

            winner = self.decide_winner(player_choice, computer_choice)

            if winner == "player":
                self.player_score += 1
                print("🎉 You win this round!")
            elif winner == "computer":
                self.computer_score += 1
                print("💻 Computer wins this round!")
            else:
                print("🤝 This round is a draw!")

            self.log_result(round_num, player_choice, computer_choice, winner)
            print(f"Score → You: {self.player_score} | Computer: {self.computer_score}\n")

        print("=== Game Over ===")
        if self.player_score > self.computer_score:
            print(f"🏆 Congratulations! You won the game by {self.player_score} to {self.computer_score}.")
        elif self.computer_score > self.player_score:
            print(f"💻 Computer wins the game by {self.computer_score} to {self.player_score}. Better luck next time!")
        else:
            print(f"🤝 The game is a draw at {self.player_score} each. Well played!")

# -----------------------------------------------
# 🖥️ Program Entry Point
# -----------------------------------------------

def main():
    print("""
🐍🐉 SNAKE-WATER-GUN GAME
--------------------------
Rules:
- Snake drinks Water (Snake wins)
- Water douses Gun (Water wins)
- Gun kills Snake (Gun wins)
- Same choices mean a draw

Let's play!
""")

    # Default rounds = 5, can modify here or extend to input if desired
    game = SnakeWaterGunGame(rounds=5)
    game.play()

# -----------------------------------------------
# ▶️ Run the game
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Snake-Water-Gun Game Program