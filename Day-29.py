# -----------------------------------------------
# 🍅 Pomodoro Timer (CLI) using OOP & File Handling
# -----------------------------------------------

import time
from datetime import datetime

# -----------------------------------------------
# ⏳ PomodoroTimer Class - Handles timer logic
# -----------------------------------------------

class PomodoroTimer:
    def __init__(self, work_duration=25, short_break=5, long_break=15, cycles_before_long_break=4):
        """
        Initialize the Pomodoro timer settings (minutes).
        :param work_duration: Work session length in minutes
        :param short_break: Short break length in minutes
        :param long_break: Long break length in minutes
        :param cycles_before_long_break: Number of cycles before long break
        """
        self.work_duration = work_duration * 60  # convert to seconds
        self.short_break = short_break * 60
        self.long_break = long_break * 60
        self.cycles_before_long_break = cycles_before_long_break
        self.current_cycle = 0
        self.log_file = "pomodoro_log.txt"

    def start(self):
        """Start the Pomodoro timer cycles."""
        print("🍅 Pomodoro Timer started! Press Ctrl+C to stop anytime.\n")

        try:
            while True:
                self.current_cycle += 1
                print(f"🔄 Cycle {self.current_cycle} - Work session started.")
                self.countdown(self.work_duration, "Work")

                # Log work session completion
                self.log_session("Work", self.work_duration)

                # Determine break type
                if self.current_cycle % self.cycles_before_long_break == 0:
                    print(f"🌟 Long break started ({self.long_break // 60} minutes). Relax!")
                    self.countdown(self.long_break, "Long Break")
                    self.log_session("Long Break", self.long_break)
                else:
                    print(f"☕ Short break started ({self.short_break // 60} minutes). Take a rest!")
                    self.countdown(self.short_break, "Short Break")
                    self.log_session("Short Break", self.short_break)

        except KeyboardInterrupt:
            print("\n👋 Pomodoro Timer stopped. Great job today!")

    def countdown(self, seconds, session_type):
        """Countdown timer that prints remaining time every second."""
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            print(f"\r⏳ {session_type} Time Left: {timer_display}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
        print()  # New line after countdown finishes

    def log_session(self, session_type, duration_seconds):
        """Log completed session with timestamp."""
        try:
            with open(self.log_file, "a") as log:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                duration_min = duration_seconds // 60
                log.write(f"[{timestamp}] Completed {session_type} session of {duration_min} minutes.\n")
        except Exception as e:
            print(f"❌ Failed to write to log file: {e}")

# -----------------------------------------------
# 🖥️ CLI Interface - Program entry point and user input
# -----------------------------------------------

def get_positive_int(prompt, default):
    """Get positive integer input from user or use default."""
    while True:
        user_input = input(f"{prompt} (default {default}): ").strip()
        if not user_input:
            return default
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("⚠️ Please enter a valid positive integer.")

def main():
    print("""
🍅 POMODORO TIMER
-----------------
Customize your Pomodoro timer durations.
Press Ctrl+C anytime to stop the timer.
""")

    work = get_positive_int("Enter work session duration in minutes", 25)
    short_break = get_positive_int("Enter short break duration in minutes", 5)
    long_break = get_positive_int("Enter long break duration in minutes", 15)
    cycles = get_positive_int("Enter number of cycles before long break", 4)

    timer = PomodoroTimer(work_duration=work,
                          short_break=short_break,
                          long_break=long_break,
                          cycles_before_long_break=cycles)
    timer.start()

# -----------------------------------------------
# 🚀 Run the Pomodoro Timer Program
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Pomodoro Timer Program