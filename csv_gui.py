import tkinter as tk
from tkinter import filedialog, messagebox
from csv_assi import csv_to_xlsx

# Open file dialog and handle CSV to Excel conversion
def select_file():
    csv_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_file:
        xlsx_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if xlsx_file:
            try:
                # Perform the conversion
                csv_to_xlsx(csv_file, xlsx_file)
                messagebox.showinfo("Success", f"CSV successfully converted to Excel!\nFile saved at:\n{xlsx_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file. Error: {e}")
        else:
            messagebox.showwarning("Warning", "No output file selected.")
    else:
        messagebox.showwarning("Warning", "No CSV file selected.")

# Set up the main GUI
def main_gui():
    root = tk.Tk()
    root.title("CSV to Excel")
    root.geometry("400x200")

    # Instructions label
    label = tk.Label(root, text="Select a CSV file to convert to Excel.", justify='center')
    label.pack(pady=20)

    # Button to open file dialog
    button = tk.Button(root, text="Select CSV", command=select_file)
    button.pack(pady=10)

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    main_gui()
