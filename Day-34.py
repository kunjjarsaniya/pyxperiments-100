# -----------------------------------------------
# 📧 Email Slicer Tool using OOP & File Handling
# -----------------------------------------------

from datetime import datetime

# -----------------------------------------------
# 📦 EmailSlicer Class – Core logic and file handling
# -----------------------------------------------

class EmailSlicer:
    def __init__(self, log_file='email_slicer_log.txt'):
        """
        Initialize the email slicer with optional log file.
        """
        self.log_file = log_file

    def slice_email(self, email):
        """
        Slice the email into username and domain parts.
        Returns a tuple: (username, domain)
        """
        try:
            if '@' not in email or email.count('@') != 1:
                raise ValueError("Invalid email format. Use the format 'username@domain.com'.")

            username, domain = email.strip().split('@')
            if not username or not domain:
                raise ValueError("Username or domain cannot be empty.")
            return username, domain

        except Exception as e:
            raise e

    def log_result(self, email, username, domain):
        """
        Log the slicing result to a text file with timestamp.
        """
        try:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"[{timestamp}] Email: {email} → Username: {username}, Domain: {domain}\n")
        except Exception as e:
            print(f"❌ Error writing to log file: {e}")

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    print("""
📧 EMAIL SLICER TOOL
---------------------
Enter an email address to split it into:
 - Username
 - Domain
""")

    slicer = EmailSlicer()

    while True:
        email_input = input("Enter an email address (or type 'exit' to quit): ").strip()
        
        if email_input.lower() == 'exit':
            print("👋 Goodbye! Thank you for using Email Slicer.")
            break

        try:
            username, domain = slicer.slice_email(email_input)
            print(f"\n🔍 Sliced Email Info:")
            print(f"👤 Username: {username}")
            print(f"🌐 Domain : {domain}\n")

            slicer.log_result(email_input, username, domain)

        except Exception as err:
            print(f"⚠️ Error: {err}\n")

# -----------------------------------------------
# ▶️ Run the Tool
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Email Slicer Tool