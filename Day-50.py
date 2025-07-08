# pip install instaloader

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import instaloader
import os

# ---------------------------------------------------------
# 📦 InstaDownloader - handles profile picture downloading
# ---------------------------------------------------------

class InstaDownloader:
    def __init__(self):
        self.loader = instaloader.Instaloader()

    def login(self, username, password):
        """Login to Instagram (needed for profile access)."""
        try:
            self.loader.login(username, password)
            return True
        except Exception as e:
            raise Exception(f"Login failed: {e}")

    def download_profile_pic(self, target_username, save_dir):
        """Download the profile pic of the target username."""
        try:
            profile = instaloader.Profile.from_username(self.loader.context, target_username)
            filename = f"{target_username}_profile.jpg"
            self.loader.download_profilepic(profile)
            # Find the downloaded file in the current directory
            for file in os.listdir():
                if file.startswith(target_username) and file.endswith(".jpg"):
                    os.rename(file, os.path.join(save_dir, filename))
                    return os.path.join(save_dir, filename)
            raise Exception("File not found after download.")
        except Exception as e:
            raise Exception(f"Download failed: {e}")

# ---------------------------------------------------------
# 🖼️ GUI App - Insta Profile Pic Downloader
# ---------------------------------------------------------

class InstaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("📸 Instagram DP Downloader")
        self.master.geometry("500x300")
        self.master.configure(bg="white")

        self.downloader = InstaDownloader()
        self.username = tk.StringVar()
        self.save_path = tk.StringVar()

        self.create_widgets()
        self.login_user()  # Ask for login at the start

    def create_widgets(self):
        tk.Label(self.master, text="Instagram Profile Pic Downloader", font=("Arial", 16), bg="white").pack(pady=15)

        # Target Username
        tk.Label(self.master, text="Enter Target Username:", font=("Arial", 12), bg="white").pack()
        tk.Entry(self.master, textvariable=self.username, font=("Arial", 12), width=30).pack(pady=5)

        # Folder select
        tk.Button(self.master, text="📁 Choose Save Folder", command=self.choose_folder).pack(pady=5)
        tk.Label(self.master, textvariable=self.save_path, font=("Arial", 9), bg="white", fg="blue").pack()

        # Download button
        tk.Button(self.master, text="⬇️ Download Profile Picture", command=self.download_dp, font=("Arial", 12)).pack(pady=15)

    def choose_folder(self):
        folder = filedialog.askdirectory(title="Choose Download Folder")
        if folder:
            self.save_path.set(folder)

    def login_user(self):
        ig_user = simpledialog.askstring("Login", "Enter your Instagram username:")
        ig_pass = simpledialog.askstring("Login", "Enter your Instagram password:", show="*")

        if not ig_user or not ig_pass:
            messagebox.showerror("Login Failed", "Username or password not entered.")
            self.master.destroy()
            return

        try:
            self.downloader.login(ig_user, ig_pass)
            messagebox.showinfo("Login", f"✅ Logged in as {ig_user}")
        except Exception as e:
            messagebox.showerror("Login Error", str(e))
            self.master.destroy()

    def download_dp(self):
        user = self.username.get().strip()
        folder = self.save_path.get().strip()

        if not user or not folder:
            messagebox.showwarning("Missing Info", "Please fill in all fields.")
            return

        try:
            file_path = self.downloader.download_profile_pic(user, folder)
            messagebox.showinfo("Success", f"✅ Profile picture saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# ---------------------------------------------------------
# 🚀 Run the app
# ---------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = InstaApp(root)
    root.mainloop()

# End of Instagram Profile Pic Downloader 📸

# Notice: some time this program not work properly due to instaloader updates.
# If you face any issues, please check the instaloader documentation or GitHub issues for