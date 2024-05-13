from docx import Document

def wordchanger(docx_file, old_text, new_text):
    doc = Document(docx_file)
    for paragraph in doc.paragraphs:
        if old_text in paragraph.text:
            paragraph.text = paragraph.text.replace(old_text, new_text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if old_text in cell.text:
                    cell.text = cell.text.replace(old_text, new_text)
    doc.save("updated_document.docx")

# Example usage:
replace_text_in_docx("original_document.docx", "old_text", "new_text")
