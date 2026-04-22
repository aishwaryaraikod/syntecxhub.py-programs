import pandas as pd
print("📊 CSV to Excel Converter")
try:
    # Step 1: Read CSV file
    file_path = "data.csv"   # since file is in same folder
    data = pd.read_csv(file_path)
    print("\nCSV Data:")
    print(data)
    # Step 2: Save as Excel
    output_file = "output.xlsx"
    data.to_excel(output_file, index=False)
    print("\n✅ Successfully converted to Excel!")
    print("File saved as:", output_file)
except Exception as e:
    print("Error:", e)