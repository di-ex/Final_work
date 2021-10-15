import pytest
from pages.wildberries import MainPage


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

    # Try to enter "носки" with English keyboard:
    page.search = 'yjcrb'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'носки' in title.lower(), msg


def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.

        Note: this test case will fail because there is a bug in
              sorting products by price.
    """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()
    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices_with.get_text()
    all_prices = [(p.replace('₽', '')) for p in all_prices]
    all_prices = [int(p.replace(' ', '')) for p in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"


def test_shopping_cart(web_browser):
    """ Make sure add to cart works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Adding item to cart
    page.select_item.move_to_element()
    page.add_to_cart.click()

    page.go_to_cart.click()
    items = page.amount_items.get_text()
    items = items[0].split(' ')
    assert int(items[1]) == page.items_list.count()





