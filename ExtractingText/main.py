import PyPDF2
pdfFileObj = open('D:/test/test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(str(pdfReader.numPages))
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())