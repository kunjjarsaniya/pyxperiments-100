# -----------------------------------------------
# 📆 Leap Year Checker in Python
# -----------------------------------------------

# Display a welcome message
print("🌟 Welcome to the Leap Year Checker!")
print("🔎 Enter a year to check whether it is a leap year or not.\n")

# Ask the user to input a year
try:
    year = int(input("🔹 Enter a year (e.g., 2024): "))
except ValueError:
    print("❌ Invalid input! Please enter a valid integer year.")
    exit()

# ✅ Logic for leap year:
# A year is a leap year if:
# 1. It is divisible by 4 AND
# 2. Not divisible by 100, UNLESS it is also divisible by 400

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"✅ Yes! {year} is a leap year. 🎉")
else:
    print(f"❌ No, {year} is not a leap year.")

# Friendly closing message
print("\n📘 Tip: Leap years occur every 4 years to help align our calendar with Earth's orbit.")
