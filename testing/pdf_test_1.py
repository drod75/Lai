from pypdf import PdfReader

file_path = "c:/Users/drodr/Documents/lai_tests/tests1/test1.pdf"

reader = PdfReader(file_path)
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"
print(full_text)
