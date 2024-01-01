import os
from PyPDF2 import PdfWriter, PdfReader

doc_side_1 = "./front.pdf"
doc_side_2 = "./back.pdf"

inputSideOnePdf = PdfReader(open(doc_side_1, "rb"))
inputSideTwoPdf = PdfReader(open(doc_side_2, "rb"))

if (len(inputSideOnePdf.pages) != len(inputSideTwoPdf.pages)):
    print("Error: Number of pages in both documents are not equal.")
    exit()

output = PdfWriter()
for i in range(len(inputSideOnePdf.pages)):
    output.add_page(inputSideOnePdf.pages[i])
    output.add_page(inputSideTwoPdf.pages[len(inputSideTwoPdf.pages) - i - 1])

with open("./dist/mergedDoc.pdf", "wb") as outputStream:
    output.write(outputStream)