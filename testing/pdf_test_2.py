import pypdfium2 as pdfium  # type: ignore


def extract_all_text(pdf_path):
    pdf = pdfium.PdfDocument(pdf_path)
    n_pages = len(pdf)
    full_text = ""

    for page_index in range(n_pages):
        page = pdf[page_index]
        textpage = page.get_textpage()
        full_text += textpage.get_text_range() + "\n"
        textpage.close()
        page.close()

    # Close the document
    pdf.close()

    return full_text


# Usage example
file_path = "c:/Users/drodr/Documents/lai_tests/tests1/test1.pdf"
content = extract_all_text(file_path)
print(content)
