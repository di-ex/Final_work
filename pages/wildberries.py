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
    products_prices = ManyWebElements(
        xpath='//div[@class="product-card__brand"]//span[@class="price-commission__current-price"]')

    # Button to sort products by discount
    sort_products_by_discount = WebElement(xpath='//span[contains(text(), "скидке")]')

    discount_list = ManyWebElements(xpath='//span[@class="product-card__sale"]')

    # Add item to cart
    select_item = WebElement(xpath='//div[@class="product-card__img-wrap"]')
    select_items = ManyWebElements(xpath='//div[@class="product-card__img-wrap"]')

    add_to_cart = WebElement(xpath='//a[@class="btn-main-sm j-add-to-basket"]')
    go_to_cart = WebElement(xpath='//a[@class="navbar-pc__link" and @href="/lk/basket"]')
    amount_items = ManyWebElements(xpath='//div[@class="b-top__count line"]/span[1]')
    items_list = ManyWebElements(
        xpath='//div[@class="accordion__list-item list-item j-b-basket-item"]')

    delete_item = WebElement(xpath='//button[@class="btn__del j-basket-item-del"]')
    empty_cart = WebElement(xpath='//div[@class="basket-page__basket-empty basket-empty"]')
    item_in_cart = WebElement(xpath='//div[@class="accordion__list-item list-item j-b-basket-item"]')

    plus = WebElement(xpath='//button[@class="count__plus plus"]')
    minus = WebElement(xpath='//button[@class="count__minus minus"]')
    summa = WebElement(xpath='//p[@class="b-top__total line"]//span[@data-link]')
    price = WebElement(xpath='//div[@class="list-item__price-new"]')
    prices = ManyWebElements(xpath='//div[@class="list-item__price-new"]')

    quick_view = WebElement(xpath='//button[@class="product-card__fast-view j-open-product-popup"]')
    content = WebElement(xpath='//div[@class="i-popup-same-part-kt shown"]')

    article = WebElement(xpath='//div[@class="same-part-kt__common-info"]/p/span[3]')


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


class FiltrationItems(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki'

        super().__init__(web_driver, url)

    brand = WebElement(xpath='//label[contains(text(), "Acer")]')
    products_brand = ManyWebElements(xpath='//strong[@class="brand-name"]')

    price_start = WebElement(xpath='//div[@class="start-n"]//input')
    price_end = WebElement(xpath='//div[@class="end-n"]//input')
    products_prices = ManyWebElements(
        xpath='//div[@class="product-card__brand"]//span[@class="price-commission__current-price"]')

    discount = WebElement(xpath='//span[contains(text(), "от 30% и выше")]')
    products_discount = ManyWebElements(xpath='//span[@class="product-card__sale"]')

    products_titles = ManyWebElements(xpath='//span[@class="goods-name"]')
    screen_resolution = WebElement(xpath='//label[contains(text(), "3840x2160")]')

    operating_system = WebElement(xpath='//label[contains(text(), "Linux")]')

    ram_size = WebElement(xpath='//label[contains(text(), "8 GB")]')

    hdd_storage = WebElement(xpath='//label[contains(text(), "500 Гб")]')


class AirTickets(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://travel.wildberries.ru/'

        super().__init__(web_driver, url)

    from_where = WebElement(id='departureButton')
    write_from_where = WebElement(xpath='//input[@class="_1SrpT _yZJ7"]')
    to_where = WebElement(id='arrivalButton')
    write_to_where = WebElement(xpath='//input[@class="_1SrpT _20K-h"]')
    start_day = WebElement(id='startDay')
    end_day = WebElement(id='endDay')
    search_button = WebElement(xpath='//button[@class="_1MYfn"]')
    select_start_day = WebElement(xpath='//td[@aria-label="понедельник, 22 ноября 2021 г."]')
    select_end_day = WebElement(xpath='//td[@aria-label="воскресенье, 28 ноября 2021 г."]')

    results_list = WebElement(id='resultsTicketsList')
    results_from_where = ManyWebElements(xpath='//div[@class="_3BDi5 _1flX6"]//span[@class="_2p9Cb HPAbM"]')
    results_to_where = ManyWebElements(xpath='//div[@class="fJG5l _1flX6"]//span[@class="_2p9Cb HPAbM"]')

    tickets_price = ManyWebElements(xpath='//span[@class="_3qqJv"]')

    transfer_0 = WebElement(xpath='//span[@class="_3Mxmu _3n6tN"][contains(text(), "Прямой")]')
    transfer_1 = WebElement(xpath='//span[@class="_3Mxmu _3n6tN"][contains(text(), "1 Пересадка")]')
    transfer_2 = WebElement(xpath='//span[@class="_3Mxmu _3n6tN"][contains(text(), "2 Пересадки")]')
    check_transfer = ManyWebElements(xpath='//span[@class="_2XVES"]')
    baggage = WebElement(xpath='//span[@class="_3Mxmu _3n6tN"][contains(text(), "Багаж")]')
    check_baggage = ManyWebElements(xpath='//span[@class="_1vYx3"]')
