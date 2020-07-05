from openpyxl import load_workbook

archivo = "./archivoPrueba.xlsx"

wb = load_workbook(archivo)

sheet = wb.active

sheet ['A1'] = "Gabriel"
sheet ['B1'] = "Ravena"
sheet ['C1'] = 34

wb.save(archivo)