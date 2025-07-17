# pip install markdown

# -------------------------------------------------------------
# 🔁 Markdown to HTML Converter using Tkinter + OOP + File IO
# -------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
import os

# -------------------------------------------------------------
# 📦 Converter Class – Converts Markdown to HTML
# -------------------------------------------------------------

class MarkdownConverter:
    """Handles Markdown to HTML conversion and file management."""

    def __init__(self):
        self.md_text = ""
        self.html_text = ""

    def convert(self, markdown_text):
        """Convert markdown to HTML."""
        if not markdown_text.strip():
            raise ValueError("Markdown content is empty.")
        try:
            self.html_text = markdown.markdown(markdown_text)
            return self.html_text
        except Exception as e:
            raise Exception(f"Conversion error: {e}")

    def load_markdown_file(self, filepath):
        """Load markdown content from file."""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                self.md_text = file.read()
            return self.md_text
        except Exception as e:
            raise Exception(f"File load error: {e}")

    def save_html_file(self, filepath, html_content):
        """Save HTML content to file."""
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(html_content)
        except Exception as e:
            raise Exception(f"File save error: {e}")

# -------------------------------------------------------------
# 🖼️ GUI Class – Tkinter Interface
# -------------------------------------------------------------

class MarkdownApp:
    """Tkinter GUI for the Markdown to HTML converter."""

    def __init__(self, master):
        self.master = master
        self.master.title("📝 Markdown to HTML Converter")
        self.master.geometry("700x600")
        self.master.configure(bg="white")

        self.converter = MarkdownConverter()

        self.create_widgets()

    def create_widgets(self):
        """Create all GUI elements."""

        # App Title
        tk.Label(self.master, text="Markdown to HTML Converter",
                 font=("Arial", 18), bg="white").pack(pady=10)

        # Text Input
        self.text_area = tk.Text(self.master, font=("Consolas", 12), wrap="word")
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Button Frame
        btn_frame = tk.Frame(self.master, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="📂 Load Markdown", font=("Arial", 12),
                  command=self.load_markdown).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="🔁 Convert", font=("Arial", 12),
                  command=self.convert_markdown).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="💾 Save HTML", font=("Arial", 12),
                  command=self.save_html).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="🧹 Clear", font=("Arial", 12),
                  command=self.clear_text).pack(side=tk.LEFT, padx=10)

    def load_markdown(self):
        """Load .md file and display in text area."""
        filepath = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
        if filepath:
            try:
                md_content = self.converter.load_markdown_file(filepath)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, md_content)
            except Exception as e:
                messagebox.showerror("Load Error", str(e))

    def convert_markdown(self):
        """Convert text from markdown to HTML."""
        try:
            md_input = self.text_area.get(1.0, tk.END).strip()
            html_output = self.converter.convert(md_input)
            messagebox.showinfo("Converted", "✅ Markdown converted to HTML successfully.")
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, html_output)
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

    def save_html(self):
        """Save converted HTML to a file."""
        filepath = filedialog.asksaveasfilename(defaultextension=".html",
                                                filetypes=[("HTML Files", "*.html")])
        if filepath:
            html_content = self.text_area.get(1.0, tk.END).strip()
            try:
                self.converter.save_html_file(filepath, html_content)
                messagebox.showinfo("Saved", "✅ HTML file saved successfully.")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

    def clear_text(self):
        """Clear the text area."""
        confirm = messagebox.askyesno("Clear All", "Do you want to clear the text?")
        if confirm:
            self.text_area.delete(1.0, tk.END)

# -------------------------------------------------------------
# 🚀 Application Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownApp(root)
    root.mainloop()

# End of Markdown to HTML Converter App 🔁
