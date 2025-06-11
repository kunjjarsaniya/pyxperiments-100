# -----------------------------------------------
# 🎮 Tic-Tac-Toe (2-Player Game) using OOP & File Handling
# -----------------------------------------------

import os

# -----------------------------------------------
# 🧩 Board Class – Represents the Game Grid
# -----------------------------------------------

class Board:
    def __init__(self):
        # Create 3x3 empty grid
        self.grid = [' ' for _ in range(9)]

    def display(self):
        """Displays the current board layout."""
        print("\n")
        for row in range(3):
            print(" | ".join(self.grid[row*3:(row+1)*3]))
            if row < 2:
                print("--+---+--")
        print("\n")

    def update(self, position, symbol):
        """Updates the board with a symbol if the position is valid."""
        if self.grid[position] == ' ':
            self.grid[position] = symbol
            return True
        return False

    def is_full(self):
        """Check if the board is completely filled (draw)."""
        return ' ' not in self.grid

    def check_winner(self, symbol):
        """Check if the given symbol has won."""
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        return any(self.grid[i] == self.grid[j] == self.grid[k] == symbol for i, j, k in win_positions)

    def reset(self):
        """Resets the board for a new game."""
        self.grid = [' ' for _ in range(9)]


# -----------------------------------------------
# 👥 Player Class – Represents Each Player
# -----------------------------------------------

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


# -----------------------------------------------
# 🎲 Game Class – Manages Game Logic & Flow
# -----------------------------------------------

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []

    def get_player_input(self):
        """Take player names and assign symbols."""
        print("🎮 Welcome to 2-Player Tic-Tac-Toe!\n")
        name1 = input("Enter name for Player 1 (X): ")
        name2 = input("Enter name for Player 2 (O): ")
        self.players = [Player(name1, 'X'), Player(name2, 'O')]

    def take_turn(self, player):
        """Prompt the player for a valid move."""
        while True:
            try:
                pos = int(input(f"{player.name} ({player.symbol}), choose your position (1-9): ")) - 1
                if pos < 0 or pos >= 9:
                    print("⚠️ Position must be between 1 and 9.")
                elif not self.board.update(pos, player.symbol):
                    print("⚠️ Position already taken. Try another.")
                else:
                    break
            except ValueError:
                print("⚠️ Invalid input. Please enter a number between 1 and 9.")

    def save_result(self, winner=None):
        """Save the result to a file."""
        try:
            with open("tic_tac_toe_log.txt", "a") as file:
                if winner:
                    file.write(f"{winner.name} ({winner.symbol}) won the game.\n")
                else:
                    file.write("The game ended in a draw.\n")
        except Exception as e:
            print(f"❌ Failed to save game result: {e}")

    def play(self):
        """Main game loop handling turns and win/draw logic."""
        self.get_player_input()
        self.board.display()
        current = 0  # Start with Player 1

        while True:
            player = self.players[current]
            self.take_turn(player)
            self.board.display()

            if self.board.check_winner(player.symbol):
                print(f"🎉 Congratulations {player.name}! You won the game.")
                self.save_result(player)
                break

            if self.board.is_full():
                print("😮 It's a draw!")
                self.save_result()
                break

            # Switch turns
            current = 1 - current

        # Ask to play again
        again = input("🔁 Do you want to play again? (y/n): ").lower()
        if again == 'y':
            self.board.reset()
            self.play()
        else:
            print("👋 Thanks for playing Tic-Tac-Toe!")


# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------
if __name__ == "__main__":
    game = Game()
    game.play()
# -----------------------------------------------
# End of Tic-Tac-Toe Program