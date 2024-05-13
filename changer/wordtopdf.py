from docx2pdf import convert

def convert_docx_to_pdf(docx_file, pdf_file):
    convert(docx_file, pdf_file)


convert_docx_to_pdf("f.docx", "Shpat Avdiu.pdf")
