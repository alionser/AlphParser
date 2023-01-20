# import pandas as pd
#
#
# def convert_dict_to_exel(data: dict):
#     frame = pd.DataFrame(data)
#     frame.to_excel("text.xlsx")

from openpyxl import Workbook


def convert_data_to_exel(data: list[dict[str, str]]):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.append(list(data[0].keys()))
    for product in data[1:]:
        worksheet.append(list(product.values()))
    # worksheet.append(enumerate(list(data.values())))
    workbook.save("товары.xlsx")
