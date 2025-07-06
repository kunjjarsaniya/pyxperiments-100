# pip install requests pillow


# -------------------------------------------------------------
# 😂 Random Meme Generator App using Tkinter + API + OOP
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io
import os

# -------------------------------------------------------------
# 🧠 MemeFetcher Class – Fetch memes from public API
# -------------------------------------------------------------

class MemeFetcher:
    """Handles meme fetching from public API."""

    def __init__(self, api_url="https://meme-api.com/gimme"):
        self.api_url = api_url
        self.last_image_data = None

    def fetch_meme(self):
        """Fetch meme from API and return title, image bytes."""
        try:
            response = requests.get(self.api_url)
            if response.status_code != 200:
                raise Exception("API request failed.")

            data = response.json()
            img_url = data.get("url")
            title = data.get("title", "Untitled Meme")

            # Download the image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                self.last_image_data = img_response.content
                return title, self.last_image_data
            else:
                raise Exception("Failed to download meme image.")

        except Exception as e:
            raise Exception(f"Error fetching meme: {e}")

    def save_meme(self, filename="downloaded_meme.jpg"):
        """Save last fetched meme image."""
        if not self.last_image_data:
            raise Exception("No meme fetched yet.")

        try:
            with open(filename, "wb") as f:
                f.write(self.last_image_data)
        except Exception as e:
            raise Exception(f"Failed to save image: {e}")

# -------------------------------------------------------------
# 🖼️ MemeApp Class – Handles the GUI with Tkinter
# -------------------------------------------------------------

class MemeApp:
    """GUI application class to view and save memes."""

    def __init__(self, master):
        self.master = master
        self.master.title("😂 Random Meme Generator")
        self.master.geometry("600x600")
        self.master.configure(bg="white")

        self.fetcher = MemeFetcher()
        self.current_img = None
        self.current_title = ""

        self.create_widgets()

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.master, text="Click Below to Load a Meme!", font=("Arial", 14), bg="white", wraplength=500)
        self.title_label.pack(pady=10)

        # Image display area
        self.image_label = tk.Label(self.master, bg="white")
        self.image_label.pack(pady=10)

        # Load Meme button
        tk.Button(self.master, text="🎲 Load Random Meme", font=("Arial", 12), command=self.load_meme).pack(pady=5)

        # Save Meme button
        tk.Button(self.master, text="💾 Save Meme", font=("Arial", 12), command=self.save_meme).pack(pady=5)

    def load_meme(self):
        """Fetch meme and display it."""
        try:
            self.title_label.config(text="Loading meme...")
            self.master.update()

            title, img_data = self.fetcher.fetch_meme()
            self.current_title = title

            # Load image in PIL, then convert to Tk format
            image = Image.open(io.BytesIO(img_data))
            image.thumbnail((500, 400))  # Resize if too big
            self.current_img = ImageTk.PhotoImage(image)

            # Update UI
            self.image_label.config(image=self.current_img)
            self.title_label.config(text=title)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_meme(self):
        """Save current meme image to file."""
        try:
            if not self.current_img:
                raise Exception("No meme loaded to save.")
            filename = f"{self.current_title[:30].strip().replace(' ', '_')}.jpg"
            filename = filename.replace("/", "_").replace("\\", "_")  # Clean filename
            self.fetcher.save_meme(filename)
            messagebox.showinfo("Saved", f"✅ Meme saved as:\n{filename}")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))

# -------------------------------------------------------------
# 🚀 Run Meme Generator App
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = MemeApp(root)
    root.mainloop()

# End of Meme Generator App 😂
