#! /usr/bin/env python3
import sys, openpyxl

if len(sys.argv) != 2:
    print('Usage: ./multiplicationTableMaker.py <n> where <n> is an integer')
    sys.exit()


if not sys.argv[1].isdigit():
    print('Argument must be an integer')
    sys.exit()

n = int(sys.argv[1])

wb = openpyxl.Workbook()
sheet = wb.active

boldFont = openpyxl.styles.Font(bold=True)

for i in range(1, n+1):
    sheet.cell(column=i+1, row=1).value = i
    sheet.cell(column=i+1, row=1).font = boldFont
    sheet.cell(column=1, row=i+1).value = i
    sheet.cell(column=1, row=i+1).font = boldFont

for i in range(1,n+1):
     for j in range(1,n+1):
         sheet.cell(column=j+1, row=i+1).value = '=PRODUCT(' + openpyxl.utils.get_column_letter(j+1) + '1, A' + str(i+1) + ')'

wb.save('table.xlsx')

