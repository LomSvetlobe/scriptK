import os
from pdf2image import convert_from_path
import pytesseract

def pdf_to_text(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Perform OCR on each image and extract text
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)

    return text

pdf_file = r'C:\Users\luka_\Desktop\Python\scriptK\thermo-tek_bd_050_wbs.pdf'
extracted_text = pdf_to_text(pdf_file)
print(extracted_text)