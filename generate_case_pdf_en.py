from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import os

md_path = r"C:\Users\harle\.copilot\chats\7b4d726a-6a03-4171-be52-5548da76b8af\CASO_ESTUDO_1_PRECIFICACAO_EN.md"
pdf_path = r"C:\Users\harle\Desktop\CASO_ESTUDO_1_PRICING_EN_Harley.pdf"

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

styles = getSampleStyleSheet()
body = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=12)
doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
story = []
for line in text.splitlines():
    if line.startswith('#'):
        lvl = line.count('#')
        txt = line.lstrip('#').strip()
        style = ParagraphStyle('H'+str(lvl), parent=styles['Normal'], fontSize=max(16-2*lvl,10), leading=14, spaceAfter=6, fontName='Helvetica-Bold')
        story.append(Paragraph(txt, style))
    elif line.strip() == '---':
        story.append(Spacer(1,12))
    elif line.strip() == '':
        story.append(Spacer(1,6))
    else:
        if line.strip().startswith('```'):
            continue
        text_line = line.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        if text_line.strip().startswith('- '):
            story.append(Paragraph('• ' + text_line.strip()[2:], body))
        else:
            story.append(Paragraph(text_line, body))

# Ensure Desktop directory exists
desktop_dir = os.path.dirname(pdf_path)
if not os.path.exists(desktop_dir):
    os.makedirs(desktop_dir)

try:
    doc.build(story)
    print('PDF_CREATED:' + pdf_path)
except Exception as e:
    print('PDF_ERROR:' + str(e))
