from docx2pdf import convert
import shutil
import os

this_path = os.path.dirname(os.path.realpath(__file__))

def word_to_pdf_converter(application_path, this_path):
    convert(application_path, f"{this_path}/Bewerbung/tosend")
