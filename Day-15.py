# -----------------------------------------------
# 🔢 Number to Words Converter in Python
# -----------------------------------------------

# Display a welcome message
print("🌟 Welcome to the Number to Words Converter!")
print("🔎 Enter a number (0 to 9999) to see it in words.\n")

# Define word mappings for basic numbers
units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", 
        "sixty", "seventy", "eighty", "ninety"]

# Function to convert number to words
def number_to_words(num):
    if num < 0 or num > 9999:
        return "❌ Please enter a number between 0 and 9999."
    
    # Handle zero
    if num == 0:
        return "zero"
    
    words = ""

    # Extract thousands place
    if num >= 1000:
        words += units[num // 1000] + " thousand "
        num %= 1000

    # Extract hundreds place
    if num >= 100:
        words += units[num // 100] + " hundred "
        num %= 100

    # Add "and" if number is not a multiple of 100 and higher place exists
    if words != "" and num != 0:
        words += "and "

    # Handle numbers between 10 and 19
    if 10 <= num < 20:
        words += teens[num - 10]
    else:
        # Handle tens place
        if num >= 20:
            words += tens[num // 10]
            if num % 10 != 0:
                words += "-" + units[num % 10]  # Add hyphen for numbers like 42
        elif num > 0:
            words += units[num]

    return words.strip()

# Input from user
try:
    number = int(input("🔹 Enter a number (0 to 9999): "))
    # Convert and display the result
    print(f"\n📝 In words: {number_to_words(number)}")
except ValueError:
    print("❌ Invalid input! Please enter a valid whole number.")

# Closing message
print("\n✅ Thank you for using the converter. Have a great day! 🚀")
