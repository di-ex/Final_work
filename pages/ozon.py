import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ozon.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(xpath='//input[@placeholder="Искать на Ozon"]')

    # Search button
    search_run_button = WebElement(xpath='//button[@class="f9k"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//span[@class="a7y a8a2 a8a6 a8b2 f-tsBodyL bj5"]')

    # Button to sort products by price
    sort_button = WebElement(xpath='//input[@class="_2jPB"]')
    sort_products_by_price = WebElement(xpath='//*[contains(text(), "Сначала дешёвые")]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='')

    select_item = WebElement()
    select_model = WebElement(xpath='')
    add_to_cart = WebElement()
    delete_elements = ManyWebElements(xpath='//div[@data-widget="skuAdvSearchShelf"]')


