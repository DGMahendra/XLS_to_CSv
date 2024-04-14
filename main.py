import pandas as pd
import os

def xlsx_to_csv(xlsx_file_path, output_folder):
    # Load the XLSX file into a pandas ExcelFile object
    xls = pd.ExcelFile(xlsx_file_path)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over each sheet in the XLSX file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a pandas DataFrame
        df = pd.read_excel(xls, sheet_name)
        
        # Extract the filename from the sheet name
        filename = f"{sheet_name}.csv"
        
        # Construct the full output path for the CSV file
        output_path = os.path.join(output_folder, filename)
        
        # Write the DataFrame to a CSV file
        df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Path to the input XLSX file
    xlsx_file_path = "example.xlsx"
    
    # Output folder where CSV files will be saved
    output_folder = "output_csv"
    
    # Convert XLSX to CSV
    xlsx_to_csv(xlsx_file_path, output_folder)
