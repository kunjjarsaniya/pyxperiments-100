# -------------------------------------------------------------
# 🗒️ Note Taking App using Tkinter + File Handling + OOP
# -------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import os

# -------------------------------------------------------------
# 📦 NoteManager Class – Handles File Saving/Loading Logic
# -------------------------------------------------------------
class NoteManager:
    def __init__(self):
        self.current_file = None
        self.saved_content = ""

    def save_note(self, content, filepath):
        """Save the content to a file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        self.current_file = filepath
        self.saved_content = content

    def load_note(self, filepath):
        """Load content from a file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        self.current_file = filepath
        self.saved_content = content
        return content

# -------------------------------------------------------------
# 🖼️ NoteApp Class – GUI + Features
# -------------------------------------------------------------
class NoteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("📝 Enhanced Note Taking App")
        self.master.geometry("700x550")
        self.master.configure(bg="white")

        self.manager = NoteManager()
        self.filename_label = tk.StringVar(value="📄 No file opened.")
        self.status_label = tk.StringVar(value="🟢 Ready.")

        self.create_widgets()

        # Warn if unsaved changes on close
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

    def create_widgets(self):
        # 🔹 Title
        tk.Label(self.master, text="📝 Simple Note Editor", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        # 🔹 Text Area
        self.text_area = tk.Text(self.master, font=("Consolas", 12), wrap="word", undo=True)
        self.text_area.pack(padx=15, pady=5, expand=True, fill=tk.BOTH)
        self.text_area.bind("<KeyRelease>", self.on_text_change)

        # 🔹 Button Controls
        btn_frame = tk.Frame(self.master, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="📂 Open", width=10, command=self.open_file).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="💾 Save", width=10, command=self.save_file).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="📝 Save As", width=10, command=self.save_as).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="🧹 Clear", width=10, command=self.clear_text).grid(row=0, column=3, padx=10)

        # 🔹 Filename & Status
        info_frame = tk.Frame(self.master, bg="#f2f2f2")
        info_frame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Label(info_frame, textvariable=self.filename_label, font=("Arial", 10), anchor="w", bg="#f2f2f2").pack(side=tk.LEFT, padx=10, pady=5)
        tk.Label(info_frame, textvariable=self.status_label, font=("Arial", 10), anchor="e", bg="#f2f2f2").pack(side=tk.RIGHT, padx=10, pady=5)

    # ---------------------------------------------------------
    # 📁 File Handling Methods
    # ---------------------------------------------------------
    def open_file(self):
        filepath = filedialog.askopenfilename(
            title="Open Note",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Markdown", "*.md"), ("Log files", "*.log")]
        )
        if filepath:
            try:
                content = self.manager.load_note(filepath)
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
                self.filename_label.set(f"📄 Opened: {os.path.basename(filepath)}")
                self.status_label.set("✅ File opened.")
            except Exception as e:
                messagebox.showerror("Open Error", str(e))
                self.status_label.set("❌ Failed to open file.")

    def save_file(self):
        if self.manager.current_file:
            try:
                content = self.text_area.get("1.0", tk.END).strip()
                self.manager.save_note(content, self.manager.current_file)
                self.filename_label.set(f"💾 Saved: {os.path.basename(self.manager.current_file)}")
                self.status_label.set("✅ Saved successfully.")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))
                self.status_label.set("❌ Save failed.")
        else:
            self.save_as()

    def save_as(self):
        filepath = filedialog.asksaveasfilename(
            title="Save Note As",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Markdown", "*.md"), ("Log files", "*.log")]
        )
        if filepath:
            try:
                content = self.text_area.get("1.0", tk.END).strip()
                self.manager.save_note(content, filepath)
                self.filename_label.set(f"💾 Saved As: {os.path.basename(filepath)}")
                self.status_label.set("✅ Saved successfully.")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))
                self.status_label.set("❌ Save As failed.")

    def clear_text(self):
        confirm = messagebox.askyesno("Confirm Clear", "Do you really want to clear all text?")
        if confirm:
            self.text_area.delete("1.0", tk.END)
            self.status_label.set("🧹 Cleared.")
            self.filename_label.set("📄 No file opened.")
            self.manager.current_file = None

    def on_text_change(self, event=None):
        """Update status if user changes text"""
        current = self.text_area.get("1.0", tk.END).strip()
        if current != self.manager.saved_content:
            self.status_label.set("✏️ Unsaved changes...")
        else:
            self.status_label.set("✅ All changes saved.")

    def on_exit(self):
        """Prompt to save before closing."""
        current = self.text_area.get("1.0", tk.END).strip()
        if current != self.manager.saved_content:
            confirm = messagebox.askyesnocancel("Unsaved Changes", "Do you want to save before exiting?")
            if confirm:
                self.save_file()
            elif confirm is None:
                return  # Cancel exit
        self.master.destroy()

# -------------------------------------------------------------
# 🚀 Run the App
# -------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()

# End of Enhanced Note Taking App 🗒️
