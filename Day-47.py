# pip install requests beautifulsoup4

# -------------------------------------------------------------
# 🧠 Quote Scraper App using Tkinter + Requests + BS4 + OOP
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, filedialog
import requests
from bs4 import BeautifulSoup

# -------------------------------------------------------------
# 🔎 QuoteScraper Class – Handles Web Scraping Logic
# -------------------------------------------------------------

class QuoteScraper:
    """Fetches quotes from http://quotes.toscrape.com."""

    def __init__(self):
        self.base_url = "http://quotes.toscrape.com"
        self.quotes = []

    def scrape_quotes(self):
        """Scrape quotes from multiple pages."""
        self.quotes.clear()
        try:
            url = self.base_url
            while url:
                response = requests.get(url)
                if response.status_code != 200:
                    raise Exception("Failed to load page.")

                soup = BeautifulSoup(response.text, "html.parser")
                quote_blocks = soup.find_all("div", class_="quote")

                for block in quote_blocks:
                    text = block.find("span", class_="text").get_text()
                    author = block.find("small", class_="author").get_text()
                    self.quotes.append(f"{text} — {author}")

                next_btn = soup.find("li", class_="next")
                url = self.base_url + next_btn.a['href'] if next_btn else None

        except Exception as e:
            raise Exception(f"Scraping Error: {e}")

        return self.quotes

    def save_to_file(self, filepath):
        """Save scraped quotes to a text file."""
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                for quote in self.quotes:
                    file.write(quote + "\n")
        except Exception as e:
            raise Exception(f"Save Error: {e}")


# -------------------------------------------------------------
# 🖼️ QuoteScraperApp Class – GUI + User Interface
# -------------------------------------------------------------

class QuoteScraperApp:
    """GUI for interacting with the scraper."""

    def __init__(self, master):
        self.master = master
        self.master.title("📝 Quote Web Scraper")
        self.master.geometry("600x500")
        self.master.configure(bg="white")

        self.scraper = QuoteScraper()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Quote Web Scraper", font=("Arial", 18), bg="white").pack(pady=20)

        tk.Button(self.master, text="🔍 Scrape Quotes", font=("Arial", 12), command=self.scrape_quotes).pack(pady=10)
        tk.Button(self.master, text="💾 Save to File", font=("Arial", 12), command=self.save_quotes).pack(pady=10)

        self.text_box = tk.Text(self.master, wrap="word", font=("Arial", 10))
        self.text_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    def scrape_quotes(self):
        try:
            self.text_box.delete(1.0, tk.END)
            quotes = self.scraper.scrape_quotes()
            if quotes:
                for q in quotes:
                    self.text_box.insert(tk.END, q + "\n\n")
                messagebox.showinfo("Success", f"✅ Scraped {len(quotes)} quotes!")
            else:
                messagebox.showinfo("No Data", "No quotes found.")

        except Exception as e:
            messagebox.showerror("Scraping Failed", str(e))

    def save_quotes(self):
        if not self.scraper.quotes:
            messagebox.showwarning("No Quotes", "⚠️ Scrape quotes before saving.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save Quotes As"
        )
        if file_path:
            try:
                self.scraper.save_to_file(file_path)
                messagebox.showinfo("Saved", f"💾 Quotes saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

# -------------------------------------------------------------
# 🚀 Run the Web Scraper App
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteScraperApp(root)
    root.mainloop()

# End of Quote Scraper App 🌐
