from docx2pdf import convert
import shutil

def convert_docx_to_pdf(docx_file, pdf_file):
    convert(docx_file, pdf_file)

def word_to_pdf_converter(docx_file, pdf_file):
    convert_docx_to_pdf(docx_file, "Bewerbung.pdf")
    shutil.move("Bewerbung.pdf", pdf_file)