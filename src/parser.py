from requests import get
from bs4 import BeautifulSoup
from requests_html import HTMLSession

BASE_ROUTE: str = "https://alphardaudio.ru"

# TODO: сделать получение ВСЕХ товаров, если нужно


def get_product_links_by_category(category: str) -> list[str]:
    page = get(f"{BASE_ROUTE}/products/{category}")
    print(page.status_code)
    link_elements = BeautifulSoup(page.text, "lxml").findAll("a", "product_list__button_more")
    links = [BASE_ROUTE + el.get("href") for el in link_elements]
    print(len(links))
    return links


def get_product_info(product_link: str):
    session = HTMLSession()
    page = session.get(product_link)
    page.html.render()

    product_info = dict()  # TODO: можно данные о товаре вынести в структуру
    table = BeautifulSoup(page.html.html, "lxml").find("table", "table")
    rows = table.findAll("tr")
    for row in rows:
        cells = row.findAll("td")
        product_info[cells[0].getText()] = cells[1].getText().strip()

    price = BeautifulSoup(page.html.html, "lxml").find("span", "price").getText().strip()
    product_info["Цена"] = price
    print(f"Processed: {product_info['Модель']}")
    return product_info


def get_all_products_info_by_category(category: str):
    products = []
    links = get_product_links_by_category(category)
    for link in links:
        products.append(get_product_info(link))
    return products
