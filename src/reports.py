from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import plotly.express as px

def create_pdf_report(data, report_path):
    doc = SimpleDocTemplate(report_path, pagesize=letter)
    styles = getSampleStyleSheet()

    title_style = styles['Title']
    heading_style = styles['Heading2']
    normal_style = styles['Normal']

    title_style.alignment = 1
    heading_style.spaceBefore = 12
    heading_style.spaceAfter = 12
    normal_style.spaceBefore = 6
    normal_style.spaceAfter = 6

    elements = []
    elements.append(Paragraph("Raport Analizy Rynku Nieruchomości", title_style))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Podsumowanie Statystyczne", heading_style))
    elements.append(Spacer(1, 12))

    # Convert summary statistics to a table and adjust it to fit on one page
    summary = data.describe().reset_index()
    summary_data = [summary.columns.to_list()] + summary.values.tolist()
    summary_table = Table(summary_data, hAlign='LEFT')
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 12))

    # Scatter matrix visualization
    fig = px.scatter_matrix(data)
    fig_path = "scatter_matrix.png"
    fig.write_image(fig_path)
    elements.append(Paragraph("Macierz Rozproszenia", heading_style))
    elements.append(Spacer(1, 12))
    elements.append(Image(fig_path, width=500, height=400))
    elements.append(Spacer(1, 12))

    # Scatter mapbox visualization
    fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", color="cena", size="powierzchnia",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                            mapbox_style="carto-positron")
    fig_path = "scatter_mapbox.png"
    fig.write_image(fig_path)
    elements.append(Paragraph("Mapa Rozproszenia", heading_style))
    elements.append(Spacer(1, 12))
    elements.append(Image(fig_path, width=500, height=400))
    elements.append(Spacer(1, 12))

    # Build PDF
    doc.build(elements)
