from fpdf import FPDF
import sys
from PIL import Image


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image(r"shirtificate.png", 10, 67, 190)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 35)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 50, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(r=255,g=255,b=255)

name = input("Name: ")

pdf.cell(0, 200, f"{name} took CS50", align="c")
pdf.output("shirtificate.pdf")


