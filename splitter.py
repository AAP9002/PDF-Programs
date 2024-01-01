import os
from PyPDF2 import PdfWriter, PdfReader

arr = os.listdir("./")
print(arr)

print("split every n pages:")
n = int(input())
print("length of desired document:")
length = int(input())
print("ignore page (separate with ','):")
ignore = input()
if ignore == "":
    ignore = []
else:
    ignore = ignore.split(",")
    ignore = [int(i)-1 for i in ignore]
print("enter file name:")
filename = input()
print("start count at:")
initialCount = int(input())

for file in arr:
    if file.endswith(".pdf"):
        print(file)
        inputpdf = PdfReader(open(file, "rb"))
        output = PdfWriter()
        count = initialCount
        for i in range(len(inputpdf.pages)):
            if(i%n in ignore):
                continue
            if(i%n == length-1):
                output.add_page(inputpdf.pages[i])
                with open("./dist/"+str(count)+" -- "+filename+".pdf", "wb") as outputStream:
                    output.write(outputStream)
                output = PdfWriter()
                count+=1
            else:
                if(i%n < length-1):
                    output.add_page(inputpdf.pages[i])