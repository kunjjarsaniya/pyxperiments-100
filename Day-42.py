# -----------------------------------------------
# 🌦️ Weather App using Tkinter + API + OOP
# -----------------------------------------------

import tkinter as tk
from tkinter import messagebox
import requests
import os

API_KEY = "your_openweathermap_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
HISTORY_FILE = "weather_search_history.txt"

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.city_entry = tk.Entry(self.master, font=('Arial', 16), justify='center')
        self.city_entry.pack(pady=20)

        tk.Button(self.master, text="Get Weather", font=('Arial', 14), command=self.get_weather).pack(pady=10)
        self.result_label = tk.Label(self.master, font=('Arial', 12), justify='left', wraplength=350)
        self.result_label.pack(padx=20, pady=10)
        tk.Button(self.master, text="View History", font=('Arial', 12), command=self.view_history).pack(pady=5)

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return
        try:
            weather_data = self.fetch_weather(city)
            if weather_data:
                display = self.format_weather_data(weather_data)
                self.result_label.config(text=display)
                self.log_history(city, weather_data)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fetch_weather(self, city):
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ValueError("City not found.")
        else:
            raise Exception("API Error")

    def format_weather_data(self, data):
        return (f"Weather in {data['name']}:\n"
                f"Temperature: {data['main']['temp']}°C\n"
                f"Condition: {data['weather'][0]['description'].capitalize()}\n"
                f"Humidity: {data['main']['humidity']}%\n"
                f"Wind Speed: {data['wind']['speed']} m/s")

    def log_history(self, city, data):
        try:
            with open(HISTORY_FILE, "a") as f:
                f.write(f"{city} - {data['main']['temp']}°C - {data['weather'][0]['description']}\n")
        except:
            pass

    def view_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                history = f.read()
            messagebox.showinfo("Search History", history or "No history found.")
        else:
            messagebox.showinfo("Search History", "No history found.")

# -----------------------------------------------
# 🚀 Run Weather App
# -----------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

# End of Weather App