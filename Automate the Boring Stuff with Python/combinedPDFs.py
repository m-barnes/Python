import PyPDF2, os

#create a list to store the list of PDF files in the directory.
pdfFiles = []


#Search the directory and make a list of all the PDF files in it. 
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

#sort the list alphabetically
pdfFiles.sort(key=str.lower)

#open the PDFFileWriter
pdfWriter = PyPDF2.PdfFileWriter()

#open the file in read-binary mode and create a file object
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	#loop through every page in every PDF and copy it to the file object.
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
	
#create a new PDF file and write everything to it. When finished, close the file. 	
pdfOutput = open('combinedPDFs.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
