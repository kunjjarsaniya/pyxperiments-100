# -----------------------------------------------
# 🔍 Binary Search Implementation using OOP & File Handling
# -----------------------------------------------

from datetime import datetime

# -----------------------------------------------
# 📦 BinarySearchTool Class – Handles core logic
# -----------------------------------------------

class BinarySearchTool:
    def __init__(self, data_list, log_file='binary_search_log.txt'):
        """
        Initialize with a sorted list and log file.
        """
        self.data = sorted(data_list)
        self.log_file = log_file

    def binary_search(self, target):
        """
        Perform binary search for the target value.
        Returns index if found, else -1.
        """
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = self.data[mid]

            if guess == target:
                return mid  # Found
            elif guess < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1  # Not found

    def log_result(self, target, result_index):
        """
        Log the search result with timestamp to a file.
        """
        try:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                status = f"Found at index {result_index}" if result_index != -1 else "Not Found"
                file.write(f"[{timestamp}] Searched for {target} → {status}\n")
        except Exception as e:
            print(f"❌ Error writing to log file: {e}")

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    print("""
🔍 BINARY SEARCH TOOL
----------------------
This tool searches a number in a sorted list using binary search.
You can modify the list inside the script.
    """)

    # Sample sorted data list – You can modify this
    sample_list = [2, 5, 8, 10, 12, 15, 18, 21, 26, 30, 35, 40]

    print(f"📄 Data List: {sample_list}\n")

    # Initialize the search tool
    search_tool = BinarySearchTool(sample_list)

    while True:
        user_input = input("Enter a number to search (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("👋 Exiting Binary Search Tool. Goodbye!")
            break

        try:
            number = int(user_input)
            result = search_tool.binary_search(number)

            if result != -1:
                print(f"✅ {number} found at index {result}.\n")
            else:
                print(f"❌ {number} not found in the list.\n")

            search_tool.log_result(number, result)

        except ValueError:
            print("⚠️ Please enter a valid integer.\n")

# -----------------------------------------------
# ▶️ Run the Binary Search Tool
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Binary Search Tool