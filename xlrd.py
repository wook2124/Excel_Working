from xlrd import open_workbook

wb = open_workbook('과일.xlsx')
for sheet in wb.sheets():
    print(sheet.name)
    for i in range(sheet.nrows):
        row = sheet.row(i)
        for c in row:
            print(c.value)