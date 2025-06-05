# -----------------------------------------------
# ✍️ Mad Libs Generator in Python
# -----------------------------------------------

# Display a welcome message
print("🌟 Welcome to the Mad Libs Generator!")
print("🧠 Fill in the blanks to create your own funny story.\n")

# Prompt the user for various words
# Each input will be used in the story template
adjective = input("🔹 Enter an adjective: ")
noun = input("🔹 Enter a noun: ")
verb = input("🔹 Enter a verb (past tense): ")
place = input("🔹 Enter a place: ")
adverb = input("🔹 Enter an adverb: ")
emotion = input("🔹 Enter an emotion: ")
animal = input("🔹 Enter an animal: ")

# 📝 Story template with placeholders
story = f"""
😄 Here's your Mad Libs story:

One day, a very {adjective} {noun} {verb} into a {place}.
It was moving so {adverb}, everyone around was {emotion}!
Suddenly, a giant {animal} appeared and started dancing! 💃

The end. 🎬
"""

# Display the final story
print("\n🎉 Your Generated Mad Libs Story:")
print(story)

# Closing message
print("✅ Thanks for playing Mad Libs! Try again for a different story! 🚀")
