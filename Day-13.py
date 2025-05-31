# -----------------------------------------------
# 🧮 Body Mass Index (BMI) Calculator
# -----------------------------------------------

# Display a welcome message
print("🌟 Welcome to the BMI Calculator!")
print("📏 Please enter your height and weight to calculate your BMI.\n")

# Get user's height in meters
try:
    height = float(input("🔹 Enter your height in meters (e.g., 1.75): "))
except ValueError:
    print("❌ Invalid input! Please enter a number for height.")
    exit()

# Get user's weight in kilograms
try:
    weight = float(input("🔹 Enter your weight in kilograms (e.g., 68): "))
except ValueError:
    print("❌ Invalid input! Please enter a number for weight.")
    exit()

# Check for valid positive values
if height <= 0 or weight <= 0:
    print("⚠️ Height and weight must be greater than zero.")
    exit()

# Calculate BMI using the formula: BMI = weight / (height^2)
bmi = weight / (height ** 2)

# Display the result with two decimal places
print(f"\n📊 Your BMI is: {bmi:.2f}")

# Determine the BMI category based on standard ranges
if bmi < 18.5:
    print("🟡 You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("🟢 You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("🟠 You are overweight.")
else:
    print("🔴 You are obese.")

# Friendly closing message
print("\n✅ Thank you for using the BMI Calculator. Stay healthy! 💪")
