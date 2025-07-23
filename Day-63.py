# -------------------------------------------------------------
# 📊 Excel File Processor to CSV/JSON (OOP + Pandas)
# -------------------------------------------------------------

# pip install pandas openpyxl

import pandas as pd
import os
import json


# -------------------------------------------------------------
# 📦 ExcelProcessor – Handles reading & cleaning Excel files
# -------------------------------------------------------------

class ExcelProcessor:
    """Reads and cleans data from Excel files."""

    def __init__(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        if not filepath.endswith(('.xlsx', '.xls')):
            raise ValueError("Invalid file type. Please provide an Excel file (.xlsx or .xls).")
        self.filepath = filepath
        self.dataframe = None

    def read_excel(self, sheet_name=0):
        """Read Excel file into a DataFrame."""
        try:
            self.dataframe = pd.read_excel(self.filepath, sheet_name=sheet_name)
            print(f"✅ Excel file loaded: {self.filepath}")
            return self.dataframe
        except Exception as e:
            raise Exception(f"Failed to read Excel file: {e}")

    def clean_data(self):
        """Basic cleaning: drop empty rows/columns and fill NAs."""
        if self.dataframe is None:
            raise ValueError("Dataframe is empty. Call read_excel() first.")
        self.dataframe.dropna(how='all', inplace=True)  # Drop completely empty rows
        self.dataframe.fillna("", inplace=True)         # Fill NaNs with empty strings
        print(f"🧹 Data cleaned.")
        return self.dataframe


# -------------------------------------------------------------
# 💾 DataExporter – Handles saving files
# -------------------------------------------------------------

class DataExporter:
    """Exports data to CSV and JSON."""

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_csv(self, dataframe, filename):
        """Save DataFrame as CSV."""
        csv_path = os.path.join(self.output_dir, filename)
        try:
            dataframe.to_csv(csv_path, index=False, encoding='utf-8')
            print(f"✅ Data saved as CSV: {csv_path}")
            return csv_path
        except Exception as e:
            raise Exception(f"Failed to save CSV: {e}")

    def save_json(self, dataframe, filename):
        """Save DataFrame as JSON."""
        json_path = os.path.join(self.output_dir, filename)
        try:
            dataframe.to_json(json_path, orient='records', indent=4, force_ascii=False)
            print(f"✅ Data saved as JSON: {json_path}")
            return json_path
        except Exception as e:
            raise Exception(f"Failed to save JSON: {e}")


# -------------------------------------------------------------
# 🚀 Main Application Logic
# -------------------------------------------------------------

def main():
    print("📊 Excel File Processor to CSV & JSON")
    excel_file = input("Enter path to Excel file (.xlsx or .xls): ").strip()

    try:
        # Instantiate classes
        processor = ExcelProcessor(excel_file)
        exporter = DataExporter()

        # Read and clean data
        df = processor.read_excel()
        df_clean = processor.clean_data()

        # Save outputs
        base_name = os.path.splitext(os.path.basename(excel_file))[0]
        exporter.save_csv(df_clean, f"{base_name}.csv")
        exporter.save_json(df_clean, f"{base_name}.json")

        print("🎯 Processing complete!")

    except Exception as e:
        print(f"❌ Error: {e}")


# -------------------------------------------------------------
# 📍 Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()

# End of Excel Processor 📊
