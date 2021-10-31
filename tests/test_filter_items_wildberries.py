import pytest
from pages.wildberries import FiltrationItems
from pages.base import WebPage


def test_filter_by_brand(web_browser):
    """Check filtering by Brand works fine. """

    page = FiltrationItems(web_browser)

    page.brand.click()
    WebPage.wait_page_loaded(page)

    # Make sure user found the relevant products
    for title in page.products_brand.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'acer' in title.lower(), msg


@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_filter_by_price(web_browser):
    """Check filtering by Price works fine. """
    page = FiltrationItems(web_browser)

    page.price_start.ctrl_a_del()
    page.price_start = '50000'
    page.price_end.ctrl_a_del()
    page.price_end = '52000'
    WebPage.wait_page_loaded(page)
    all_prices = page.products_prices.get_text()
    all_prices = [(p.replace('₽', '')) for p in all_prices]
    all_prices = [int(p.replace(' ', '')) for p in all_prices]
    for i in all_prices:
        assert 50000 <= i <= 52000


@pytest.mark.xfail(reason="Filter by discount doesn't work")
def test_filter_by_discount(web_browser):
    """Check filtering by Discount works fine. """
    page = FiltrationItems(web_browser)

    page.discount.click()
    WebPage.wait_page_loaded(page)
    all_discount = page.products_discount.get_text()
    all_discount = [int(p.replace('%', '')) for p in all_discount]
    for i in all_discount:
        assert i <= -30


def test_filter_by_diagonal(web_browser):
    """Check filtering by Diagonal works fine. """

    page = FiltrationItems(web_browser)

    page.screen_resolution.click()
    WebPage.wait_page_loaded(page)

    # # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert '3840x2160' in title.lower(), msg


def test_filter_by_operating_system(web_browser):
    """Check filtering by Operating system works fine. """

    page = FiltrationItems(web_browser)

    page.operating_system.click()
    WebPage.wait_page_loaded(page)
    # # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'linux' in title.lower(), msg


def test_filter_by_ram_size(web_browser):
    """Check filtering by Ram size works fine. """

    page = FiltrationItems(web_browser)

    page.ram_size.click()
    WebPage.wait_page_loaded(page)
    # # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert '8 gb' in title.lower(), msg


def test_filter_by_hdd_storage(web_browser):
    """Check filtering by HDD storage works fine. """

    page = FiltrationItems(web_browser)

    page.hdd_storage.click()
    WebPage.wait_page_loaded(page)
    # # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert '500 гб' in title.lower(), msg
