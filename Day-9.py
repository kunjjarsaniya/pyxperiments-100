# -----------------------------------------------
# 📌 Currency Converter (Static Rates)
# -----------------------------------------------

# This tool converts currencies using predefined exchange rates.

# 🔹 Exchange Rates (Static)
exchange_rates = {
    "USD": 83.00,  # 1 USD = 83 INR (Example rate)
    "EUR": 90.50,  # 1 EUR = 90.50 INR
    "GBP": 105.00,  # 1 GBP = 105 INR
    "JPY": 0.55,  # 1 JPY = 0.55 INR
}

def convert_currency(amount, currency):
    """
    Function to convert given amount to INR using static exchange rates.
    """
    if currency in exchange_rates:
        return amount * exchange_rates[currency]  # Convert currency to INR
    else:
        return "❌ Error: Unsupported currency."

# 🔹 User Input
print("\n💰 Currency Converter 💰")
print("Supported currencies: USD, EUR, GBP, JPY")
currency = input("🔄 Enter currency code (e.g., USD): ").upper()
amount = float(input("💵 Enter amount: "))

# 🔹 Conversion Process
converted_amount = convert_currency(amount, currency)

# ✅ Displaying the result
print(f"\n✅ {amount} {currency} is {converted_amount} INR")
