# -----------------------------------------------
# ⏰ Alarm Clock App using Tkinter + OOP
# -----------------------------------------------

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time
import os

ALARM_FILE = "alarms.txt"

class AlarmClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Alarm Clock")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        self.alarms = []
        self.load_alarms()
        self.create_widgets()
        self.start_alarm_thread()

    def create_widgets(self):
        tk.Label(self.master, text="Set Alarm (HH:MM AM/PM)", font=("Arial", 14)).pack(pady=10)
        self.time_entry = tk.Entry(self.master, font=("Arial", 14), justify='center')
        self.time_entry.pack(pady=10)
        tk.Button(self.master, text="Set Alarm", font=("Arial", 12), command=self.set_alarm).pack(pady=5)
        tk.Button(self.master, text="View Alarms", font=("Arial", 12), command=self.view_alarms).pack(pady=5)
        tk.Button(self.master, text="Exit", font=("Arial", 12), command=self.master.quit).pack(pady=20)

    def set_alarm(self):
        time_str = self.time_entry.get().strip()
        if not self.validate_time_format(time_str):
            messagebox.showerror("Invalid Format", "Use HH:MM AM/PM format.")
            return
        self.alarms.append(time_str)
        self.save_alarms()
        messagebox.showinfo("Alarm Set", f"Alarm set for {time_str}")

    def validate_time_format(self, time_str):
        try:
            datetime.strptime(time_str, "%I:%M %p")
            return True
        except ValueError:
            return False

    def view_alarms(self):
        if not self.alarms:
            messagebox.showinfo("Alarms", "No alarms set.")
        else:
            messagebox.showinfo("Alarms Set", "\n".join(self.alarms))

    def load_alarms(self):
        if os.path.exists(ALARM_FILE):
            try:
                with open(ALARM_FILE, "r") as f:
                    self.alarms = [line.strip() for line in f]
            except:
                pass

    def save_alarms(self):
        try:
            with open(ALARM_FILE, "w") as f:
                for alarm in self.alarms:
                    f.write(alarm + "\n")
        except:
            pass

    def start_alarm_thread(self):
        def check_alarms():
            while True:
                now = datetime.now().strftime("%I:%M %p")
                if now in self.alarms:
                    self.alarms.remove(now)
                    self.save_alarms()
                    messagebox.showinfo("Alarm", f"⏰ Time's up: {now}")
                time.sleep(1)

        threading.Thread(target=check_alarms, daemon=True).start()

# -----------------------------------------------
# 🚀 Run Alarm App
# -----------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()

# End of Alarm Clock App