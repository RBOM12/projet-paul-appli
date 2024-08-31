from tkinter import filedialog
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, BaseDocTemplate, Frame, \
    PageTemplate
from reportlab.lib.enums import TA_CENTER

def lien_pdf(datag, datad, info, lentille, psc_g, psc_d, tonus_g, tonus_d, prisme_g, prisme_d,
             lipide_g, lipide_d, lacrymale_g, lacrymale_d, particularite, dhiv_d,dhiv_g, r0_g, r0_d, xlrpg_g,xlrpg_d, ylrpg_g,ylrpg_d, zlrpg_g,zlrpg_d, materiau):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        generate_pdf(file_path, info, lentille, psc_g, psc_d, tonus_g, tonus_d,
                     prisme_g, prisme_d, lipide_g, lipide_d, lacrymale_g, lacrymale_d,
                     particularite, dhiv_g,dhiv_d, r0_g, r0_d, xlrpg_g,xlrpg_d, ylrpg_g,ylrpg_d, zlrpg_g,zlrpg_d, materiau)



def add_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.beige)
    canvas.rect(0, 0, A4[0], A4[1], fill=1)
    canvas.restoreState()

def generate_pdf(filename, info, lentille, psc_g, psc_d, tonus_g, tonus_d,
                 prisme_g, prisme_d, lipide_g, lipide_d, lacrymale_g, lacrymale_d,
                 particularite, dhiv_g, dhiv_d, r0_g, r0_d, xlrpg_g, xlrpg_d, ylrpg_g, ylrpg_d, zlrpg_g, zlrpg_d,
                 materiau):
    # Initialisation du document


    pdf = BaseDocTemplate(filename, pagesize=A4)
    frame = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width, pdf.height, id='normal')
    template = PageTemplate(id='background', frames=frame, onPage=add_background)
    pdf.addPageTemplates([template])

    elements = []

    # Styles
    styles = getSampleStyleSheet()
    style_normal = styles['Normal']
    style_title = styles['Title']
    style_centered = styles['Normal']
    style_centered.alignment = TA_CENTER

    # Ajout du titre
    title = Paragraph("Rapport de Consultation", style_title)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Information du patient
    patient_info = Paragraph(f"Nom: {info["Nom"]}   Prénom: {info["Prénom"]}    Âge: {info["Âge"]}", style_normal)
    elements.append(patient_info)
    elements.append(Spacer(1, 12))

    # Type de lentille
    lentille_info = Paragraph(f"Lentille: {lentille}", style_normal)
    elements.append(lentille_info)
    elements.append(Spacer(1, 12))

    # Récapitulatif des données
    recapitulatif_data = [
        ["Récapitulatif des données"],
        ['Oeil Gauche', 'Oeil Droit'],
        [f"Psc: {psc_g}", f"Psc: {psc_d}"],
        [f"Tonus: {tonus_g}", f"Tonus: {tonus_d}"],
        [f"Hauteur du prisme: {prisme_g}", f"Hauteur du prisme: {prisme_d}"],
        [f"Grade lipide: {lipide_g}", f"Grade lipide: {lipide_d}"],
        [f"Charge lacrymale: {lacrymale_g}", f"Charge lacrymale: {lacrymale_d}"],
    ]

    recapitulatif_table = Table(recapitulatif_data, colWidths=[7 * cm, 7 * cm])
    recapitulatif_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcyan),
        ('GRID', (0, 0), (-1, -1), 1, colors.transparent),
    ]))

    elements.append(recapitulatif_table)
    elements.append(Spacer(1, 12))

    # Particularités
    particularite_info = Paragraph(f"Particularité: {particularite}", style_normal)
    elements.append(particularite_info)
    elements.append(Spacer(1, 12))

    # Paramètres de commande
    parametre_data = [
        ["Paramètres de commande"],
        ['Oeil Gauche', 'Oeil Droit'],
        [f"Diamètre Gauche = {dhiv_g}", f"Diamètre Droit = {dhiv_d}"],
        [f"Rayon Gauche = {r0_g}", f"Rayon Droit = {r0_d}"],
        [f"Puissance Gauche = {xlrpg_g} ({ylrpg_g}) {zlrpg_g}°", f"Puissance Droit = {xlrpg_d} ({ylrpg_d}) {zlrpg_d}°"],
    ]

    parametre_table = Table(parametre_data, colWidths=[7 * cm, 7 * cm])
    parametre_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightcoral),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.mistyrose),
        ('GRID', (0, 0), (-1, -1), 1, colors.transparent),
    ]))

    elements.append(parametre_table)
    elements.append(Spacer(1, 12))

    # Matériau
    materiau_info = Paragraph(f"Matériau = {materiau}", style_normal)
    elements.append(materiau_info)

    # Génération du PDF
    pdf.build(elements)
    # Finalisation du PDF
    #pdf.showPage()
    #pdf.save()
