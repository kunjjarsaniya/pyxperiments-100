# -----------------------------------------------
# 😄 Emoji Translator in Python
# -----------------------------------------------

# Display a welcome message
print("🌟 Welcome to the Emoji Translator!")
print("📝 Type a sentence and see it come alive with emojis!\n")

# Dictionary of words and their emoji translations
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "cat": "🐱",
    "dog": "🐶",
    "pizza": "🍕",
    "coffee": "☕",
    "sun": "☀️",
    "star": "⭐",
    "fire": "🔥",
    "cool": "😎",
    "sleep": "😴",
    "laugh": "😂",
    "hello": "👋",
    "bye": "👋",
}

# Ask the user to enter a message
user_input = input("🔹 Enter a sentence: ")

# Split the sentence into words
words = user_input.lower().split()

# Replace each word with an emoji if available
translated = []
for word in words:
    # Get emoji if the word is in the dictionary, else keep the original word
    translated.append(emoji_dict.get(word, word))

# Join the translated list into a sentence
emoji_sentence = " ".join(translated)

# Display the translated message
print("\n🧠 Translated Sentence with Emojis:")
print(emoji_sentence)

# Friendly closing
print("\n✅ Try again with different words to see more emojis! 🎉")

# End of the Emoji Translator
# Thank you for using the Emoji Translator! 😊

# How to Work this code
# Input:- I love pizza and my dog is cool
# Output:- i ❤️ 🍕 and my 🐶 is 😎
