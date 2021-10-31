from pages.wildberries import Categories
from pages.base import WebPage


def test_women_categories(web_browser):
    """Check category Women. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.women_categories.click()
    assert page.name_title.get_text() == Categories.women_title


def test_men_categories(web_browser):
    """Check category Men. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.men_categories.click()
    assert page.name_title.get_text() == Categories.men_title


def test_children_categories(web_browser):
    """Check category Children. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.children_categories.click()
    assert page.name_title.get_text() == Categories.children_title


def test_shoes_categories(web_browser):
    """Check category Shoes. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.shoes_categories.click()
    assert page.name_title.get_text() == Categories.shoes_title


def test_accessories_categories(web_browser):
    """Check category Accessories. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.accessories_categories.click()
    assert page.name_title.get_text() == Categories.accessories_title


def test_electronics_categories(web_browser):
    """Check category Electronics. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.electronics_categories.click()
    assert page.name_title.get_text() == Categories.electronics_title


def test_video_categories(web_browser):
    """Check category Video. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.video_categories.click()
    assert page.video_name_title.get_text() == Categories.video_title


def test_air_tickets_categories(web_browser):
    """Check category Air tickets. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.air_tickets_categories.click()
    assert Categories.air_tickets_title in WebPage.get_page_title(page)


def test_premium_categories(web_browser):
    """Check category Premium. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.premium_categories.click()
    assert WebPage.get_page_title(page) == Categories.premium_title


def test_household_appliances_categories(web_browser):
    """Check category Household appliances. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.household_appliances_categories.click()
    assert page.name_title.get_text() == Categories.household_appliances_title


def test_books_categories(web_browser):
    """Check category Books. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.books_categories.click()
    assert page.name_title.get_text() == Categories.books_title


def test_sport_categories(web_browser):
    """Check category Sport. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.sport_categories.click()
    WebPage.wait_page_loaded(page)
    assert Categories.sport_title in WebPage.get_page_title(page)


def test_school_categories(web_browser):
    """Check category School. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.school_categories.click()
    assert page.name_title.get_text() == Categories.school_title


def test_beauty_categories(web_browser):
    """Check category Beauty. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.beauty_categories.click()
    assert page.name_title.get_text() == Categories.beauty_title


def test_toys_categories(web_browser):
    """Check category Toys. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.toys_categories.click()
    assert page.name_title.get_text() == Categories.toys_title


def test_food_categories(web_browser):
    """Check category Food. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.food_categories.click()
    assert page.name_title.get_text() == Categories.food_title


def test_garden_cottage_categories(web_browser):
    """Check category Garden cottage. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.garden_cottage_categories.click()
    assert page.name_title.get_text() == Categories.garden_cottage_title


def test_pet_products_categories(web_browser):
    """Check category Pet products. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.pet_products_categories.click()
    assert page.name_title.get_text() == Categories.pet_products_title


def test_stationery_categories(web_browser):
    """Check category Stationery. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.stationery_categories.click()
    assert page.name_title.get_text() == Categories.stationery_title


def test_health_categories(web_browser):
    """Check category Health. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.health_categories.click()
    assert page.name_title.get_text() == Categories.health_title


def test_repair_categories(web_browser):
    """Check category For repair. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.repair_categories.click()
    assert page.name_title.get_text() == Categories.repair_title


def test_house_categories(web_browser):
    """Check category House. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.house_categories.click()
    assert page.name_title.get_text() == Categories.house_title


def test_automotive_supplies_categories(web_browser):
    """Check category Automotive supplies. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.automotive_supplies_categories.click()
    assert page.name_title.get_text() == Categories.automotive_supplies_title


def test_jewelry_categories(web_browser):
    """Check category Jewelry. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.jewelry_categories.click()
    assert page.name_title.get_text() == Categories.jewelry_title


def test_brands_categories(web_browser):
    """Check category Brands. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.brands_categories.click()
    assert page.brands_name_title.get_text() == Categories.brands_title


def test_discounts_categories(web_browser):
    """Check category Discounts. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.discounts_categories.click()
    assert page.discounts_name_title.get_text() == Categories.discounts_title


def test_products_adults_categories(web_browser):
    """Check category Products adults. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.products_adults_categories.click()
    assert page.name_title.get_text() == Categories.products_adults_title


def test_digital_categories(web_browser):
    """Check category Digital. """

    page = Categories(web_browser)
    page.categories_list.click()
    page.digital_categories.click()
    assert Categories.digital_title in WebPage.get_page_title(page)
