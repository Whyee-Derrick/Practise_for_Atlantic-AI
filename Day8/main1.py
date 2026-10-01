from pypdf import PdfReader
text = ""

reader = PdfReader("maths.pdf")

for page in reader.pages:
    text+=page.extract_text()
   
print (len(text))