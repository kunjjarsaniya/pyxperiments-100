# -----------------------------------------------
# 📝 CLI Notepad App using OOP & File Handling
# -----------------------------------------------

import os
from datetime import datetime

# -----------------------------------------------
# 📦 Note Class – Represents a single note
# -----------------------------------------------

class Note:
    def __init__(self, title, content, timestamp=None):
        """
        Initialize a note with a title, content, and timestamp.
        """
        self.title = title
        self.content = content
        self.timestamp = timestamp if timestamp else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        """
        Display the note in a readable format.
        """
        return f"\n📝 {self.title} (Created: {self.timestamp})\n{'-'*50}\n{self.content}\n"

# -----------------------------------------------
# 📒 Notepad Class – Manages notes with file handling
# -----------------------------------------------

class Notepad:
    def __init__(self, filename="notes.txt"):
        """
        Initialize the Notepad with a storage file.
        """
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        """
        Load notes from the file into memory.
        """
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = f.read().strip().split('\n\n%%\n\n')  # Separator between notes
                for block in data:
                    if block:
                        lines = block.strip().split('\n')
                        title_line = lines[0]
                        timestamp_line = lines[1]
                        content = '\n'.join(lines[2:])
                        title = title_line.replace('Title: ', '')
                        timestamp = timestamp_line.replace('Timestamp: ', '')
                        self.notes.append(Note(title, content, timestamp))
        except Exception as e:
            print(f"❌ Error loading notes: {e}")

    def save_notes(self):
        """
        Save all notes to the file.
        """
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                for note in self.notes:
                    f.write(f"Title: {note.title}\n")
                    f.write(f"Timestamp: {note.timestamp}\n")
                    f.write(f"{note.content}\n\n%%\n\n")
        except Exception as e:
            print(f"❌ Error saving notes: {e}")

    def create_note(self, title, content):
        """
        Create and store a new note.
        """
        note = Note(title, content)
        self.notes.append(note)
        self.save_notes()
        print("✅ Note saved successfully.\n")

    def view_notes(self):
        """
        Display all stored notes.
        """
        if not self.notes:
            print("📭 No notes found.\n")
            return

        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note.title} (Created: {note.timestamp})")
        print()

    def show_note(self, index):
        """
        Show full content of a specific note by index.
        """
        if 0 <= index < len(self.notes):
            print(self.notes[index])
        else:
            print("❌ Invalid note index.\n")

    def delete_note(self, index):
        """
        Delete a note by index.
        """
        if 0 <= index < len(self.notes):
            removed = self.notes.pop(index)
            self.save_notes()
            print(f"🗑️ Deleted note: {removed.title}\n")
        else:
            print("❌ Invalid note index.\n")

    def edit_note(self, index, new_content):
        """
        Edit the content of a note.
        """
        if 0 <= index < len(self.notes):
            self.notes[index].content = new_content
            self.notes[index].timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.save_notes()
            print("✏️ Note updated.\n")
        else:
            print("❌ Invalid note index.\n")

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    notepad = Notepad()

    print("""
📝 SIMPLE CLI NOTEPAD
------------------------
1. Create a Note
2. View Notes List
3. Read a Note
4. Edit a Note
5. Delete a Note
6. Exit
""")

    while True:
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            title = input("📌 Enter note title: ").strip()
            print("🖊️  Enter your content (end with an empty line):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            content = '\n'.join(lines)
            notepad.create_note(title, content)

        elif choice == '2':
            notepad.view_notes()

        elif choice == '3':
            try:
                index = int(input("🔍 Enter note number to read: ")) - 1
                notepad.show_note(index)
            except ValueError:
                print("⚠️ Invalid input.\n")

        elif choice == '4':
            try:
                index = int(input("✏️ Enter note number to edit: ")) - 1
                print("🖊️ Enter new content (end with an empty line):")
                new_lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    new_lines.append(line)
                new_content = '\n'.join(new_lines)
                notepad.edit_note(index, new_content)
            except ValueError:
                print("⚠️ Invalid input.\n")

        elif choice == '5':
            try:
                index = int(input("🗑️ Enter note number to delete: ")) - 1
                notepad.delete_note(index)
            except ValueError:
                print("⚠️ Invalid input.\n")

        elif choice == '6':
            print("👋 Exiting Notepad. Have a productive day!")
            break

        else:
            print("⚠️ Please enter a valid option (1-6).\n")

# -----------------------------------------------
# ▶️ Run the Notepad App
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Notepad App