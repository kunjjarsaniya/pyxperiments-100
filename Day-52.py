# pip install requests

# -------------------------------------------------------------
# 💱 Currency Converter App using Tkinter + API + OOP
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import requests
import json

# -------------------------------------------------------------
# 📦 CurrencyConverter Class – Handles API logic + saving
# -------------------------------------------------------------

class CurrencyConverter:
    """Handles live exchange rate fetching and conversion logic."""

    def __init__(self, api_url="https://api.exchangerate-api.com/v4/latest/"):
        self.api_url = api_url
        self.rates = {}
        self.base_currency = "USD"

    def fetch_rates(self, base_currency):
        """Fetch live exchange rates from the API."""
        try:
            response = requests.get(self.api_url + base_currency)
            if response.status_code != 200:
                raise Exception("API fetch failed. Check internet or base currency.")

            data = response.json()
            self.rates = data['rates']
            self.base_currency = base_currency
        except Exception as e:
            raise Exception(f"Error fetching rates: {e}")

    def convert(self, amount, to_currency):
        """Convert amount from base to target currency."""
        if not self.rates:
            raise Exception("Exchange rates not loaded.")
        if to_currency not in self.rates:
            raise Exception(f"Target currency {to_currency} not available.")
        return amount * self.rates[to_currency]

    def save_conversion(self, details, filepath):
        """Save conversion details to file."""
        try:
            with open(filepath, "w") as file:
                json.dump(details, file, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save file: {e}")

# -------------------------------------------------------------
# 🖼️ CurrencyConverterApp Class – GUI using Tkinter
# -------------------------------------------------------------

class CurrencyConverterApp:
    """Main GUI application class."""

    def __init__(self, master):
        self.master = master
        self.master.title("💱 Currency Converter")
        self.master.geometry("500x400")
        self.master.configure(bg="white")

        self.converter = CurrencyConverter()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Currency Converter", font=("Arial", 18), bg="white").pack(pady=10)

        # From Currency
        self.from_currency = tk.StringVar(value="USD")
        tk.Label(self.master, text="From Currency (e.g. USD):", bg="white", font=("Arial", 12)).pack()
        tk.Entry(self.master, textvariable=self.from_currency, font=("Arial", 12), width=15).pack(pady=5)

        # To Currency Dropdown
        self.to_currency = tk.StringVar()
        tk.Label(self.master, text="To Currency (e.g. INR):", bg="white", font=("Arial", 12)).pack()
        tk.Entry(self.master, textvariable=self.to_currency, font=("Arial", 12), width=15).pack(pady=5)

        # Amount Entry
        self.amount = tk.StringVar()
        tk.Label(self.master, text="Amount to Convert:", bg="white", font=("Arial", 12)).pack()
        tk.Entry(self.master, textvariable=self.amount, font=("Arial", 12), width=20).pack(pady=5)

        # Convert Button
        tk.Button(self.master, text="🔁 Convert", font=("Arial", 12), command=self.perform_conversion).pack(pady=10)

        # Result Display
        self.result_label = tk.Label(self.master, text="", font=("Arial", 14), bg="white", fg="green")
        self.result_label.pack(pady=10)

        # Save Button
        tk.Button(self.master, text="💾 Save Result", font=("Arial", 12), command=self.save_result).pack(pady=5)

    def perform_conversion(self):
        """Perform currency conversion."""
        from_curr = self.from_currency.get().upper().strip()
        to_curr = self.to_currency.get().upper().strip()
        try:
            amt = float(self.amount.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid numeric amount.")
            return

        try:
            self.converter.fetch_rates(from_curr)
            result = self.converter.convert(amt, to_curr)
            self.result_label.config(text=f"{amt} {from_curr} = {result:.2f} {to_curr}")
            self.last_conversion = {
                "from": from_curr,
                "to": to_curr,
                "amount": amt,
                "converted": round(result, 2)
            }
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

    def save_result(self):
        """Save the conversion result to file."""
        if not hasattr(self, "last_conversion"):
            messagebox.showwarning("Nothing to Save", "Perform a conversion first.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json")],
            title="Save Conversion Result"
        )
        if file_path:
            try:
                self.converter.save_conversion(self.last_conversion, file_path)
                messagebox.showinfo("Saved", f"✅ Conversion saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

# -------------------------------------------------------------
# 🚀 Run Currency Converter App
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

# End of Currency Converter App 💱
