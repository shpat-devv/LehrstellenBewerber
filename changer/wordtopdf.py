from docx import Document
import pdfkit

docxfilepath = "Tests/hello.docx"

def convert_docx_to_pdf(docx_file, pdf_file):
    # Read the docx file
    doc = Document(docx_file)
    
    # Extract text from the docx file
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    
    # Write text to a temporary HTML file
    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(text)
    
    # Convert HTML to PDF
    pdfkit.from_file("temp.html", pdf_file)
    
    # Remove the temporary HTML file
    import os
    os.remove("temp.html")

# Example usage:
convert_docx_to_pdf("hello.docx", "example.pdf")
