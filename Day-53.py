# -------------------------------------------------------------
# ✅ To-Do List App using Tkinter + OOP + File Handling (JSON)
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# -------------------------------------------------------------
# 📦 TaskManager Class – Logic for tasks & file operations
# -------------------------------------------------------------

class TaskManager:
    """Handles loading, saving, adding, and deleting tasks."""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.tasks = json.load(f)
            except Exception as e:
                print(f"⚠️ Error loading tasks: {e}")
                self.tasks = []

    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=4)
        except Exception as e:
            print(f"⚠️ Error saving tasks: {e}")

    def add_task(self, task):
        """Add a new task."""
        if task.strip():
            self.tasks.append(task.strip())
            self.save_tasks()

    def delete_task(self, index):
        """Delete a task by index."""
        try:
            del self.tasks[index]
            self.save_tasks()
        except IndexError:
            pass

    def clear_all_tasks(self):
        """Remove all tasks."""
        self.tasks = []
        self.save_tasks()

# -------------------------------------------------------------
# 🖼️ ToDoApp Class – Handles GUI with Tkinter
# -------------------------------------------------------------

class ToDoApp:
    """Graphical user interface for the To-Do list."""
    
    def __init__(self, master):
        self.master = master
        self.master.title("📝 To-Do List App")
        self.master.geometry("400x500")
        self.master.configure(bg="white")

        self.manager = TaskManager()
        self.create_widgets()
        self.update_task_list()

    def create_widgets(self):
        """Create all UI components."""
        tk.Label(self.master, text="📋 My Tasks", font=("Arial", 18), bg="white").pack(pady=10)

        self.task_listbox = tk.Listbox(self.master, font=("Arial", 12), height=15, selectbackground="skyblue")
        self.task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Buttons
        tk.Button(self.master, text="➕ Add Task", font=("Arial", 12), command=self.add_task).pack(pady=5)
        tk.Button(self.master, text="🗑️ Delete Selected", font=("Arial", 12), command=self.delete_task).pack(pady=5)
        tk.Button(self.master, text="🧹 Clear All", font=("Arial", 12), command=self.clear_all).pack(pady=5)

    def update_task_list(self):
        """Refresh the listbox from the task list."""
        self.task_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        """Add a new task using input dialog."""
        task = simpledialog.askstring("New Task", "Enter your task:")
        if task:
            self.manager.add_task(task)
            self.update_task_list()

    def delete_task(self):
        """Delete selected task."""
        try:
            index = self.task_listbox.curselection()[0]
            confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete the selected task?")
            if confirm:
                self.manager.delete_task(index)
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task to delete.")

    def clear_all(self):
        """Delete all tasks after confirmation."""
        confirm = messagebox.askyesno("Clear All Tasks", "Are you sure you want to clear all tasks?")
        if confirm:
            self.manager.clear_all_tasks()
            self.update_task_list()

# -------------------------------------------------------------
# 🚀 Program Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

# End of To-Do List App 🗂️
