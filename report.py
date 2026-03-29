import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Step 1: Read data
df = pd.read_csv("data.csv")

# Step 2: Analyze data
average = df["Marks"].mean()
maximum = df["Marks"].max()
minimum = df["Marks"].min()

# Step 3: Create PDF
doc = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

elements = []

# Title
elements.append(Paragraph("Student Report", styles['Title']))
elements.append(Spacer(1, 12))

# Table
table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)
elements.append(Spacer(1, 12))

# Analysis
elements.append(Paragraph(f"Average Marks: {average}", styles['Normal']))
elements.append(Paragraph(f"Highest Marks: {maximum}", styles['Normal']))
elements.append(Paragraph(f"Lowest Marks: {minimum}", styles['Normal']))

# Build PDF
doc.build(elements)

print("Report Generated Successfully!")