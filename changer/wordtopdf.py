from docx2pdf import convert
import shutil

def convert_docx_to_pdf(docx_file, pdf_file):
    convert(docx_file, pdf_file)

def word_to_pdf_converter():
    convert_docx_to_pdf("Bewerbung/Shpat Avdiu.docx", "Bewerbung.pdf")
    shutil.move("Bewerbung.pdf", "Bewerbung/tosend/Bewerbung.pdf")
