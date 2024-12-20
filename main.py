import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")
print(filepaths)

for file in filepaths:
    df  = pd.read_excel(file, sheet_name = "Sheet 1")
    PDF = FPDF(orientation= "P", unit= "mm", format= "A4")
    PDF.add_page()
    filename= Path(file).stem

    invoice_no = filename.split("-")[0]
    date = filename.split("-")[1]

    PDF.set_font(family="Times", size = 16, style= "B")
    PDF.cell(w= 50,h=8, txt=f'Invoice No.{invoice_no}', ln=1)

    PDF.set_font(family="Times", size=16, style="B")
    PDF.cell(w=50,h=8, txt= f'Date {date}', ln=1)

    df = pd.read_excel(file, sheet_name="Sheet 1")

    #Add a header
    columns = df.columns
    columns = [item.replace("_"," ").title() for item in columns]
    PDF.set_font(family = "Times", size=10, style= "BI")
    PDF.set_text_color(80, 80, 80)
    PDF.cell(w=30, h=8, txt=columns[0], border=1)
    PDF.cell(w=70, h=8, txt=columns[1], border=1)
    PDF.cell(w=30, h=8, txt=columns[2], border=1)
    PDF.cell(w=30, h=8, txt=columns[3], border=1)
    PDF.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    #add rows to the table
    for index,row in df.iterrows():
        PDF.set_font(family= "Times", size=10)
        PDF.set_text_color(80,80,80)
        PDF.cell(w=30,h=8, txt = str(row["product_id"]),border=1)
        PDF.cell(w=70, h=8, txt= str(row["product_name"]), border= 1)
        PDF.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        PDF.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        PDF.cell(w=30, h=8, txt=str(row["total_price"]),border=1, ln=1)

    PDF.output(f"pdf/{filename}.pdf")

