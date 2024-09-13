from docx2pdf import convert
import shutil

def convert_docx_to_pdf(docx_file, pdf_file):
    convert(docx_file, pdf_file)

def word_to_pdf_converter():
    convert_docx_to_pdf("_internal/Bewerbung/Bewerbung.docx", "_internal/Bewerbung.pdf")
    shutil.move("_internal/Bewerbung.pdf", "_internal/Bewerbung/tosend/Bewerbung.pdf")
