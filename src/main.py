from pprint import pprint
from converter import *
from parser import *


category = input("Введите название категории с сайта: ")
data = get_all_products_info_by_category(category)
convert_data_to_exel(data)
