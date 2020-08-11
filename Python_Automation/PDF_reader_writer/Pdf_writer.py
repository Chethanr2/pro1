import PyPDF2, os

os.chdir('G:\Chethan\Python notes\Selenium programs\Python_Automation')

PDF1File = open('VPSDTraining_ Parameters.pdf', 'rb')
PDF2File = open('VPSDTraining_CartographyV2.pdf', 'rb')

Reader1 = PyPDF2.PdfFileReader(PDF1File)
Reader2 = PyPDF2.PdfFileReader(PDF2File)

writer = PyPDF2.PdfFileWriter()

for PageNum in range(Reader1.numPages):
    page = Reader1.getPage(PageNum)
    writer.addPage(page)

for PageNum in range(Reader2.numPages):
    page = Reader2.getPage(PageNum)
    writer.addPage(page)

outputFile = open('Combination.pdf','wb')
writer.write(outputFile)

outputFile.close()
PDF2File.close()
PDF1File.close()