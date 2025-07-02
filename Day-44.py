# -----------------------------------------------
# 🖼️ Image Viewer App using Tkinter + PIL + OOP
# -----------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageViewerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Image Viewer")
        self.master.geometry("800x600")
        self.master.configure(bg="white")
        self.image_list = []
        self.image_index = 0
        self.create_widgets()

    def create_widgets(self):
        btn_frame = tk.Frame(self.master, bg="white")
        btn_frame.pack(side=tk.TOP, pady=10)

        tk.Button(btn_frame, text="Load Folder", command=self.load_images, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Previous", command=self.show_previous_image, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Next", command=self.show_next_image, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

        self.image_label = tk.Label(self.master, bg="white")
        self.image_label.pack(expand=True)

        self.status_label = tk.Label(self.master, text="", font=("Arial", 10), bg="white")
        self.status_label.pack(pady=10)

    def load_images(self):
        folder = filedialog.askdirectory(title="Select Folder")
        if not folder: return

        formats = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
        self.image_list = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(formats)]

        if self.image_list:
            self.image_index = 0
            self.show_image()
        else:
            messagebox.showwarning("No Images", "No supported images found.")

    def show_image(self):
        try:
            path = self.image_list[self.image_index]
            img = Image.open(path)
            img.thumbnail((750, 500))
            photo = ImageTk.PhotoImage(img)

            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.status_label.config(text=f"{os.path.basename(path)} ({self.image_index + 1}/{len(self.image_list)})")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_next_image(self):
        if self.image_index + 1 < len(self.image_list):
            self.image_index += 1
            self.show_image()

    def show_previous_image(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.show_image()

# -----------------------------------------------
# 🚀 Run Image Viewer
# -----------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()

# End of Image Viewer App