from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text


# pdf = PdfReader(r"C:\Users\luka_\Desktop\Python\scriptK\testni.pdf")
# strani = pdf.pages[0]
text = extract_text(r"C:\Users\luka_\Desktop\Python\scriptK\thermo-tek_bd_050_wbs.pdf")
print(repr(text))
#print(strani.extract_text())