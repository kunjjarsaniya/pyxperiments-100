# pip install pyttsx3


# -------------------------------------------------------------
# 🗣️ Text-to-Speech App using Tkinter + pyttsx3 + OOP
# -------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import os

# -------------------------------------------------------------
# 📦 TTSManager Class – Handles text-to-speech logic
# -------------------------------------------------------------

class TTSManager:
    """Manages text-to-speech settings and speech generation."""

    def __init__(self):
        self.engine = pyttsx3.init()
        self.set_defaults()

    def set_defaults(self):
        """Set default voice, speed and volume."""
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[0].id)  # Default to first voice

    def speak(self, text):
        """Speak the given text."""
        if not text.strip():
            raise ValueError("Text is empty.")
        self.engine.say(text)
        self.engine.runAndWait()

    def save_audio(self, text, filepath):
        """Save spoken text to audio file."""
        if not text.strip():
            raise ValueError("Text is empty.")
        self.engine.save_to_file(text, filepath)
        self.engine.runAndWait()

# -------------------------------------------------------------
# 🖼️ TextToSpeechApp Class – GUI using Tkinter
# -------------------------------------------------------------

class TextToSpeechApp:
    """Tkinter GUI app for text-to-speech conversion."""

    def __init__(self, master):
        self.master = master
        self.master.title("🗣️ Text to Speech App")
        self.master.geometry("600x500")
        self.master.config(bg="white")

        self.tts = TTSManager()
        self.filename_label = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(self.master, text="Text to Speech Converter", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

        # Filename display
        tk.Label(self.master, textvariable=self.filename_label, bg="white", fg="gray").pack()

        # Text area
        self.text_area = tk.Text(self.master, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(padx=15, pady=10, expand=True, fill=tk.BOTH)

        # Button frame
        btn_frame = tk.Frame(self.master, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="📂 Open Text File", command=self.open_file).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="💾 Save as Audio", command=self.save_audio).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="▶️ Speak Text", command=self.speak_text).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="🧹 Clear", command=self.clear_text).grid(row=0, column=3, padx=10)

    def open_file(self):
        """Open and load a text file."""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
                    self.filename_label.set(f"Opened: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_audio(self):
        """Save the current text as an audio file."""
        text = self.text_area.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Text area is empty.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 File", "*.mp3")])
        if file_path:
            try:
                self.tts.save_audio(text, file_path)
                messagebox.showinfo("Saved", f"✅ Audio saved at:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def speak_text(self):
        """Speak the text entered."""
        text = self.text_area.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to speak.")
            return
        try:
            self.tts.speak(text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_text(self):
        """Clear the text area."""
        confirm = messagebox.askyesno("Clear", "Clear all text?")
        if confirm:
            self.text_area.delete(1.0, tk.END)
            self.filename_label.set("")

# -------------------------------------------------------------
# 🚀 Program Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

# End of Text-to-Speech App 🗣️
