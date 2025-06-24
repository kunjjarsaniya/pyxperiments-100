# -----------------------------------------------
# 🔗 URL Shortener CLI App using OOP & File Handling
# -----------------------------------------------

import json
import os
import string

# -----------------------------------------------
# 📦 URLShortener Class – Core Shortening Logic
# -----------------------------------------------

class URLShortener:
    def __init__(self, db_file="url_data.json"):
        """
        Initialize the URLShortener with an optional database file.
        """
        self.url_map = {}            # Maps short_code → original URL
        self.reverse_map = {}        # Maps original URL → short_code
        self.db_file = db_file
        self.counter = 1000          # Base counter for generating unique short codes
        self.chars = string.ascii_letters + string.digits
        self.base = len(self.chars)

        self.load_data()

    def encode(self, num):
        """Convert a number to base62 string."""
        result = []
        while num > 0:
            result.append(self.chars[num % self.base])
            num //= self.base
        return ''.join(reversed(result))

    def shorten(self, original_url):
        """Shorten the given URL and return the short code."""
        if original_url in self.reverse_map:
            return self.reverse_map[original_url]

        short_code = self.encode(self.counter)
        self.url_map[short_code] = original_url
        self.reverse_map[original_url] = short_code
        self.counter += 1
        self.save_data()
        return short_code

    def retrieve(self, short_code):
        """Return the original URL given the short code."""
        return self.url_map.get(short_code, None)

    def save_data(self):
        """Save the mappings to a JSON file."""
        try:
            with open(self.db_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "url_map": self.url_map,
                    "reverse_map": self.reverse_map,
                    "counter": self.counter
                }, f, indent=4)
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def load_data(self):
        """Load saved mappings from the JSON file."""
        if not os.path.exists(self.db_file):
            return  # Nothing to load

        try:
            with open(self.db_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.url_map = data.get("url_map", {})
                self.reverse_map = data.get("reverse_map", {})
                self.counter = data.get("counter", 1000)
        except Exception as e:
            print(f"❌ Error loading data: {e}")

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    shortener = URLShortener()

    print("""
🔗 URL SHORTENER CLI APP
---------------------------
1. Shorten a URL
2. Retrieve original URL
3. Exit
""")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            original = input("🔸 Enter the original URL: ").strip()
            if not original.startswith("http"):
                print("⚠️ Please enter a valid URL (starting with http/https)\n")
                continue

            short = shortener.shorten(original)
            print(f"✅ Shortened URL Code: {short}\n")

        elif choice == '2':
            code = input("🔹 Enter short code: ").strip()
            original = shortener.retrieve(code)
            if original:
                print(f"🔁 Original URL: {original}\n")
            else:
                print("❌ Short code not found!\n")

        elif choice == '3':
            print("👋 Exiting URL Shortener. Goodbye!")
            break

        else:
            print("⚠️ Invalid option. Please choose 1, 2, or 3.\n")

# -----------------------------------------------
# ▶️ Run the App
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of URL Shortener CLI App