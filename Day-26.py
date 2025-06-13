# -----------------------------------------------
# ⏱️ Stopwatch (CLI Version) using OOP & File Handling
# -----------------------------------------------

import time
import datetime

# -----------------------------------------------
# 🧩 Stopwatch Class – Handles Stopwatch Logic
# -----------------------------------------------

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.running = False
        self.elapsed_time = 0.0  # in seconds

    def start(self):
        """Start the stopwatch."""
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("⏳ Stopwatch started...")
        else:
            print("⚠️ Stopwatch is already running.")

    def stop(self):
        """Stop the stopwatch and calculate elapsed time."""
        if self.running:
            self.end_time = time.time()
            self.elapsed_time += self.end_time - self.start_time
            self.running = False
            print(f"🛑 Stopwatch stopped. Total time: {self.format_time(self.elapsed_time)}")
            self.save_log()
        else:
            print("⚠️ Stopwatch is not running.")

    def reset(self):
        """Reset the stopwatch to 0."""
        self.start_time = None
        self.end_time = None
        self.running = False
        self.elapsed_time = 0.0
        print("🔄 Stopwatch reset.")

    def format_time(self, seconds):
        """Convert seconds to hh:mm:ss.ms format."""
        return time.strftime("%H:%M:%S", time.gmtime(seconds)) + f".{int((seconds % 1) * 100):02d}"

    def save_log(self):
        """Save the timing log to a file with timestamp."""
        try:
            with open("stopwatch_log.txt", "a") as file:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                duration = self.format_time(self.elapsed_time)
                file.write(f"[{now}] Duration: {duration}\n")
        except Exception as e:
            print(f"❌ Error writing to log file: {e}")

    def status(self):
        """Display current status of the stopwatch."""
        if self.running:
            current = time.time()
            elapsed = self.elapsed_time + (current - self.start_time)
        else:
            elapsed = self.elapsed_time
        print(f"⏲️ Elapsed Time: {self.format_time(elapsed)}")


# -----------------------------------------------
# 🧭 CLI Interface – User Command Handler
# -----------------------------------------------

def main():
    sw = Stopwatch()

    print("""
🕹️ STOPWATCH CLI - COMMANDS
----------------------------
start  -> Start the stopwatch
stop   -> Stop the stopwatch
reset  -> Reset the stopwatch
status -> Show current elapsed time
exit   -> Exit the program
""")

    while True:
        cmd = input("📥 Enter command: ").strip().lower()

        if cmd == "start":
            sw.start()
        elif cmd == "stop":
            sw.stop()
        elif cmd == "reset":
            sw.reset()
        elif cmd == "status":
            sw.status()
        elif cmd == "exit":
            if sw.running:
                sw.stop()  # auto stop before exiting
            print("👋 Exiting stopwatch. Goodbye!")
            break
        else:
            print("⚠️ Invalid command. Please try again.")

# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------

if __name__ == "__main__":
    main()
    
# -----------------------------------------------
# 🕰️ Stopwatch CLI Program