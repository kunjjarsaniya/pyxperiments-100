# pip install requests

# 🔑 Get Your API Key (Free)
# Visit: https://openweathermap.org/api
# Sign up & get your API key
# Replace "YOUR_API_KEY" in the code


# -------------------------------------------------------------
# 🌦️ Desktop Weather Dashboard using Tkinter + OOP + API
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

# Replace this with your own OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"  # 🔑 https://openweathermap.org/api


# -------------------------------------------------------------
# 📦 WeatherManager Class – Handles API and File Logic
# -------------------------------------------------------------

class WeatherManager:
    """Handles weather API communication and file storage."""

    def __init__(self, api_key, history_file="last_city.json"):
        self.api_key = api_key
        self.history_file = history_file

    def get_weather(self, city):
        """Fetch weather data for a city from OpenWeatherMap."""
        try:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather?q={city}"
                f"&appid={self.api_key}&units=metric"
            )
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            raise ValueError("Invalid city name or network issue.")
        except Exception as e:
            raise Exception(f"API error: {e}")

    def save_last_city(self, city):
        """Save the last searched city to a file."""
        try:
            with open(self.history_file, "w") as f:
                json.dump({"city": city}, f)
        except Exception as e:
            print(f"⚠️ Could not save last city: {e}")

    def load_last_city(self):
        """Load the last searched city from a file."""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r") as f:
                    data = json.load(f)
                    return data.get("city", "")
            except Exception as e:
                print(f"⚠️ Could not load last city: {e}")
        return ""


# -------------------------------------------------------------
# 🖼️ WeatherApp Class – Manages the GUI
# -------------------------------------------------------------

class WeatherApp:
    """Creates the Tkinter interface for the weather dashboard."""

    def __init__(self, master):
        self.master = master
        self.master.title("🌦️ Weather Dashboard")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f8ff")

        self.manager = WeatherManager(API_KEY)
        self.create_widgets()

        # Auto-load last searched city
        last_city = self.manager.load_last_city()
        if last_city:
            self.city_entry.insert(0, last_city)
            self.search_weather()

    def create_widgets(self):
        """Build all GUI widgets."""

        # Title
        tk.Label(self.master, text="Live Weather", font=("Arial", 20, "bold"), bg="#f0f8ff").pack(pady=10)

        # City Entry
        self.city_entry = tk.Entry(self.master, font=("Arial", 14), width=25)
        self.city_entry.pack(pady=10)

        # Search Button
        tk.Button(self.master, text="🔍 Get Weather", font=("Arial", 12),
                  command=self.search_weather).pack(pady=5)

        # Weather Result Label
        self.result_label = tk.Label(self.master, text="", font=("Arial", 12), justify="left", bg="#f0f8ff")
        self.result_label.pack(pady=20)

    def search_weather(self):
        """Handle search and update UI."""
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        try:
            data = self.manager.get_weather(city)
            self.display_weather(data)
            self.manager.save_last_city(city)
        except Exception as e:
            messagebox.showerror("Weather Error", str(e))

    def display_weather(self, data):
        """Format and show weather information on screen."""
        try:
            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            weather_info = (
                f"📍 Location: {city}, {country}\n"
                f"🌡️ Temperature: {temp} °C\n"
                f"🌥️ Condition: {desc}\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind Speed: {wind} m/s"
            )

            self.result_label.config(text=weather_info)
        except KeyError:
            raise Exception("Incomplete data received from API.")

# -------------------------------------------------------------
# 🚀 Launch the Tkinter Application
# -------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

# End of Weather Dashboard App 🌦️
