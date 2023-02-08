import PyPDF2
file = open("File handeling/Core Python.pdf",'rb')
pdfReader = PyPDF2.PdfFileReader(file)

print(pdfReader.numPages)
page = pdfReader.getPage(0)
print(page.extractText())
file.close()
