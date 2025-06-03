# -----------------------------------------------
# 🎲 Dice Roller Simulator in Python
# -----------------------------------------------

import random  # Used to generate random numbers
import sys     # Used for exiting the program

# Display a welcome message
print("🎉 Welcome to the Dice Roller Simulator!")
print("🎲 Press Enter to roll the dice or type 'exit' to quit.\n")

# List of dice faces using text art for visual appeal
dice_faces = {
    1: (
        "⚀",  # Unicode dice face for 1
        "[     ]\n[  •  ]\n[     ]"
    ),
    2: (
        "⚁",
        "[•    ]\n[     ]\n[    •]"
    ),
    3: (
        "⚂",
        "[•    ]\n[  •  ]\n[    •]"
    ),
    4: (
        "⚃",
        "[•   •]\n[     ]\n[•   •]"
    ),
    5: (
        "⚄",
        "[•   •]\n[  •  ]\n[•   •]"
    ),
    6: (
        "⚅",
        "[•   •]\n[•   •]\n[•   •]"
    ),
}

# Start the main loop
while True:
    user_input = input("🔁 Press Enter to roll or type 'exit' to quit: ").strip().lower()

    # Check if user wants to exit
    if user_input == "exit":
        print("👋 Thanks for playing! Goodbye!")
        sys.exit()

    # Roll the dice (random number from 1 to 6)
    roll = random.randint(1, 6)

    # Display the result
    face_symbol, face_graphic = dice_faces[roll]
    print(f"\n🎲 You rolled a {face_symbol} ({roll})!")
    print(face_graphic)
    print("-" * 25)  # Separator for readability
