from selenium.webdriver import ActionChains
from pages.wildberries import MainPage
from pages.base import WebPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'Samsung s20'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'samsung' or 's20' in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Try to enter "чайник" with English keyboard:
    page.search = 'xfqybr'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'чайник' in title.lower(), msg


def test_check_sort_by_ascending_price(web_browser):
    """ Make sure that sort by ascending price works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Sort by ascending price
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()
    all_prices = [(p.replace('₽', '')) for p in all_prices]
    all_prices = [int(p.replace(' ', '')) for p in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"


def test_check_sort_by_descending_price(web_browser):
    """ Make sure that sort by descending price works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()
    # Sort by descending price
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()
    all_prices = [(p.replace('₽', '')) for p in all_prices]
    all_prices = [int(p.replace(' ', '')) for p in all_prices]
    sorted_prices = sorted(all_prices)
    # Make sure products are sorted by price correctly:
    assert all_prices == sorted_prices[::-1], "Sort by price doesn't work!"


def test_check_sort_by_discount(web_browser):
    """ Make sure that sort by discount works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    page.sort_products_by_discount.click()
    page.wait_page_loaded()

    # Get discounts on products in Search results
    all_discount = page.discount_list.get_text()
    all_discount = [int(p.replace('%', '')) for p in all_discount]

    # Make sure products are sorted by discount correctly:
    assert all_discount == sorted(all_discount), "Sort by price doesn't work!"


def test_add_item_cart(web_browser):
    """ Make sure add to cart works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Adding item to cart
    page.select_item.move_to_element()
    page.add_to_cart.click()

    # Go to cart
    page.go_to_cart.click()

    # Checking items in the cart
    items = page.amount_items.get_text()
    items = items[0].split(' ')
    assert int(items[1]) == page.items_list.count()


def test_delete_item_cart(web_browser):
    """ Make sure delete from the cart works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Adding item to cart
    page.select_item.move_to_element()
    page.add_to_cart.click()
    # Go to cart
    page.go_to_cart.click()
    # Delete item
    page.item_in_cart.move_to_element()
    page.delete_item.click()
    WebPage.wait_page_loaded(page)
    assert page.empty_cart.is_visible()


def test_more_less_items(web_browser):
    """ Make sure increase and decrease items from cart works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Adding item to cart
    page.select_item.move_to_element()
    page.add_to_cart.click()
    # Go to cart
    page.go_to_cart.click()
    # Increase the number of items
    price = page.price.get_text()
    price = price.replace('₽', '')
    price = int(price.replace(' ', ''))
    page.plus.click()
    page.plus.click()
    page.minus.click()
    WebPage.wait_page_loaded(page)
    total = page.summa.get_text()
    total = total.replace('₽', '')
    total = int(total.replace(' ', ''))
    assert total == price * 2


def test_total_price(web_browser):
    """ Make sure the total price is calculated correctly. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Adding 3 items to cart
    elements = page.select_items.find()

    for i, element in enumerate(elements):
        if i < 3:
            action = ActionChains(page._web_driver)
            action.move_to_element(element).perform()
            page.add_to_cart.click()
            i += 1

    # Go to cart
    page.go_to_cart.click()

    # Check the total price
    price_list = page.prices.get_text()
    new_price_list = []
    for i in range(len(price_list)):
        one_price = price_list[i].replace('₽', '')
        one_price = int(one_price.replace(' ', ''))
        new_price_list.append(one_price)
    total = page.summa.get_text()
    total = total.replace('₽', '')
    total = int(total.replace(' ', ''))
    # print(sum(new_price_list))
    # print(total)
    assert sum(new_price_list) == total


def test_quick_view(web_browser):
    """ Make sure that Quick view works. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Open quick view
    page.select_item.move_to_element()
    page.quick_view.click()
    WebPage.wait_page_loaded(page)

    # Check that quick view is open
    assert page.content.is_visible()


def test_search_by_article(web_browser):
    """ Make sure main search by article works fine. """

    page = MainPage(web_browser)

    page.search = '21052470'
    page.search_run_button.click()

    art = page.article.get_text()
    assert int(art) == 21052470
