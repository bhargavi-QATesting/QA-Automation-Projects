import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.reader.excel import load_workbook


#File->Workbook->Sheets->Rows->Cells
#Write same data into excel
'''path="C:\\SeleniumPractice\\Workbook2.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active # or sheet = workbook["Data"] if we have only one sheet (get active sheet from excel)

rows = sheet.max_row
cols = sheet.max_column
#to write same data in all the cells use for loop
for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value="Bhargavi"'''


#Write different data into excel
path="C:\\SeleniumPractice\\Workbook3.xlsx"
workbook = load_workbook(path) #if we use from openpyxl.reader.excel import load_workbook
sheet = workbook.active # or sheet = workbook["Data"] if we have only one sheet (get active sheet from excel)

sheet.cell(1,1).value="Bhargavi"
sheet.cell(1,2).value="Rama"
sheet.cell(1,3).value="Sita"
sheet.cell(2,1).value="sitara"
sheet.cell(2,2).value="Manasa"
sheet.cell(2,3).value="Rahul"
sheet.cell(3,1).value="Karthik"
sheet.cell(3,2).value="Alisia"
sheet.cell(3,3).value="Nagaleela"

workbook.save(path) #save the file after entering the data

