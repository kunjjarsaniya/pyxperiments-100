# -----------------------------------------------
# 💰 Mini Expense Tracker using OOP & File Handling
# -----------------------------------------------

import csv
import os
from datetime import datetime

# -----------------------------------------------
# 📦 Expense Class – Represents a single expense
# -----------------------------------------------

class Expense:
    def __init__(self, date, category, amount, note):
        """
        Initialize an expense item.
        """
        self.date = date  # string (YYYY-MM-DD)
        self.category = category
        self.amount = float(amount)
        self.note = note

# -----------------------------------------------
# 🧾 ExpenseTracker Class – Manages all expenses
# -----------------------------------------------

class ExpenseTracker:
    def __init__(self, file_name="expenses.csv"):
        """
        Initialize the expense tracker with a CSV file.
        """
        self.file_name = file_name
        self.expenses = []
        self.load_expenses()

    def add_expense(self, expense):
        """
        Add a new expense to the tracker and save it.
        """
        self.expenses.append(expense)
        self.save_expense(expense)
        print("✅ Expense added successfully!")

    def save_expense(self, expense):
        """
        Save a single expense to the CSV file.
        """
        try:
            with open(self.file_name, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([expense.date, expense.category, expense.amount, expense.note])
        except Exception as e:
            print(f"❌ Error saving expense: {e}")

    def load_expenses(self):
        """
        Load expenses from the CSV file into memory.
        """
        if not os.path.exists(self.file_name):
            return  # No data to load yet

        try:
            with open(self.file_name, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:
                        date, category, amount, note = row
                        self.expenses.append(Expense(date, category, float(amount), note))
        except Exception as e:
            print(f"❌ Error loading expenses: {e}")

    def view_expenses(self):
        """
        Display all stored expenses in a tabular format.
        """
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return

        print("\n📋 Expense List:")
        print("{:<12} {:<15} {:<10} {:<30}".format("Date", "Category", "Amount", "Note"))
        print("-" * 70)
        for exp in self.expenses:
            print("{:<12} {:<15} ₹{:<9.2f} {:<30}".format(exp.date, exp.category, exp.amount, exp.note))
        print()

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    tracker = ExpenseTracker()

    print("""
💸 MINI EXPENSE TRACKER
--------------------------
1. Add Expense
2. View Expenses
3. Exit
""")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            try:
                # Auto date with option to override
                use_today = input("Use today's date? (Y/n): ").strip().lower()
                if use_today == 'n':
                    date = input("Enter date (YYYY-MM-DD): ").strip()
                else:
                    date = datetime.now().strftime('%Y-%m-%d')

                category = input("Enter category (e.g., Food, Travel): ").strip()
                amount = float(input("Enter amount spent (₹): ").strip())
                note = input("Enter optional note: ").strip()

                expense = Expense(date, category, amount, note)
                tracker.add_expense(expense)

            except ValueError:
                print("⚠️ Invalid input! Amount must be a number.\n")

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            print("👋 Exiting Expense Tracker. Have a budget-friendly day!")
            break

        else:
            print("⚠️ Please enter a valid option (1-3).\n")

# -----------------------------------------------
# ▶️ Run the Expense Tracker
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Mini Expense Tracker