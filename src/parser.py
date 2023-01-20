from requests import get
from bs4 import BeautifulSoup as bs

BASE_ROUTE: str = "https://alphardaudio.ru"


def get_product_links(category: str) -> list[str]:
    page = get(f"{BASE_ROUTE}/products/{category}")
    print(page.status_code)
    link_elements = bs(page.text, "lxml").findAll("a", "product_list__button_more")
    links = [BASE_ROUTE + el.get("href") for el in link_elements]
    print(len(links))
    return links
