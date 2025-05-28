# -----------------------------------------------
# 📌 Multiplication Table Generator
# -----------------------------------------------
# This program prints the multiplication table for any number entered by the user.

def generate_table(number, limit=10):
    """
    Function to generate multiplication table for a given number.
    By default, it prints up to 10 multiples.
    """
    print(f"\n📖 Multiplication Table for {number}\n" + "-"*30)
    
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")  # Display multiplication result
    
    print("-"*30)  # Formatting for clarity

# 🔹 Get user input
print("\n🔢 Multiplication Table Generator")
num = int(input("✍️  Enter a number: "))
limit = int(input("🔄 Enter table limit (default is 10): ") or 10)

# ✅ Generate and display the table
generate_table(num, limit)