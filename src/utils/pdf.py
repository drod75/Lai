from pypdf import PdfReader


def extract_text(file) -> str:
    """The function `extract_text` reads text from a PDF file using the PdfReader library and returns the
    concatenated text from all pages.

    Parameters
    ----------
    file
        The `extract_text` function takes a file path as input and reads the text content from a PDF file
    located at that path. It uses the `PdfReader` class to read the PDF file and extract text from each
    page. The function then concatenates all the extracted text from each page into a

    Returns
    -------
        The function `extract_text` returns a string containing the extracted text from all pages of the
    PDF file specified as the input parameter.

    """
    reader = PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    return full_text
