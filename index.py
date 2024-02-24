from src.CreatorService import CreatorService

import openpyxl
import uuid

try:
    creators = CreatorService.get_creators()

    excel_book = openpyxl.Workbook()
    sheet = excel_book.active

    sheet['A1'] = "Id"
    sheet['B1'] = "Lastname"
    sheet['C1'] = "Firstname"
    sheet['D1'] = "Birthdate"
    sheet['E1'] = "Genre"

    for index, row in enumerate(creators):
        sheet[f'A{index+2}'] = str(uuid.uuid4())
        sheet[f'B{index+2}'] = row[0]
        sheet[f'C{index+2}'] = row[1]
        sheet[f'D{index+2}'] = row[2]
        sheet[f'E{index+2}'] = row[3]

    excel_book.save("my_excel_file.xlsx")

except Exception as ex:
    print("Exception: {}".format(str(ex)))
