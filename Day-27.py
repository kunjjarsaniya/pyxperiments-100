# -----------------------------------------------
# ⏰ Digital Clock (CLI) using OOP & File Handling
# -----------------------------------------------

import time
import datetime
import os

# -----------------------------------------------
# 🕒 DigitalClock Class – Core Clock Logic
# -----------------------------------------------

class DigitalClock:
    def __init__(self, log_to_file=False):
        """
        Initialize the digital clock.
        :param log_to_file: If True, log each timestamp to a file
        """
        self.log_to_file = log_to_file
        self.running = False

    def get_current_time(self):
        """Get current system time in hh:mm:ss format."""
        return datetime.datetime.now().strftime("%H:%M:%S")

    def display_time(self):
        """Continuously display the clock in the terminal."""
        self.running = True
        print("\n🕒 Real-Time Digital Clock - Press Ctrl+C to exit\n")

        try:
            while self.running:
                current_time = self.get_current_time()
                print(f"\r⏰ {current_time}", end='', flush=True)  # Print on same line

                if self.log_to_file:
                    self.save_log(current_time)

                time.sleep(1)  # Wait for 1 second
        except KeyboardInterrupt:
            self.running = False
            print("\n\n👋 Clock stopped by user.")

    def save_log(self, timestamp):
        """Save the timestamp to a log file."""
        try:
            with open("digital_clock_log.txt", "a") as file:
                file.write(f"{timestamp}\n")
        except Exception as e:
            print(f"\n❌ Error writing to log file: {e}")


# -----------------------------------------------
# 🚀 Program Entry Point – Handles User Setup
# -----------------------------------------------

def main():
    print("""
🕹️ DIGITAL CLOCK (CLI)
----------------------------
Real-time terminal-based clock.
Press Ctrl+C to stop at any time.

Would you like to log every second to a file?
(Useful if you want a history of timestamps)
""")
    
    choice = input("Enable logging? (y/n): ").strip().lower()
    log_enabled = choice == 'y'

    # Create and run the clock
    clock = DigitalClock(log_to_file=log_enabled)
    clock.display_time()


# -----------------------------------------------
# ▶️ Run Program
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Digital Clock Program