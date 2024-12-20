import pandas as pd
import glob

filepaths = glob.glob("Invoices/*.xlsx")
print(filepaths)

for file in filepaths:
    df  = pd.read_excel(file, sheet_name = "sheet 1")
    print(df)

