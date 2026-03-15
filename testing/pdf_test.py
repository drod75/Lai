from pypdf import PdfReader

reader = PdfReader("c:/Users/drodr/Documents/lai_tests/tests1/test1.pdf")
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"
print(full_text)
