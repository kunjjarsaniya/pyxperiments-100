# -----------------------------------------------
# 📂 File Organizer by Extension using OOP & File Handling
# -----------------------------------------------

import os
import shutil
from datetime import datetime

# -----------------------------------------------
# 🗂️ Organizer Class – Core Logic for organizing files
# -----------------------------------------------

class FileOrganizer:
    def __init__(self, directory):
        """
        Initialize with the target directory to organize.
        :param directory: Path to the directory to organize
        """
        self.directory = directory
        self.log_file = "organizer_log.txt"

    def organize(self):
        """
        Organize files by their extensions into folders.
        """
        # Check if directory exists
        if not os.path.isdir(self.directory):
            raise NotADirectoryError(f"❌ Directory '{self.directory}' does not exist.")

        files_moved = 0

        try:
            # Iterate through items in directory
            for item in os.listdir(self.directory):
                full_path = os.path.join(self.directory, item)

                # Process only files (skip folders)
                if os.path.isfile(full_path):
                    # Get file extension without dot, lowercase for consistency
                    ext = os.path.splitext(item)[1][1:].lower()

                    # If no extension, use 'no_extension' folder
                    folder_name = ext if ext else "no_extension"
                    folder_path = os.path.join(self.directory, folder_name)

                    # Create folder if it doesn't exist
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                        print(f"📁 Created folder: {folder_path}")

                    # Move the file to the folder
                    dest_path = os.path.join(folder_path, item)
                    shutil.move(full_path, dest_path)
                    print(f"✅ Moved '{item}' to '{folder_name}/'")
                    files_moved += 1

            # Log the result
            self.log_result(files_moved)
            print(f"\n🎉 Organizing complete! Total files moved: {files_moved}")

        except PermissionError:
            print("❌ Permission denied. Please run the program with appropriate permissions.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

    def log_result(self, files_moved):
        """
        Log the organizing result with timestamp.
        :param files_moved: Number of files moved
        """
        try:
            with open(self.log_file, "a") as log:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.write(f"[{now}] Organized '{self.directory}': {files_moved} files moved.\n")
        except Exception as e:
            print(f"❌ Failed to write to log file: {e}")


# -----------------------------------------------
# 🖥️ CLI Interface – Main program flow
# -----------------------------------------------

def main():
    print("""
📂 FILE ORGANIZER BY EXTENSION
------------------------------
Organizes all files in the specified directory into folders based on their extensions.

Example:
- picture.jpg → jpg/picture.jpg
- document.pdf → pdf/document.pdf
- README (no extension) → no_extension/README
""")

    directory = input("Enter the full path of the directory to organize: ").strip()

    organizer = FileOrganizer(directory)

    try:
        organizer.organize()
    except NotADirectoryError as nde:
        print(nde)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of File Organizer Program