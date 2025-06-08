# -----------------------------------------------
# 😄 Contact Book Program using OOP and File Saving
# -----------------------------------------------

import os  # For checking if file exists
import json  # For saving/loading data in JSON format

# -----------------------------------------------
# 📦 Contact Class - Represents a single contact
# -----------------------------------------------

class Contact:
    """Defines a contact with name, phone, and email."""

    def __init__(self, name, phone, email):
        # Initialize contact attributes
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        # Convert contact object to dictionary for saving as JSON
        return {'name': self.name, 'phone': self.phone, 'email': self.email}

    def __str__(self):
        # Format contact nicely when printed
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


# -----------------------------------------------
# 📚 ContactBook Class - Handles all operations
# -----------------------------------------------

class ContactBook:
    """Manages a list of Contact objects and handles file operations."""

    def __init__(self, filename="contacts.txt"):
        self.filename = filename  # File to save/load contacts
        self.contacts = []  # Store list of contacts
        self.load_contacts()  # Load existing contacts from file

    def load_contacts(self):
        # Load contacts from file if it exists
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    # Convert each dictionary to Contact object
                    self.contacts = [Contact(**contact) for contact in data]
            except Exception as e:
                print(f"⚠️ Error loading contacts: {e}")

    def save_contacts(self):
        # Save all contacts to file in JSON format
        try:
            with open(self.filename, "w") as file:
                json.dump([c.to_dict() for c in self.contacts], file, indent=4)
        except Exception as e:
            print(f"⚠️ Error saving contacts: {e}")

    def add_contact(self, name, phone, email):
        # Add a new contact to the list
        self.contacts.append(Contact(name, phone, email))
        print("✅ Contact added successfully!")

    def view_contacts(self):
        # Display all saved contacts
        if not self.contacts:
            print("📭 No contacts found.")
        else:
            print("\n📒 All Contacts:")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"\nContact {idx}:\n{contact}")

    def search_contact(self, keyword):
        # Search contacts by name or phone
        found = [c for c in self.contacts if keyword.lower() in c.name.lower() or keyword in c.phone]
        if found:
            print(f"\n🔍 Found {len(found)} contact(s):")
            for contact in found:
                print(f"\n{contact}")
        else:
            print("❌ No matching contact found.")

    def delete_contact(self, name):
        # Delete a contact by name (case-insensitive)
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        if len(self.contacts) < original_count:
            print("🗑️ Contact deleted successfully.")
        else:
            print("❌ Contact not found.")

    def menu(self):
        # -----------------------------------------------
        # 🧭 Menu Method - User interaction loop
        # -----------------------------------------------
        while True:
            print("\n========= 📇 Contact Book Menu =========")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            # Handle menu choices
            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                self.add_contact(name, phone, email)

            elif choice == '2':
                self.view_contacts()

            elif choice == '3':
                keyword = input("Enter name or phone to search: ")
                self.search_contact(keyword)

            elif choice == '4':
                name = input("Enter name to delete: ")
                self.delete_contact(name)

            elif choice == '5':
                self.save_contacts()  # Save contacts before exiting
                print("💾 Contacts saved. Goodbye!")
                break

            else:
                print("⚠️ Invalid choice. Please enter a number between 1 and 5.")


# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------
if __name__ == "__main__":
    # Create an instance of ContactBook and start the menu
    book = ContactBook()
    book.menu()
# End of the Contact Book Program
# Thank you for using the Contact Book! 📖