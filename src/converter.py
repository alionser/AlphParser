# import pandas as pd
#
#
# def convert_dict_to_exel(data: dict):
#     frame = pd.DataFrame(data)
#     frame.to_excel("text.xlsx")

from openpyxl import Workbook


def normalize_category_by_params(data: list[dict[str, str]]):
    types = {}
    for product in data:
        if tuple(product.keys()) not in types:
            types[tuple(product.keys())] = list()
            types[tuple(product.keys())].append(product.values())
        else:
            types[tuple(product.keys())].append(product.values())
    return types


def convert_data_to_exel(data: list[dict[str, str]]):
    data = normalize_category_by_params(data)
    workbook = Workbook()
    worksheet = workbook.active
    for product_type in data:
        worksheet.append(list(product_type))
        for product in data[product_type]:
            worksheet.append(list(product))
    # worksheet.append(list(data[0].keys()))
    # for product in data[1:]:
    #     worksheet.append(list(product.values()))
    # worksheet.append(enumerate(list(data.values())))
    workbook.save("товары.xlsx")
