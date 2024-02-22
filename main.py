import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("text_files/*txt")

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to title case (e.g. Cat)
    filename = Path(filepath).stem
    topic = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Courier", style="B", size=16)
    pdf.cell(w=40, h=8, txt=topic, ln=1)

    # Add the content to the PDF
    filepath = f"text_files/{topic}.txt"
    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family="Courier", style="I", size=14)
    pdf.multi_cell(w=0, h=8, txt=content)

# Produce the PDF
pdf.output("output.pdf")
