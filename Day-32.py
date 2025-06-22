# -----------------------------------------------
# 🧠 Flashcard App (CLI) using OOP & File Handling
# -----------------------------------------------

import json
import os

# -----------------------------------------------
# 📘 Flashcard Class – represents a single flashcard
# -----------------------------------------------

class Flashcard:
    def __init__(self, question, answer):
        """
        Represents a single flashcard.
        """
        self.question = question
        self.answer = answer

    def to_dict(self):
        """Return a dictionary representation for saving."""
        return {'question': self.question, 'answer': self.answer}

# -----------------------------------------------
# 📚 FlashcardApp Class – handles operations
# -----------------------------------------------

class FlashcardApp:
    def __init__(self, filename="flashcards.json"):
        """
        Flashcard app with loading and saving from a JSON file.
        """
        self.filename = filename
        self.flashcards = []
        self.load_flashcards()

    def load_flashcards(self):
        """Load flashcards from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.flashcards = [Flashcard(**item) for item in data]
            except Exception as e:
                print(f"❌ Error loading flashcards: {e}")

    def save_flashcards(self):
        """Save flashcards to a JSON file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([fc.to_dict() for fc in self.flashcards], file, indent=4)
        except Exception as e:
            print(f"❌ Error saving flashcards: {e}")

    def add_flashcard(self):
        """Prompt user to add a new flashcard."""
        question = input("📝 Enter the question: ").strip()
        answer = input("✅ Enter the answer: ").strip()
        if question and answer:
            self.flashcards.append(Flashcard(question, answer))
            self.save_flashcards()
            print("✅ Flashcard added and saved.")
        else:
            print("⚠️ Question and answer cannot be empty.")

    def review_flashcards(self):
        """Review flashcards one by one."""
        if not self.flashcards:
            print("📭 No flashcards available. Add some first.")
            return

        print("\n📖 Flashcard Review Mode (Press Enter to show answer, type 'q' to quit)\n")

        for i, card in enumerate(self.flashcards, 1):
            print(f"Q{i}: {card.question}")
            cmd = input("Press Enter to see the answer or 'q' to quit: ").strip().lower()
            if cmd == 'q':
                break
            print(f"A{i}: {card.answer}\n{'-'*40}")

    def list_flashcards(self):
        """List all flashcards in the app."""
        if not self.flashcards:
            print("📭 No flashcards to show.")
            return
        print("\n📃 All Flashcards:")
        for i, card in enumerate(self.flashcards, 1):
            print(f"{i}. Q: {card.question} → A: {card.answer}")
        print("-" * 40)

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    app = FlashcardApp()

    while True:
        print("""
🧠 FLASHCARD APP MENU
----------------------
1. Add a flashcard
2. Review flashcards
3. List all flashcards
4. Exit
""")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            app.add_flashcard()
        elif choice == '2':
            app.review_flashcards()
        elif choice == '3':
            app.list_flashcards()
        elif choice == '4':
            print("👋 Goodbye! Your flashcards are saved.")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, 3, or 4.")

# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Flashcard App