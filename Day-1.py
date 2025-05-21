# Simple Calculator in Python
def calculate():
    print("\n🔢 Simple Calculator 🔢")
    print("Operations: + (Add)  |  - (Subtract)  |  * (Multiply)  |  / (Divide)")
    
    operation = input("Enter operation: ")
    if operation not in ('+', '-', '*', '/'):
        print("❌ Invalid operation. Try again.")
        return
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    # Perform Calculation
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        result = x / y if y != 0 else "❌ Error: Division by zero"

    print(f"\n✅ Result: {result}")
    print("🔚 Thank you for using the calculator! 🔚")

# Run the Calculator
calculate()