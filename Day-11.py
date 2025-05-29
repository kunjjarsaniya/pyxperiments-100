# -----------------------------------------------
# 📌 Python Quiz App (CLI)
# -----------------------------------------------

# Multiple-choice quiz with Python programming questions

quiz_questions = {
    "Which keyword is used to define a function in Python?": ["A) def", "B) func", "C) function", "D) define"],
    "Which data type is immutable in Python?": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
    "What does 'print(2**3)' output?": ["A) 8", "B) 6", "C) 9", "D) 16"],
    "Which module is used for working with JSON in Python?": ["A) json", "B) jsonlib", "C) pyjson", "D) pickle"],
    "How do you create a virtual environment in Python?": ["A) python -m venv env", "B) pip install venv", "C) virtual create env", "D) env new venv"]
}

# 🔹 Correct Answers
correct_answers = {
    "Which keyword is used to define a function in Python?": "A",
    "Which data type is immutable in Python?": "C",
    "What does 'print(2**3)' output?": "A",
    "Which module is used for working with JSON in Python?": "A",
    "How do you create a virtual environment in Python?": "A"
}

def run_quiz():
    """
    Function to execute Python quiz.
    Asks multiple-choice questions and tracks score.
    """
    score = 0  # Initialize score

    print("\n🐍 Welcome to the Python Quiz!")
    print("Answer the following questions by selecting A, B, C, or D.\n")

    # Loop through quiz questions
    for question, choices in quiz_questions.items():
        print(f"❓ {question}")
        for choice in choices:
            print(choice)

        user_answer = input("🔹 Your Answer: ").upper()
        
        # Validate answer and update score
        if user_answer == correct_answers[question]:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong! Correct answer:", correct_answers[question], "\n")

    # ✅ Display final score
    print(f"\n🏆 Quiz Completed! Your Final Score: {score}/{len(quiz_questions)}")

# 🔹 Start the Quiz
run_quiz()