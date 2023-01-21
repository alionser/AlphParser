# import pandas as pd
#
#
# def convert_dict_to_exel(data: dict):
#     frame = pd.DataFrame(data)
#     frame.to_excel("text.xlsx")

from openpyxl import Workbook


def normalize_category_by_params(data: list[dict[str, str]]):
    headers = set()
    for product in data:
        headers = headers.union(set(product.keys()))

    normalized_category = [list(headers), ]
    for product in data:
        product_list = []
        for col in list(headers):
            if col in product:
                product_list.append(product[col])
            else:
                product_list.append("")
        normalized_category.append(product_list)
    print(normalized_category)

    return normalized_category



def convert_data_to_exel(data: list[dict[str, str]]):
    data = normalize_category_by_params(data)
    workbook = Workbook()
    worksheet = workbook.active
    for row in data:
        worksheet.append(row)
    # worksheet.append(list(data[0].keys()))
    # for product in data[1:]:
    #     worksheet.append(list(product.values()))
    # worksheet.append(enumerate(list(data.values())))
    workbook.save("товары.xlsx")
