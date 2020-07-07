import xlrd
import openpyxl

excel_file = "G:/Chethan/Python notes/Selenium programs/excel/Book12.xlsx"

wb = xlrd.open_workbook(excel_file)
sheet = wb.sheet_by_index(0)


for i in range(sheet.nrows):
    if '100D-U' == sheet.cell_value(i,0):
        b=set()

        # x=sheet.row_values(0)
        # d=sheet.row_values(i)
        a = sheet.row_values(i,3,4)
        for j in (sheet.row_values(i,3,4)):
            b.add(j)
        print(b)



