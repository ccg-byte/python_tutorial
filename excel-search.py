import os
import openpyxl
import re

def search_string_in_files(directory, search_string, excel_file):
    # Create a new Excel workbook
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Search Results"
    sheet['A1'] = "File Name"
    
    # Write headers for match lines in Excel
    for i in range(len(search_string)):
        sheet.cell(row=1, column=i+2, value="Match Line " + str(i+1))
    
    # Loop through each file in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            sheet.append([os.path.relpath(file_path, directory)])
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    matches = []
                    # Search for the string in each line of the file
                    for line in lines:
                        if re.search(search_string, line):
                            matches.append(line.strip())
                    # Write match lines to Excel
                    for match in matches:
                        sheet.append(['', match])
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    
    # Save the Excel file
    wb.save(excel_file)
    print(f"Search results saved to {excel_file}")

# Example usage:
search_string_in_files("/path/to/directory", "your_search_string", "search_results.xlsx")
