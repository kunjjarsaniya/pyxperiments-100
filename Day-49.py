# pip install yt-dlp

# -----------------------------------------------
# 📥 YouTube Video Downloader using yt_dlp + Tkinter
# -----------------------------------------------

import tkinter as tk
from tkinter import messagebox, filedialog
import os
import threading
import yt_dlp

# -----------------------------------------------
# 📦 VideoDownloader Class – Logic for downloading
# -----------------------------------------------

class VideoDownloader:
    """Handles the logic for downloading YouTube videos using yt_dlp."""

    def __init__(self):
        self.last_download_path = ""

    def download_video(self, url, output_path):
        """Download video using yt_dlp to a selected path."""
        if not url.startswith("http"):
            raise ValueError("Invalid URL.")

        try:
            ydl_opts = {
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'quiet': True,
                'format': 'bv*+ba/best[ext=mp4]/best',  # ✅ Smart fallback
                'merge_output_format': 'mp4'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                self.last_download_path = ydl.prepare_filename(info_dict)
                return self.last_download_path

        except Exception as e:
            raise Exception(f"Download failed: {e}")


# -----------------------------------------------
# 🖼️ GUI Class – Tkinter Interface
# -----------------------------------------------

class YouTubeDownloaderApp:
    """Creates a GUI for downloading YouTube videos."""

    def __init__(self, master):
        self.master = master
        self.master.title("📥 YouTube Video Downloader")
        self.master.geometry("500x350")
        self.master.configure(bg="white")

        self.downloader = VideoDownloader()
        self.download_path = tk.StringVar()
        self.video_url = tk.StringVar()
        self.status = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="🎬 YouTube Video Downloader", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        tk.Label(self.master, text="Enter YouTube URL:", font=("Arial", 12), bg="white").pack()
        tk.Entry(self.master, textvariable=self.video_url, font=("Arial", 12), width=50).pack(pady=5)

        tk.Button(self.master, text="📁 Select Download Folder", font=("Arial", 12), command=self.select_path).pack(pady=5)
        tk.Label(self.master, textvariable=self.download_path, wraplength=450, font=("Arial", 9), bg="white", fg="blue").pack()

        tk.Button(self.master, text="⬇️ Download Video", font=("Arial", 12), command=self.start_download_thread).pack(pady=10)
        tk.Label(self.master, textvariable=self.status, font=("Arial", 10), bg="white", fg="green").pack()

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.download_path.set(path)

    def start_download_thread(self):
        # 🔄 Threading wrapper calls internal method with no args
        threading.Thread(target=self.download_video_thread).start()

    def download_video_thread(self):
        url = self.video_url.get().strip()
        path = self.download_path.get().strip()

        if not url:
            messagebox.showwarning("⚠️ Missing URL", "Please enter a YouTube video URL.")
            return

        if not path:
            messagebox.showwarning("⚠️ Missing Path", "Please select a folder to save the video.")
            return

        self.status.set("⏳ Downloading...")
        try:
            file_path = self.downloader.download_video(url, path)
            self.status.set(f"✅ Downloaded:\n{file_path}")
            messagebox.showinfo("Success", f"Video downloaded to:\n{file_path}")
        except Exception as e:
            self.status.set("")
            messagebox.showerror("❌ Error", str(e))


# -----------------------------------------------
# 🚀 App Launcher
# -----------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()


# End of YouTube Downloader GUI 🎥

# Notice: Some time this program not work properly due to yt-dlp updates.
# If you face any issues, please check the yt-dlp documentation or GitHub issues for solutions.