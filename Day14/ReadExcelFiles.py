import openpyxl

#File->Workbook->Sheets->Rows->Cells
#Read data from excel
path="C:\\SeleniumPractice\\Workbook1.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook["Sheet1"]

rows = sheet.max_row #count no of rows in excel sheet
cols = sheet.max_column #count no of columns in excel sheet

for r in range(1,rows+1):
    for c in range(1,cols+1):
        print(sheet.cell(r,c).value,end='   ')
    print()
