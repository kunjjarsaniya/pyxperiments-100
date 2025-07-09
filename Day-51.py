# pip install requests

# -------------------------------------------------------------
# 📚 Dictionary App using Tkinter + API + OOP + File Handling
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import json
import os

# -------------------------------------------------------------
# 🧠 DictionaryFetcher Class – API + Save logic
# -------------------------------------------------------------

class DictionaryFetcher:
    """Handles API fetching and saving definitions."""

    def __init__(self):
        self.api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        self.last_result = ""

    def get_definition(self, word):
        """Fetch definition from API."""
        try:
            response = requests.get(self.api_url + word)
            if response.status_code != 200:
                raise Exception("Word not found or invalid response.")

            data = response.json()
            meaning = data[0]['meanings'][0]['definitions'][0]['definition']
            example = data[0]['meanings'][0]['definitions'][0].get('example', "No example available.")
            phonetic = data[0].get('phonetic', '')

            result = f"🔤 Word: {word}\n🔊 Phonetic: {phonetic}\n📝 Definition: {meaning}\n💬 Example: {example}"
            self.last_result = result
            return result

        except Exception as e:
            raise Exception(f"API Error: {e}")

    def save_to_file(self, filepath):
        """Save last definition to file."""
        if not self.last_result:
            raise Exception("Nothing to save.")
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(self.last_result)
        except Exception as e:
            raise Exception(f"Save Error: {e}")

# -------------------------------------------------------------
# 🖼️ DictionaryApp Class – GUI Layer
# -------------------------------------------------------------

class DictionaryApp:
    """GUI to interact with dictionary API."""

    def __init__(self, master):
        self.master = master
        self.master.title("📚 Dictionary App")
        self.master.geometry("600x500")
        self.master.configure(bg="white")

        self.fetcher = DictionaryFetcher()
        self.word_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Dictionary Lookup", font=("Arial", 18), bg="white").pack(pady=15)

        # Word Entry
        tk.Label(self.master, text="Enter a Word:", font=("Arial", 12), bg="white").pack()
        tk.Entry(self.master, textvariable=self.word_var, font=("Arial", 12), width=30).pack(pady=5)

        # Buttons
        tk.Button(self.master, text="🔍 Search", font=("Arial", 12), command=self.search_word).pack(pady=5)
        tk.Button(self.master, text="💾 Save Result", font=("Arial", 12), command=self.save_result).pack(pady=5)

        # Result Box
        self.result_box = tk.Text(self.master, height=15, wrap="word", font=("Arial", 11))
        self.result_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    def search_word(self):
        word = self.word_var.get().strip()
        if not word:
            messagebox.showwarning("Input Error", "Please enter a word.")
            return
        try:
            result = self.fetcher.get_definition(word)
            self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_result(self):
        if not self.fetcher.last_result:
            messagebox.showwarning("No Result", "Nothing to save. Search a word first.")
            return
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save Definition")
        if filepath:
            try:
                self.fetcher.save_to_file(filepath)
                messagebox.showinfo("Success", f"✅ Saved to: {filepath}")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

# -------------------------------------------------------------
# 🚀 Run the Dictionary App
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()

# End of Dictionary App 📖
