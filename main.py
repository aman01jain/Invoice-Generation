import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")
print(filepaths)

for file in filepaths:
    df  = pd.read_excel(file, sheet_name = "Sheet 1")
    print(df)
    PDF = FPDF(orientation= "P", unit= "mm", format= "A4")
    PDF.add_page()
    filename= Path(file).stem
    invoice_no = filename.split("-")[0]
    PDF.set_font(family="Times", size = 16, style= "B")
    PDF.cell(w= 50,h=8, txt=f'Invoice No.{invoice_no}')
    PDF.output(f"pdf/{filename}.pdf")

