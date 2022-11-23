import os
import PyPDF2

# encrypted_pdfFiles = []
# #for root, dirs, files in os.walk('../automate_online-materials2e'):
# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.pdf'):
#             fileObj = open(file, 'rb')
#             pdfFileReader = PyPDF2.PdfFileReader(fileObj)
#             if pdfFileReader.isEncrypted:
#                 encrypted_pdfFiles.append(os.path.join(root,file))
#
# for pdfFile in encrypted_pdfFiles:
#     password = input('Enter the password for ' + pdfFile.split('/')[-1] + ':\n')
#     fileObj = open(pdfFile, 'rb')
#     pdfFileReader = PyPDF2.PdfFileReader(fileObj)
#     pdfFileReader.decrypt(password)
#     try:
#         pdfFileReader.getPage(0)
#     except:
#         if pdfFile != encrypted_pdfFiles[-1]:
#             print('Password is incorrect. Continuing to the next file...')
#         else:
#             print('Password is incorrect.')
#         continue
#     newFileObj = open(pdfFile.split('/')[-1].split('.pdf')[0] + '_decrypted.pdf', 'wb')
#     newpdfFileWriter = PyPDF2.PdfFileWriter()
#     for pageNum in range(pdfFileReader.numPages):
#         newpdfFileWriter.addPage(pdfFileReader.getPage(pageNum))
#     newpdfFileWriter.write(newFileObj)
#     print(pdfFile.split('/')[-1].split('.pdf')[0] + '_decrypted.pdf created')
#
#
#

encrypted_pdfFiles = []
#for root, dirs, files in os.walk('../automate_online-materials2e'):
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.pdf'):
            fileObj = open(os.path.join(root,file), 'rb')
            pdfFileReader = PyPDF2.PdfFileReader(fileObj)
            if not pdfFileReader.isEncrypted:
                continue
            password = input('Enter the password for ' + file + ':\n')
            pdfFileReader.decrypt(password)
            try:
                pdfFileReader.getPage(0)
            except:
                print('Password is incorrect. Continuing to the next file...')
                continue
            newFileObj = open(file.split('.pdf')[0] + '_decrypted.pdf', 'wb')
            newpdfFileWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfFileReader.numPages):
                newpdfFileWriter.addPage(pdfFileReader.getPage(pageNum))
            newpdfFileWriter.write(newFileObj)
            print(file.split('.pdf')[0] + '_decrypted.pdf created')
print('Completed. Ending program...')