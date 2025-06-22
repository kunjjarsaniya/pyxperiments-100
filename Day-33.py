# -----------------------------------------------
# 🧠 Quiz App using OOP Principles
# -----------------------------------------------

# -----------------------------------------------
# 📘 Question Class – Represents a quiz question
# -----------------------------------------------

class Question:
    def __init__(self, question_text, options, correct_option_index):
        """
        Represents a single quiz question.
        """
        self.text = question_text
        self.options = options
        self.correct_index = correct_option_index  # 1-based index

    def is_correct(self, user_choice):
        """Check if the selected option is correct."""
        return user_choice == self.correct_index

# -----------------------------------------------
# 🧩 QuizApp Class – Controls the quiz logic
# -----------------------------------------------

class QuizApp:
    def __init__(self):
        """
        Initializes the quiz with built-in questions.
        """
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        """
        Returns a list of predefined questions (no file used).
        """
        return [
            Question("What is the capital of India?",
                     ["Mumbai", "Delhi", "Kolkata", "Chennai"], 2),
            Question("Which planet is known as the Red Planet?",
                     ["Earth", "Mars", "Jupiter", "Venus"], 2),
            Question("What is 5 + 7?",
                     ["10", "12", "14", "15"], 2),
            Question("Who wrote 'Romeo and Juliet'?",
                     ["Leo Tolstoy", "William Shakespeare", "Mark Twain", "Charles Dickens"], 2),
            Question("Which gas do plants absorb from the atmosphere?",
                     ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], 3)
        ]

    def run_quiz(self):
        """
        Run the quiz by asking each question to the user.
        """
        print("\n🎓 Welcome to the Quiz App!\n")
        total_questions = len(self.questions)

        for i, question in enumerate(self.questions, start=1):
            print(f"Q{i}: {question.text}")
            for idx, option in enumerate(question.options, start=1):
                print(f"   {idx}. {option}")

            # Input validation
            while True:
                try:
                    user_input = int(input("Your answer (1-4): ").strip())
                    if 1 <= user_input <= len(question.options):
                        break
                    else:
                        print("⚠️ Please choose a number between 1 and 4.")
                except ValueError:
                    print("⚠️ Invalid input! Please enter a number.")

            if question.is_correct(user_input):
                self.score += 1
                print("✅ Correct!\n")
            else:
                correct_answer = question.options[question.correct_index - 1]
                print(f"❌ Incorrect! Correct answer: {correct_answer}\n")

        self.show_result(total_questions)

    def show_result(self, total):
        """
        Display the final score and percentage.
        """
        print("📝 Quiz Completed!")
        print(f"✅ Your Score: {self.score} / {total}")
        percentage = (self.score / total) * 100 if total else 0
        print(f"📊 Percentage: {percentage:.2f}%\n")

# -----------------------------------------------
# ▶️ Run the Quiz App
# -----------------------------------------------

def main():
    app = QuizApp()
    app.run_quiz()

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Quiz App