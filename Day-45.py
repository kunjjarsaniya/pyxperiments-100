# pip install PyPDF2

# -------------------------------------------------------------
# 📄 PDF to Text Converter App using Tkinter + PyPDF2 + OOP
# -------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

# -------------------------------------------------------------
# 🧠 PDFConverter Class - Handles conversion logic
# -------------------------------------------------------------

class PDFConverter:
    """Class to extract text from PDF and handle saving."""

    def __init__(self):
        self.text_data = ""

    def extract_text_from_pdf(self, pdf_path):
        """Extracts text from a PDF file."""
        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                self.text_data = ""

                for page in reader.pages:
                    self.text_data += page.extract_text() + "\n"

            if not self.text_data.strip():
                raise ValueError("No text found in PDF.")
            
            return self.text_data

        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")

    def save_text_to_file(self, text, save_path):
        """Saves extracted text to a file."""
        try:
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            raise Exception(f"Error saving file: {e}")

# -------------------------------------------------------------
# 🖼️ PDFConverterApp Class - Tkinter GUI Layer
# -------------------------------------------------------------

class PDFConverterApp:
    """Handles GUI components and user interactions."""

    def __init__(self, master):
        self.master = master
        self.master.title("📄 PDF to Text Converter")
        self.master.geometry("600x450")
        self.master.configure(bg="white")

        self.converter = PDFConverter()
        self.pdf_path = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="PDF to Text Converter", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

        tk.Button(self.master, text="📂 Select PDF File", font=("Arial", 12), command=self.select_pdf).pack(pady=10)
        tk.Button(self.master, text="📝 Convert to Text", font=("Arial", 12), command=self.convert_pdf).pack(pady=10)
        tk.Button(self.master, text="💾 Save Text File", font=("Arial", 12), command=self.save_text).pack(pady=10)

        self.preview_box = tk.Text(self.master, height=10, wrap="word", font=("Arial", 10))
        self.preview_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            messagebox.showinfo("File Selected", f"📄 Selected file:\n{self.pdf_path}")
            self.preview_box.delete(1.0, tk.END)

    def convert_pdf(self):
        if not self.pdf_path:
            messagebox.showwarning("No File", "⚠️ Please select a PDF file first.")
            return
        try:
            text = self.converter.extract_text_from_pdf(self.pdf_path)
            self.preview_box.delete(1.0, tk.END)
            self.preview_box.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

    def save_text(self):
        text = self.preview_box.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Empty Content", "⚠️ No text to save. Convert a PDF first.")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save As")
        if save_path:
            try:
                self.converter.save_text_to_file(text, save_path)
                messagebox.showinfo("Success", f"✅ File saved to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

# -------------------------------------------------------------
# 🚀 Run the PDF Converter App
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()

# End of PDF to Text Converter Program 🧾
