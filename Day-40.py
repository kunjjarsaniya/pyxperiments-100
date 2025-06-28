# -----------------------------------------------
# 🧪 Code Syntax Checker using OOP & File Handling
# -----------------------------------------------

import os
import traceback

# -----------------------------------------------
# 📦 CodeChecker Class – Core syntax check logic
# -----------------------------------------------

class CodeChecker:
    def __init__(self, file_path):
        """
        Initialize with the file path to be checked.
        """
        self.file_path = file_path
        self.code = ""

    def load_code(self):
        """
        Load code from the given Python (.py) file.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("❌ File not found!")

        if not self.file_path.endswith('.py'):
            raise ValueError("⚠️ Only Python (.py) files are supported.")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.code = file.read()
        except Exception as e:
            raise IOError(f"❌ Error reading file: {e}")

    def check_syntax(self):
        """
        Check the syntax of the loaded Python code using built-in compile().
        """
        try:
            # Try compiling the code to bytecode (syntax check only)
            compile(self.code, self.file_path, 'exec')
            return True, "✅ No syntax errors found!"
        except SyntaxError as e:
            # Return line number and syntax message
            return False, f"❌ Syntax Error on line {e.lineno}: {e.msg}"
        except Exception as e:
            # Handle other non-syntax-related exceptions
            return False, f"❌ Error: {str(e)}"

# -----------------------------------------------
# 🖥️ CLI Interface – User Interaction
# -----------------------------------------------

def main():
    print("""
🧪 PYTHON SYNTAX CHECKER
----------------------------
This tool checks the syntax of a Python (.py) file.
""")

    file_path = input("📄 Enter path to Python file: ").strip()

    checker = CodeChecker(file_path)

    try:
        checker.load_code()
        is_valid, message = checker.check_syntax()
        print("\n" + message + "\n")

    except FileNotFoundError as fnf_err:
        print(fnf_err)
    except ValueError as val_err:
        print(val_err)
    except IOError as io_err:
        print(io_err)
    except Exception as ex:
        print("❌ An unexpected error occurred:")
        print(traceback.format_exc())

# -----------------------------------------------
# ▶️ Run the Syntax Checker
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Python Syntax Checker