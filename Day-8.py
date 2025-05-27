# -----------------------------------------------
# World Count Tool
# -----------------------------------------------

# 📌 Importing the necessary library
import re

def count_words(text):
    """
    Function to count words in a given text.
    It removes special characters and counts the number of words.
    """
    cleaned_text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    words = cleaned_text.split()  # Split text into words
    return len(words)  # Return total word count

# 🔹 Getting user input
print("\n📜 Word Count Tool")
text = input("✍️  Enter your text: ")

# 🔹 Calculating word count
word_count = count_words(text)

# ✅ Displaying the result
print(f"\n📝 Total words: {word_count}")
