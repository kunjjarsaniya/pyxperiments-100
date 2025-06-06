# -----------------------------------------------
# 🏦 Mini Banking System in Python
# -----------------------------------------------

# Initialize user's bank balance
balance = 0.0

# Display a welcome message
print("🌟 Welcome to the Python Mini Banking System!")
print("💳 Manage your account with deposit, withdraw, and balance check.\n")

# Function to display the main menu
def show_menu():
    print("\n📋 Please choose an option:")
    print("1️⃣  Deposit")
    print("2️⃣  Withdraw")
    print("3️⃣  Check Balance")
    print("4️⃣  Exit")

# Main loop to handle user actions
while True:
    show_menu()
    choice = input("👉 Enter your choice (1-4): ")

    # Option 1: Deposit money
    if choice == '1':
        try:
            amount = float(input("💰 Enter amount to deposit: $"))
            if amount <= 0:
                print("⚠️ Please enter a positive amount.")
            else:
                balance += amount
                print(f"✅ Successfully deposited ${amount:.2f}. New balance: ${balance:.2f}")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    # Option 2: Withdraw money
    elif choice == '2':
        try:
            amount = float(input("💸 Enter amount to withdraw: $"))
            if amount <= 0:
                print("⚠️ Please enter a positive amount.")
            elif amount > balance:
                print("❌ Insufficient funds! Your current balance is ${:.2f}".format(balance))
            else:
                balance -= amount
                print(f"✅ Successfully withdrew ${amount:.2f}. New balance: ${balance:.2f}")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    # Option 3: Check balance
    elif choice == '3':
        print(f"💼 Your current balance is: ${balance:.2f}")

    # Option 4: Exit
    elif choice == '4':
        print("👋 Thank you for using the Mini Banking System. Goodbye!")
        break

    # Invalid choice
    else:
        print("❌ Invalid option! Please choose between 1 and 4.")
