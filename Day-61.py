# -------------------------------------------------------------
# 🌐 Web Scraper to CSV Automation (OOP + Pandas + BeautifulSoup)
# -------------------------------------------------------------

# pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os


# -------------------------------------------------------------
# 📦 Scraper Class – Handles web scraping logic
# -------------------------------------------------------------

class WebScraper:
    """Scrapes data from a given URL and parses it."""

    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        """Fetch HTML content of the page."""
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch page: {e}")

    def parse_quotes(self, html):
        """
        Example: Scrape quotes from http://quotes.toscrape.com
        Returns a list of dictionaries.
        """
        soup = BeautifulSoup(html, 'html.parser')
        quotes_data = []

        quotes = soup.find_all("div", class_="quote")
        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
            quotes_data.append({
                "quote": text,
                "author": author,
                "tags": ", ".join(tags)
            })

        return quotes_data


# -------------------------------------------------------------
# 📊 DataManager Class – Handles data storage and export
# -------------------------------------------------------------

class DataManager:
    """Manages saving and loading scraped data."""

    def __init__(self, output_dir="data"):
        # Change 'data' to a full path you have access to, e.g. your Desktop
        self.output_dir = os.path.expanduser(r"C:\Users\DELL\Desktop\data")
        os.makedirs(self.output_dir, exist_ok=True)

    def save_json(self, data, filename):
        """Save data as JSON file."""
        filepath = os.path.join(self.output_dir, filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return filepath
        except Exception as e:
            raise Exception(f"Failed to save JSON: {e}")

    def save_csv(self, data, filename):
        """Save data as CSV using pandas."""
        filepath = os.path.join(self.output_dir, filename)
        try:
            df = pd.DataFrame(data)
            df.to_csv(filepath, index=False, encoding="utf-8")
            return filepath
        except Exception as e:
            raise Exception(f"Failed to save CSV: {e}")

    def load_json(self, filename):
        """Load JSON data from file."""
        filepath = os.path.join(self.output_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Failed to load JSON: {e}")


# -------------------------------------------------------------
# 🚀 Main Function – Application entry point
# -------------------------------------------------------------

def main():
    # Target URL for scraping
    url = "http://quotes.toscrape.com"
    print(f"🌐 Scraping data from: {url}")

    scraper = WebScraper(url)
    data_manager = DataManager()

    try:
        html_content = scraper.fetch_html()
        quotes_data = scraper.parse_quotes(html_content)

        if not quotes_data:
            print("⚠️ No data found on the page.")
            return

        # Save as JSON
        json_file = data_manager.save_json(quotes_data, "quotes.json")
        print(f"✅ Data saved as JSON: {json_file}")

        # Save as CSV
        csv_file = data_manager.save_csv(quotes_data, "quotes.csv")
        print(f"✅ Data saved as CSV: {csv_file}")

    except Exception as e:
        print(f"❌ Error: {e}")


# -------------------------------------------------------------
# 📍 Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()

# End of Web Scraper to CSV Automation 🌐