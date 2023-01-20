from requests import get
from bs4 import BeautifulSoup

BASE_ROUTE: str = "https://alphardaudio.ru"


def get_product_links(category: str) -> list[str]:
    page = get(f"{BASE_ROUTE}/products/{category}")
    print(page.status_code)
    link_elements = BeautifulSoup(page.text, "lxml").findAll("a", "product_list__button_more")
    links = [BASE_ROUTE + el.get("href") for el in link_elements]
    print(len(links))
    return links


def get_product_info(product_link: str):
    product_page = get(product_link)
    print(product_page.status_code)

    product_info = dict()  # TODO: можно данные о товаре вынести в структуру
    table = BeautifulSoup(product_page.text, "lxml").find("table", "table")
    rows = table.findAll("tr")
    for row in rows:
        cells = row.findAll("td")
        product_info[cells[0].getText()] = cells[1].getText().strip()
    return product_info

