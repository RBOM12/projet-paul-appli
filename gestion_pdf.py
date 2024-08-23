from tkinter import filedialog

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


def lien_pdf(datag,datad):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        # Generate PDF
        generate_pdf(file_path, datag, datad)


def generate_pdf(filename, datag, datad):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    c.setFillColorRGB(1, 0, 0)
    c.setFont("Helvetica", 20)
    c.drawString(100, height - 100, "Résultats:")
    y_position = height - 120
    y_positiond = y_position - 20
    y_positiong = y_position - 20
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0, 0, 0)
    for key, value in datag.items():
        c.drawString(100, y_positiong, f"{key}: {value}")
        y_positiong -= 20

    for key, value in datad.items():
        c.drawString(400, y_positiond, f"{key}: {value}")
        y_positiond -= 20
    c.showPage()
    c.save()
