# -----------------------------------------------
# 🔗 Linked List Implementation using OOP in Python
# -----------------------------------------------

from datetime import datetime

# -----------------------------------------------
# 📦 Node Class – Represents a single node in the list
# -----------------------------------------------

class Node:
    def __init__(self, data):
        """
        Initialize a node with data and reference to next node (None initially).
        """
        self.data = data
        self.next = None

# -----------------------------------------------
# 🧩 LinkedList Class – Core Linked List Operations
# -----------------------------------------------

class LinkedList:
    def __init__(self, log_file="linked_list_log.txt"):
        """
        Initialize the linked list and log file path.
        """
        self.head = None
        self.log_file = log_file

    def insert_at_end(self, data):
        """Insert a node at the end of the linked list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.log(f"Inserted {data} as head node.")
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        self.log(f"Inserted {data} at the end.")

    def delete_node(self, key):
        """Delete the first occurrence of a node with the given value."""
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if not current:
            self.log(f"Value {key} not found in list.")
            return False

        if not previous:
            self.head = current.next  # Delete head
        else:
            previous.next = current.next  # Bypass the node

        self.log(f"Deleted node with value {key}.")
        return True

    def search(self, key):
        """Search for a value in the list and return True if found."""
        current = self.head
        position = 0
        while current:
            if current.data == key:
                self.log(f"Value {key} found at position {position}.")
                return True
            current = current.next
            position += 1

        self.log(f"Value {key} not found.")
        return False

    def display(self):
        """Display all nodes in the linked list."""
        if not self.head:
            print("📭 Linked list is empty.")
            return

        current = self.head
        print("🔗 Linked List:", end=" ")
        while current:
            print(f"[{current.data}]", end=" → ")
            current = current.next
        print("None")

    def log(self, message):
        """Log messages with timestamps to a file."""
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {message}\n")
        except Exception as e:
            print(f"❌ Error writing to log: {e}")

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    ll = LinkedList()

    print("""
🔗 LINKED LIST APP
---------------------
Available Operations:
1. Insert Node at End
2. Delete Node by Value
3. Search for a Value
4. Display List
5. Exit
""")

    while True:
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            data = input("Enter value to insert: ").strip()
            ll.insert_at_end(data)
            print("✅ Node inserted.\n")

        elif choice == '2':
            key = input("Enter value to delete: ").strip()
            if ll.delete_node(key):
                print("🗑️ Node deleted.\n")
            else:
                print("❌ Value not found in list.\n")

        elif choice == '3':
            key = input("Enter value to search: ").strip()
            found = ll.search(key)
            print("🔍 Found!\n" if found else "❌ Not found.\n")

        elif choice == '4':
            ll.display()
            print()

        elif choice == '5':
            print("👋 Exiting Linked List App.")
            break

        else:
            print("⚠️ Invalid choice. Please enter 1 to 5.\n")

# -----------------------------------------------
# ▶️ Run the Linked List Program
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Linked List Implementation