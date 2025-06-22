# -----------------------------------------------
# 📡 Morse Code Translator using OOP & File Handling
# -----------------------------------------------

from datetime import datetime

# -----------------------------------------------
# 📖 Morse Code Dictionary (International Standard)
# -----------------------------------------------

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--',
    '4': '....-', '5': '.....', '6': '-....','7': '--...',
    '8': '---..', '9': '----.',
    '&': '.-...',  '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--',
    '.': '.-.-.-', '-': '-....-', '+': '.-.-.', '"': '.-..-.',
    '?': '..--..', '/': '-..-.', "'": '.----.',
    ' ': '/'  # Using '/' as a word separator
}

# -----------------------------------------------
# 🔁 Reverse Dictionary for Morse to Text
# -----------------------------------------------

MORSE_TO_TEXT_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# -----------------------------------------------
# 🧩 MorseCodeTranslator Class - Core Logic
# -----------------------------------------------

class MorseCodeTranslator:
    def __init__(self, log_file="morse_log.txt"):
        self.log_file = log_file

    def text_to_morse(self, message):
        """
        Convert plain text to Morse code.
        """
        morse_code = []
        for char in message.upper():
            if char in MORSE_CODE_DICT:
                morse_code.append(MORSE_CODE_DICT[char])
            else:
                # Handle unsupported characters gracefully
                morse_code.append('[?]')
        return ' '.join(morse_code)

    def morse_to_text(self, morse_code):
        """
        Convert Morse code to plain text.
        """
        words = morse_code.strip().split(' / ')
        decoded_words = []

        for word in words:
            letters = word.strip().split()
            decoded_word = ''.join(MORSE_TO_TEXT_DICT.get(code, '?') for code in letters)
            decoded_words.append(decoded_word)

        return ' '.join(decoded_words)

    def log_translation(self, input_data, output_data, mode):
        """
        Log the translation with timestamp.
        """
        try:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] [{mode}]\nInput: {input_data}\nOutput: {output_data}\n\n")
        except Exception as e:
            print(f"❌ Error writing to log file: {e}")

# -----------------------------------------------
# 🖥️ CLI Interface - User Interaction
# -----------------------------------------------

def main():
    print("""
📡 MORSE CODE TRANSLATOR
-------------------------
Options:
1. Text to Morse Code
2. Morse Code to Text
3. Exit
    """)

    translator = MorseCodeTranslator()

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            morse = translator.text_to_morse(text)
            print(f"🔤 Text to Morse: {morse}")
            translator.log_translation(text, morse, "Text → Morse")

        elif choice == '2':
            morse = input("Enter Morse code (use '/' for space between words): ")
            text = translator.morse_to_text(morse)
            print(f"📡 Morse to Text: {text}")
            translator.log_translation(morse, text, "Morse → Text")

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------

if __name__ == "__main__":
    main()
# -----------------------------------------------
# End of Morse Code Translator