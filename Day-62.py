# -------------------------------------------------------------
# 🌐 API Data Fetcher to CSV (OOP + Pandas)
# -------------------------------------------------------------

# pip install requests pandas

import requests
import pandas as pd
import json
import os


# -------------------------------------------------------------
# 📦 APIClient – Handles API requests
# -------------------------------------------------------------

class APIClient:
    """Handles fetching data from a public API."""

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_crypto_market_data(self, vs_currency='usd', per_page=10):
        """
        Fetch cryptocurrency market data from CoinGecko.
        Returns a list of dicts.
        """
        endpoint = "/coins/markets"
        params = {
            'vs_currency': vs_currency,
            'order': 'market_cap_desc',
            'per_page': per_page,
            'page': 1,
            'sparkline': False
        }

        try:
            response = requests.get(self.base_url + endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")


# -------------------------------------------------------------
# 📊 DataManager – Handles file operations and data export
# -------------------------------------------------------------

class DataManager:
    """Handles saving and loading data."""

    def __init__(self, output_dir=r"C:\Users\DELL\Desktop\data"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_json(self, data, filename):
        """Save data to JSON file."""
        filepath = os.path.join(self.output_dir, filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return filepath
        except Exception as e:
            raise Exception(f"Failed to save JSON: {e}")

    def save_csv(self, data, filename):
        """Save data to CSV file using pandas."""
        filepath = os.path.join(self.output_dir, filename)
        try:
            df = pd.DataFrame(data)
            df.to_csv(filepath, index=False, encoding="utf-8")
            return filepath
        except Exception as e:
            raise Exception(f"Failed to save CSV: {e}")


# -------------------------------------------------------------
# 🚀 Main Application Logic
# -------------------------------------------------------------

def main():
    print("🌐 Fetching Crypto Market Data...")

    api_client = APIClient(base_url="https://api.coingecko.com/api/v3")
    data_manager = DataManager()

    try:
        # Fetch top 10 cryptocurrencies
        crypto_data = api_client.fetch_crypto_market_data()

        if not crypto_data:
            print("⚠️ No data fetched from API.")
            return

        # Select fields of interest
        processed_data = []
        for item in crypto_data:
            processed_data.append({
                "id": item.get("id"),
                "symbol": item.get("symbol"),
                "name": item.get("name"),
                "current_price": item.get("current_price"),
                "market_cap": item.get("market_cap"),
                "price_change_percentage_24h": item.get("price_change_percentage_24h")
            })

        # Save data
        json_path = data_manager.save_json(processed_data, "crypto_market.json")
        csv_path = data_manager.save_csv(processed_data, "crypto_market.csv")

        print(f"✅ Data saved to JSON: {json_path}")
        print(f"✅ Data saved to CSV: {csv_path}")

    except Exception as e:
        print(f"❌ Error: {e}")


# -------------------------------------------------------------
# 📍 Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()

# End of API Data Fetcher to CSV 🌐
