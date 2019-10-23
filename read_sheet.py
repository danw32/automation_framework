# ** Daniel Whalley Dec 2017 ** #
from xlrd import open_workbook

book = open_workbook('test_sheet_YN.xls')
#book = open_workbook('ladbrokes_sheet.xls')
sheet = book.sheet_by_index(0)

first_row = []  # The row where we store the name of the column
for col in range(sheet.ncols):
    first_row.append(sheet.cell_value(0, col))
# transform the workbook to a list of dictionaries
data = []
for row in range(1, sheet.nrows):
    data_dict = {}
    for col in range(sheet.ncols):
        data_dict[first_row[col]] = sheet.cell_value(row, col)
    data.append(data_dict)
#print data