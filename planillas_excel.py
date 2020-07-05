from openpyxl import load_workbook

DOCUMENTO = 'equipos-futbol.xlsx'
SHEET = "Hoja1"

workbook = load_workbook(DOCUMENTO, read_only=True)
sheet = workbook[SHEET]

for columna in sheet.iter_columns():
    print(columna[1].value)





