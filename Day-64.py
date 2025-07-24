# -------------------------------------------------------------
# 📑 PDF Merger Tool with CSV Logging (OOP + Pandas)
# -------------------------------------------------------------

# pip install PyPDF2 pandas

from PyPDF2 import PdfMerger
import pandas as pd
import os
import datetime


# -------------------------------------------------------------
# 📦 PDFMergerTool – Handles merging of PDFs
# -------------------------------------------------------------

class PDFMergerTool:
    """Merges multiple PDF files into one."""

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.merge_log = []  # To store merge info

    def merge_pdfs(self, file_list, output_filename):
        """Merge given list of PDF files and save output."""
        if not file_list or len(file_list) < 2:
            raise ValueError("Provide at least two PDF files to merge.")

        merger = PdfMerger()

        try:
            for file in file_list:
                if not os.path.exists(file) or not file.lower().endswith(".pdf"):
                    raise FileNotFoundError(f"Invalid file: {file}")
                merger.append(file)
                self.merge_log.append({
                    "filename": os.path.basename(file),
                    "filepath": os.path.abspath(file)
                })

            output_path = os.path.join(self.output_dir, output_filename)
            merger.write(output_path)
            merger.close()
            print(f"✅ Merged PDF saved at: {output_path}")
            return output_path

        except Exception as e:
            raise Exception(f"Failed to merge PDFs: {e}")

    def save_merge_log_csv(self, log_filename="merge_log.csv"):
        """Save a CSV log of merged files."""
        if not self.merge_log:
            print("⚠️ No merge log to save.")
            return None

        df_log = pd.DataFrame(self.merge_log)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = os.path.join(self.output_dir, f"{timestamp}_{log_filename}")

        try:
            df_log.to_csv(log_path, index=False, encoding="utf-8")
            print(f"📝 Merge log saved at: {log_path}")
            return log_path
        except Exception as e:
            raise Exception(f"Failed to save merge log: {e}")


# -------------------------------------------------------------
# 🚀 Main Application Logic
# -------------------------------------------------------------

def main():
    print("📑 PDF Merger Tool with CSV Logging")

    # Prompt user for PDF files
    files = []
    while True:
        file = input("Enter path to a PDF file (or leave blank to finish): ").strip()
        if not file:
            break
        files.append(file)

    if len(files) < 2:
        print("❌ Need at least two PDF files to merge.")
        return

    output_name = input("Enter name for merged PDF file (e.g., merged.pdf): ").strip()
    if not output_name.endswith(".pdf"):
        output_name += ".pdf"

    try:
        merger = PDFMergerTool()
        merged_file = merger.merge_pdfs(files, output_name)
        log_file = merger.save_merge_log_csv()
        print("🎯 All done!")
    except Exception as e:
        print(f"❌ Error: {e}")


# -------------------------------------------------------------
# 📍 Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()

# End of PDF Merger Tool 📑
