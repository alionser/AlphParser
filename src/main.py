from pprint import pprint
from converter import *
from parser import *

# test_product = get_product_info("https://alphardaudio.ru/products/subwoofers/machete-mf-12r-d2-d4")
# pprint(test_product)
# convert_dict_to_exel(test_product)
# print(get_product_links("subwoofers"))
data = get_all_products_info_by_category("subwoofers")
# pprint(data)
convert_data_to_exel(data)
print("\n\n\n")
# pprint(get_all_products_info_by_category("speakers"))



