# -----------------------------------------------
# 💰 Tip Calculator in Python
# -----------------------------------------------

# Display a welcome message
print("🌟 Welcome to the Tip Calculator!")
print("🧾 Let's help you calculate how much tip to leave.\n")

# Get user input for bill amount
try:
    bill_amount = float(input("🔹 Enter the total bill amount ($): "))
except ValueError:
    print("❌ Invalid input! Please enter a valid number for the bill.")
    exit()

# Get user input for tip percentage
try:
    tip_percentage = float(input("🔹 Enter the tip percentage you'd like to give (e.g., 15): "))
except ValueError:
    print("❌ Invalid input! Please enter a valid number for the tip percentage.")
    exit()

# Get user input for number of people sharing the bill
try:
    people = int(input("🔹 How many people are splitting the bill? "))
    if people <= 0:
        raise ValueError
except ValueError:
    print("❌ Invalid input! Number of people must be a positive whole number.")
    exit()

# Calculate tip and total
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / people

# Display results
print("\n🧮 Calculation Result:")
print(f"💵 Tip Amount: ${tip_amount:.2f}")
print(f"💰 Total Bill (with tip): ${total_amount:.2f}")
print(f"👥 Each person pays: ${amount_per_person:.2f}")

# Closing message
print("\n✅ Thank you for using the Tip Calculator! Enjoy your meal! 🍽️")
