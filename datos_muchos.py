from openpyxl import load_workbook

archivo = "./archivoPrueba.xlsx"

wb = load_workbook(archivo)

sheet = wb.active

datos = [('ID', 'Nombre', 'Edad', 'Puesto', 'Sueldo'),
            (0, 'Gabriel', 34, 'QA Automation', '50000'),
            (1, 'esteban', 44, 'Tester  jr', '26000'),
            (2, 'ricardo', 42, 'recursos humanos', '35000'),
            (3, 'juan', 43, 'Scrum Master', '45000'),
            (4, 'Ariel', 32, 'Tester', '60000')]

for row in datos:
    sheet.append(row)

wb.save(archivo)

