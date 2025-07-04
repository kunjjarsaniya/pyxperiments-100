# pip install cryptography

# -------------------------------------------------------------
# 🔐 File Encryptor & Decryptor GUI App using Tkinter + OOP
# -------------------------------------------------------------

import os
from tkinter import filedialog, messagebox, Tk, Button, Label, Entry
from cryptography.fernet import Fernet


# -------------------------------------------------------------
# 🔑 CryptoManager Class – Handles Encryption & Decryption
# -------------------------------------------------------------

class CryptoManager:
    """Handles key generation, encryption, and decryption logic."""

    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        self.key = None
        self.load_or_create_key()

    def load_or_create_key(self):
        # Load existing key or generate a new one
        if os.path.exists(self.key_file):
            try:
                with open(self.key_file, 'rb') as file:
                    self.key = file.read()
            except Exception as e:
                raise Exception(f"Error loading key: {e}")
        else:
            self.key = Fernet.generate_key()
            try:
                with open(self.key_file, 'wb') as file:
                    file.write(self.key)
            except Exception as e:
                raise Exception(f"Error creating key file: {e}")

    def encrypt_file(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                data = f.read()

            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)

            encrypted_file = filepath + '.encrypted'
            with open(encrypted_file, 'wb') as f:
                f.write(encrypted)

            return encrypted_file

        except Exception as e:
            raise Exception(f"Encryption failed: {e}")

    def decrypt_file(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                encrypted_data = f.read()

            fernet = Fernet(self.key)
            decrypted = fernet.decrypt(encrypted_data)

            original_name = filepath.replace('.encrypted', '')
            with open(original_name, 'wb') as f:
                f.write(decrypted)

            return original_name

        except Exception as e:
            raise Exception(f"Decryption failed: {e}")


# -------------------------------------------------------------
# 🖼️ FileEncryptorApp Class – Tkinter GUI + Logic Integration
# -------------------------------------------------------------

class FileEncryptorApp:
    """Manages GUI interactions and uses CryptoManager to perform encryption/decryption."""

    def __init__(self, master):
        self.master = master
        self.master.title("🔐 File Encryptor & Decryptor")
        self.master.geometry("400x300")
        self.crypto = CryptoManager()

        self.create_widgets()

    def create_widgets(self):
        # App title
        Label(self.master, text="File Encryptor/Decryptor", font=("Arial", 16)).pack(pady=20)

        # Encrypt button
        Button(self.master, text="Encrypt File", font=("Arial", 12),
               command=self.encrypt_action).pack(pady=10)

        # Decrypt button
        Button(self.master, text="Decrypt File", font=("Arial", 12),
               command=self.decrypt_action).pack(pady=10)

        # Show key location
        Label(self.master, text=f"Key File: {self.crypto.key_file}", font=("Arial", 8)).pack(side="bottom", pady=10)

    def encrypt_action(self):
        # Select and encrypt a file
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if file_path:
            try:
                encrypted_file = self.crypto.encrypt_file(file_path)
                messagebox.showinfo("Success", f"✅ File encrypted as:\n{encrypted_file}")
            except Exception as e:
                messagebox.showerror("Encryption Error", str(e))

    def decrypt_action(self):
        # Select and decrypt a file
        file_path = filedialog.askopenfilename(title="Select File to Decrypt", filetypes=[("Encrypted Files", "*.encrypted")])
        if file_path:
            try:
                decrypted_file = self.crypto.decrypt_file(file_path)
                messagebox.showinfo("Success", f"🔓 File decrypted as:\n{decrypted_file}")
            except Exception as e:
                messagebox.showerror("Decryption Error", str(e))


# -------------------------------------------------------------
# 🚀 Program Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    root = Tk()
    app = FileEncryptorApp(root)
    root.mainloop()

# End of File Encryptor/Decryptor App
# Stay safe and encrypt wisely! 🛡️
