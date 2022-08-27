import openpyxl

wb = openpyxl.Workbook()

sheet  = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 42
sheet['A2'] = 'Hello'

wb.save('example1.xlsx')

#adding new worksheet
sheet2 = wb.create_sheet()