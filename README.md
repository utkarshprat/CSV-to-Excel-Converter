    CSV to Excel Converter:-
        This project provides a simple tool to convert CSV files to Excel format using a graphical user interface (GUI). It's designed to be user-friendly and requires no programming knowledge to operate.
    
    Features:-
        •   Load CSV Files: Easily select a CSV file through a file dialog.
        •   Save as Excel: Choose a location and name for the converted Excel file.
        •   Error Handling: Alerts you if there are issues with file selection, saving, or processing.
    
    How to Use:-
        Step 1: Install Requirements-
            Before using the tool, ensure you have the required libraries installed. You can install them using:
                        pip install pandas openpyxl
        Step 2: Run the Program
            Run the program by executing csv_gui.py:
                        python csv_gui.py
        Step 3: Convert Your File
        •   Select a CSV File:
            o   Click the "Select CSV" button.
            o   Use the file dialog to choose a CSV file from your computer.
        •   Choose Save Location:
            o   After selecting the CSV file, you will be prompted to choose a location and name for the Excel file.
        •   View Confirmation:
            o   A success message will confirm that the Excel file has been created and saved.
    
    Code Breakdown:-
    1. csv_assi.py-
        This file contains the core logic for CSV to Excel conversion:
        •    load(file): Reads a CSV file and loads it into a pandas DataFrame. It checks for errors like missing files.
        •   save_excel(data, out_file): Saves a DataFrame to an Excel file using the openpyxl engine.
        •   csv_to_xlsx(csv_file, xlsx_file): Combines the loading and saving steps to perform the entire conversion process.
    2. csv_gui.py
        This file provides the graphical user interface (GUI) for the tool:
        •   select_file(): Opens a file dialog to let the user select a CSV file and specify the Excel save location. Handles errors and displays appropriate messages.
        •   main_gui(): Sets up the GUI with instructions and a button for starting the conversion process.
    
    Example Usage:-
        Here’s what the process looks like:
        •   Run the GUI: When you execute csv_gui.py, a window will appear with instructions and a button labeled "Select CSV".
        •   Select and Save:
            o   Click "Select CSV" to choose a CSV file.
            o   Specify where you want the converted Excel file saved.
        •   Get Confirmation: After the conversion, you’ll see a message box confirming the success and showing the save location.
    
    Error Messages:-
        •   "No CSV file selected": Displayed when you don’t select a CSV file.
        •   "No output file selected": Shown if you don’t provide a location to save the Excel file.
        •   "Failed to save file": Indicates an issue during the file-saving process.
        
    Troubleshooting:-
        •   Error: "File not found": Ensure the CSV file exists and the path is correct.
        •   Error: Missing Dependencies: Make sure pandas and openpyxl are installed.

  This README is designed to help users easily understand how to set up and use the tool.

    Sample Images-

![csv_to_excel (1)](https://github.com/user-attachments/assets/ae9a0969-6b8d-4301-87ea-5959c7ce9bf2)

![csv_to_excel (2)](https://github.com/user-attachments/assets/ec2f67d2-00a8-4740-ac3f-f896fe70cfc0)

![csv_to_excel (3)](https://github.com/user-attachments/assets/3a09f55e-4026-4bc8-a21a-aff5e23255ee)

![csv_to_excel (4)](https://github.com/user-attachments/assets/abd5a428-1b23-45a5-acc4-869696be582e)

![csv_to_excel (5)](https://github.com/user-attachments/assets/7b338455-e875-4bb2-9a20-08acdcef7721)

![csv_to_excel (6)](https://github.com/user-attachments/assets/8460550a-ecce-4e48-9cb2-e63ba396fdb4)
