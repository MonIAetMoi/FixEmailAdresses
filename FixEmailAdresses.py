import os

os.chdir("/Users/mariengiraud/Desktop/CV")

from xlrd import open_workbook

old_doc = raw_input(Quel fichier voulez-vous nettoyer ?)
old = open_workbook(old_doc)
for sheet in old.sheets():
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
    item.append(new_adresses)

print(values)
print("new_adresses = ")
print(new_adresses)

new_doc = old_doc[:-4]
with open_workbook(new_doc + " updated") as new :
    for adresses in new_adresses:
        new.writelines(adresses)
