# -----------------------------------------------
# 📚 Library Management CLI App using OOP & File I/O
# -----------------------------------------------

import os  # For file checking
import json  # For saving/loading data


# -----------------------------------------------
# 📕 Book Class - Represents a single book
# -----------------------------------------------

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, year, is_borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed

    def to_dict(self):
        """Convert book object to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'is_borrowed': self.is_borrowed
        }

    def __str__(self):
        """Format the book details nicely."""
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"📘 {self.title} by {self.author} ({self.year}) - {status}"


# -----------------------------------------------
# 📖 Library Class - Manages book operations
# -----------------------------------------------

class Library:
    """Handles all library operations and file handling."""

    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.books = []  # List to store book objects
        self.load_books()  # Load existing books

    def load_books(self):
        """Load books from file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    self.books = [Book(**book) for book in data]
            except Exception as e:
                print(f"⚠️ Error loading books: {e}")

    def save_books(self):
        """Save current list of books to file in JSON format."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([b.to_dict() for b in self.books], file, indent=4)
        except Exception as e:
            print(f"⚠️ Error saving books: {e}")

    def add_book(self, title, author, year):
        """Add a new book to the library."""
        self.books.append(Book(title, author, year))
        print("✅ Book added successfully!")

    def view_books(self):
        """Display all books in the library."""
        if not self.books:
            print("📭 No books in the library.")
        else:
            print("\n📚 All Books:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")

    def borrow_book(self, title):
        """Mark a book as borrowed by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print("❌ This book is already borrowed.")
                else:
                    book.is_borrowed = True
                    print("📦 Book borrowed successfully.")
                return
        print("❌ Book not found.")

    def return_book(self, title):
        """Return a previously borrowed book."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print("📚 This book was not borrowed.")
                else:
                    book.is_borrowed = False
                    print("✅ Book returned successfully.")
                return
        print("❌ Book not found.")

    def delete_book(self, title):
        """Delete a book by title."""
        original_count = len(self.books)
        self.books = [b for b in self.books if b.title.lower() != title.lower()]
        if len(self.books) < original_count:
            print("🗑️ Book deleted successfully.")
        else:
            print("❌ Book not found.")

    def menu(self):
        # -----------------------------------------------
        # 🧭 CLI Menu Loop for User Interaction
        # -----------------------------------------------
        while True:
            print("\n========= 📖 Library Menu =========")
            print("1. Add Book")
            print("2. View Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Delete Book")
            print("6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                year = input("Enter published year: ")
                self.add_book(title, author, year)

            elif choice == '2':
                self.view_books()

            elif choice == '3':
                title = input("Enter title of book to borrow: ")
                self.borrow_book(title)

            elif choice == '4':
                title = input("Enter title of book to return: ")
                self.return_book(title)

            elif choice == '5':
                title = input("Enter title of book to delete: ")
                self.delete_book(title)

            elif choice == '6':
                self.save_books()  # Save changes before exit
                print("💾 Library saved. Goodbye!")
                break

            else:
                print("⚠️ Invalid option. Please enter 1 to 6.")


# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------
if __name__ == "__main__":
    library = Library()
    library.menu()
# -----------------------------------------------
# 📚 Library Management CLI App using OOP & File I/O