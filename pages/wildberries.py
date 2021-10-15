import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.wildberries.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='searchInput')

    # Search button
    search_run_button = WebElement(id='applySearchBtn')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//span[@class="goods-name"]')

    # Button to sort products by price
    sort_products_by_price = WebElement(xpath='//a[contains(text(), "цене")]')

    # Prices of the products in search results
    # price without discount
    # products_prices_without = ManyWebElements(xpath='//span[@class="lower-price"]')
    # price with discount
    products_prices_with = ManyWebElements(xpath='//div[@class="product-card__brand"]//span[@class="price-commission__current-price"]')

    # Add item to cart
    select_item = WebElement(xpath='//div[@class="product-card__img-wrap"]')
    s_i = ManyWebElements(xpath='//div[@class="product-card__img-wrap"]')


    add_to_cart = WebElement(xpath='//a[@class="btn-main-sm j-add-to-basket"]')
    go_to_cart = WebElement(xpath='//a[@class="navbar-pc__link" and @href="/lk/basket"]')
    amount_items = ManyWebElements(xpath='//div[@class="b-top__count line"]/span[1]')
    items_list = ManyWebElements(xpath='//div[@class="accordion__list-item list-item j-b-basket-item"]')

    delete_item = WebElement(xpath='//button[@class="btn__del j-basket-item-del"]')
    empty_cart = WebElement(xpath='//div[@class="basket-page__basket-empty basket-empty"]')
    item_in_cart = WebElement(xpath='//div[@class="accordion__list-item list-item j-b-basket-item"]')

    plus = WebElement(xpath='//button[@class="count__plus plus"]')
    minus = WebElement(xpath='//button[@class="count__minus minus"]')
    summa = WebElement(xpath='//p[@class="b-top__total line"]//span[@data-link]')
    price = WebElement(xpath='//div[@class="list-item__price-new"]')


class Categories(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.wildberries.ru/'

        super().__init__(web_driver, url)

    categories_list = WebElement(xpath='//button[@class="nav-element__burger j-menu-burger-btn"]')
    name_title = WebElement(xpath='//*[@class="catalog-title"]')

    women_categories = WebElement(xpath='//li[@data-menu-id="306"]')
    women_title = 'Женщинам'

    men_categories = WebElement(xpath='//li[@data-menu-id="566"]')
    men_title = 'Мужчинам'

    children_categories = WebElement(xpath='//li[@data-menu-id="115"]')
    children_title = 'Детям'

    shoes_categories = WebElement(xpath='//li[@data-menu-id="629"]')
    shoes_title = 'Обувь'

    accessories_categories = WebElement(xpath='//li[@data-menu-id="1"]')
    accessories_title = 'Аксессуары'

    electronics_categories = WebElement(xpath='//li[@data-menu-id="4830"]')
    electronics_title = 'Электроника'

    video_categories = WebElement(xpath='//li[@data-menu-id="111"]')
    video_name_title = WebElement(xpath='//div[@class="head-title"]')
    video_title = 'Видеообзоры'

    air_tickets_categories = WebElement(xpath='//li[@data-menu-id="61037"]')
    air_tickets_title = 'авиабилеты онлайн'

    premium_categories = WebElement(xpath='//li[@data-menu-id="128297"]')
    premium_title = 'Wildberries - модный интернет магазин'

    household_appliances_categories = WebElement(xpath='//li[@data-menu-id="16107"]')
    household_appliances_title = 'Бытовая техника'

    books_categories = WebElement(xpath='//li[@data-menu-id="519"]')
    books_title = 'Книги'

    sport_categories = WebElement(xpath='//li[@data-menu-id="784"]')
    sport_title = 'спортивные товары'

    school_categories = WebElement(xpath='//li[@data-menu-id="250"]')
    school_title = 'Школа'

    beauty_categories = WebElement(xpath='//li[@data-menu-id="543"]')
    beauty_title = 'Красота'

    toys_categories = WebElement(xpath='//li[@data-menu-id="481"]')
    toys_title = 'Игрушки'

    food_categories = WebElement(xpath='//li[@data-menu-id="10296"]')
    food_title = 'Продукты'

    garden_cottage_categories = WebElement(xpath='//li[@data-menu-id="4863"]')
    garden_cottage_title = 'Сад и дача'

    pet_products_categories = WebElement(xpath='//li[@data-menu-id="6119"]')
    pet_products_title = 'Зоотовары'

    stationery_categories = WebElement(xpath='//li[@data-menu-id="5486"]')
    stationery_title = 'Канцтовары'

    health_categories = WebElement(xpath='//li[@data-menu-id="10326"]')
    health_title = 'Здоровье'

    repair_categories = WebElement(xpath='//li[@data-menu-id="17006"]')
    repair_title = 'Для ремонта'

    house_categories = WebElement(xpath='//li[@data-menu-id="258"]')
    house_title = 'Дом'

    automotive_supplies_categories = WebElement(xpath='//li[@data-menu-id="6994"]')
    automotive_supplies_title = 'Автотовары'

    jewelry_categories = WebElement(xpath='//li[@data-menu-id="1023"]')
    jewelry_title = 'Ювелирные изделия'

    brands_categories = WebElement(xpath='//li[@data-menu-id="4853"]')
    brands_name_title = WebElement(xpath='//h2[@class="brands-list-page__header"]')
    brands_title = 'Страницы брендов'

    discounts_categories = WebElement(xpath='//li[@data-menu-id="2192"]')
    discounts_name_title = WebElement(xpath='//*[@class="promo-page__title"]')
    discounts_title = 'Акции дня'
    """ОКНО 18+"""
    products_adults_categories = WebElement(xpath='//li[@data-menu-id="62057"]')
    products_adults_title = 'Товары для взрослых'

    digital_categories = WebElement(xpath='//li[@data-menu-id="12"]')
    digital_title = 'Digital Wildberries'


class Other(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.wildberries.ru/'

        super().__init__(web_driver, url)

    delete_item = WebElement(xpath='//button[@class="btn__del j-basket-item-del"]')
    empty_cart = WebElement(xpath='//div[@class="basket-page__basket-empty basket-empty"]')

