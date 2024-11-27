import pandas as pd  # Library for working with CSV and Excel files

# Load a CSV file
def load(file):
    try:
        data = pd.read_csv(file)
        print(f"CSV '{file}' loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
        return None

# Save data to an Excel file
def save_excel(data, out_file):
    try:
        with pd.ExcelWriter(out_file, engine='openpyxl') as writer:
            data.to_excel(writer, index=False)
        print(f"Excel saved as '{out_file}'.")
    except Exception as e:
        print(f"Error saving Excel: {e}")

# Convert CSV to Excel
def csv_to_xlsx(csv_file, xlsx_file):
    data = load(csv_file)
    if data is None:
        return

    save_excel(data, xlsx_file)
