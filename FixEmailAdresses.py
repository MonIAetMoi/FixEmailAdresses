import os

os.chdir("/Users/mariengiraud/Desktop/CV")

from xlrd import open_workbook


wb = open_workbook('CV ASVOLT 2.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

values = []

for row in range(1, number_of_rows):
    values.append(sheet.cell(row,0).value)

for item in values:
    new_adresses = []
    if "<" in item or ">" in item :
        item = (item[item.index("<")+1:item.index(">")-1])
    else :
        item = item

print(values)
print("new_adresses = ")
print(new_adresses)


with open_workbook('CV ASVOLT 2 updated','w') as new :
    for adresses in new_adresses:
        new.writelines(adresses)
