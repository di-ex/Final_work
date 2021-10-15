import pytest
from pages.wildberries import *


# def test_delete_item_cart(web_browser):
#     """ Make sure delete to cart works fine. """
#
#     page = MainPage(web_browser)
#
#     page.search = 'iPhone 12'
#     page.search_run_button.click()
#
#     # Adding item to cart
#     page.select_item.move_to_element()
#     page.add_to_cart.click()
#     # Go to cart
#     page.go_to_cart.click()
#     # Delete item
#     page.item_in_cart.move_to_element()
#     page.delete_item.click()
#     WebPage.wait_page_loaded(page)
#     assert page.empty_cart.is_visible()

# def test_more_less_items(web_browser):
#     """ Make sure increase and decrease items from cart works fine. """
#
#     page = MainPage(web_browser)
#
#     page.search = 'iPhone 12'
#     page.search_run_button.click()
#
#     # Adding item to cart
#     page.select_item.move_to_element()
#     page.add_to_cart.click()
#     # Go to cart
#     page.go_to_cart.click()
#     # Increase the number of items
#     price = page.price.get_text()
#     price = int(price.replace('₽', ''))
#     page.plus.click()
#     page.plus.click()
#     page.minus.click()
#     WebPage.wait_page_loaded(page)
#     total = page.summa.get_text()
#     total = int(total.replace('₽', ''))
#     assert total == price * 2

def test_total_price(web_browser):
    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Adding item to cart
    a = page.s_i.find()
    for i in range(len(a)):
        if i < 3:
            a[i].move_to_element()
            page.add_to_cart.click()
            i += 1
