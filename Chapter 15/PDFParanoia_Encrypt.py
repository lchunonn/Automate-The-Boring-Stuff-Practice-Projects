import os
import PyPDF2

# pdfFiles = []
# for root, dirs, files in os.walk('../automate_online-materials2e'):
#     for file in files:
#         if file.endswith('.pdf'):
#             pdfFiles.append(os.path.join(root,file))
#
# for pdfFile in pdfFiles:
#     pdfFileObj = open(pdfFile, 'rb')
#     filename = pdfFile.split('/')[-1].split('.pdf')[0]
#     pdfFileReader = PyPDF2.PdfFileReader(pdfFileObj)
#     if pdfFileReader.isEncrypted:
#         continue
#     newpdf = PyPDF2.PdfWriter()
#     for i in range(pdfFileReader.numPages):
#         newpdf.addPage(pdfFileReader.getPage(i))
#     newpdf.encrypt('passwordispassword')
#     new_pdfFileObj = open(filename + '_encrypted.pdf', 'wb')
#     newpdf.write(new_pdfFileObj)
#     print(filename + '_encrypted.pdf created.')
#
#


for root, dirs, files in os.walk('../automate_online-materials2e'):
    for file in files:
        if file.endswith('.pdf'):
            pdfFileObj = open(os.path.join(root, file), 'rb')
            filename = os.path.join(root, file).split('/')[-1].split('.pdf')[0]
            pdfFileReader = PyPDF2.PdfFileReader(pdfFileObj)
            if pdfFileReader.isEncrypted:
                continue
            newpdf = PyPDF2.PdfWriter()
            for i in range(pdfFileReader.numPages):
                newpdf.addPage(pdfFileReader.getPage(i))
            newpdf.encrypt('passwordispassword')
            new_pdfFileObj = open(filename + '_encrypted.pdf', 'wb')
            newpdf.write(new_pdfFileObj)
            print(filename + '_encrypted.pdf created.')
print('Completed. Ending program...')