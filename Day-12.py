# -----------------------------------------------
# 📌 Password Generator
# -----------------------------------------------

# This program generates a strong random password based on user preferences.

import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """
    Function to generate a random password.
    - length: The number of characters in the password (default = 12)
    - use_digits: Whether to include numbers in the password
    - use_special_chars: Whether to include special characters
    """
    # 🔹 Define character sets
    letters = string.ascii_letters  # A-Z & a-z
    digits = string.digits if use_digits else ""  # 0-9
    special_chars = string.punctuation if use_special_chars else ""  # Special symbols

    # 🔹 Combine all selected character sets
    all_chars = letters + digits + special_chars

    # 🔹 Generate password
    password = "".join(random.choice(all_chars) for _ in range(length))

    return password

# 🔹 User Input
print("\n🔑 Password Generator")
length = int(input("🔢 Enter password length (default: 12): ") or 12)
use_digits = input("🔄 Include numbers? (yes/no): ").strip().lower() == "yes"
use_special_chars = input("🔄 Include special characters? (yes/no): ").strip().lower() == "yes"

# ✅ Generate and display the password
generated_password = generate_password(length, use_digits, use_special_chars)
print(f"\n🛡️ Strong Password Generated: {generated_password}")
