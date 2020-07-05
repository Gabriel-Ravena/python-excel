from openpyxl import load_workbook

archivo = "./archivoPrueba.xlsx"

wb = load_workbook(archivo)

sheet = wb.active

a2 = sheet['A2'].value
b2 = sheet['B2'].value
c2 = sheet['C2'].value

celdas = [a2, b2, c2]

for cell in celdas:
    print(cell)


