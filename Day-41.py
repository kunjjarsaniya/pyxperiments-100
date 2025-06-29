# -----------------------------------------------
# 🧮 GUI Calculator App using Tkinter and OOP
# -----------------------------------------------

import tkinter as tk
from tkinter import messagebox

# -----------------------------------------------
# 📐 CalculatorApp Class - GUI & Logic
# -----------------------------------------------

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python GUI Calculator")
        self.master.geometry("300x400")
        self.master.resizable(False, False)
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master, font=('Arial', 18), borderwidth=5, relief="ridge", justify='right')
        self.entry.pack(padx=10, pady=10, fill=tk.X, ipady=10)

        buttons = [['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['C', '0', '=', '+']]

        for row_values in buttons:
            row = tk.Frame(self.master)
            row.pack(expand=True, fill='both')
            for val in row_values:
                btn = tk.Button(row, text=val, font=('Arial', 16), command=lambda v=val: self.on_button_click(v))
                btn.pack(side='left', expand=True, fill='both')

    def on_button_click(self, char):
        if char == "=":
            self.calculate_result()
        elif char == "C":
            self.expression = ""
            self.update_entry()
        else:
            self.expression += str(char)
            self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.update_entry()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.expression = ""
            self.update_entry()

# -----------------------------------------------
# 🚀 Run the Calculator
# -----------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

# End of Calculator App