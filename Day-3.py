# -----------------------------------------------
# Palindrome Checker in Python
# -----------------------------------------------

# A palindrome is a word, number, phrase, or sequence that reads the same backward as forward.
# Examples: "madam", "racecar", "121", "noon"

def is_palindrome(text):
    """
    This function checks if the given text is a palindrome.
    
    Parameters:
        text (str): The string to be checked.
        
    Returns:
        bool: True if 'text' is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase to make it case-insensitive and space-insensitive
    cleaned_text = text.replace(" ", "").lower()
    
    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

def main():
    # Print a welcome message
    print("🔁 Palindrome Checker 🔁")
    print("------------------------")
    
    # Ask the user to enter a word or phrase
    user_input = input("Enter a word or phrase: ")

    # Call the function and store the result
    if is_palindrome(user_input):
        print(f"✅ '{user_input}' is a palindrome!")
    else:
        print(f"❌ '{user_input}' is not a palindrome.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
