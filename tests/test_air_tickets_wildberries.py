import time

from pages.wildberries import AirTickets


def test_search_start_day(web_browser):
    """ Make sure the tickets search works fine. """

    page = AirTickets(web_browser)

    # Entering country of departure
    page.from_where.click()
    page.write_from_where = 'Москва'
    time.sleep(0.5)
    page.write_from_where.push_enter()

    # Entering country of arrival
    page.to_where.click()
    page.write_to_where = 'Новосибирск'
    time.sleep(0.5)
    page.write_to_where.push_enter()

    # Click search
    page.start_day.click()
    page.select_start_day.click()

    page.search_button.click()
    page.results_list.wait_to_be_clickable()

    # Check search is work
    list_from_where = page.results_from_where.get_text()
    for i in list_from_where:
        assert i == 'Москва'
    list_to_where = page.results_to_where.get_text()
    for i in list_to_where:
        assert i == 'Новосибирск'


def test_air_sort_by_price(web_browser):
    """ Make sure that sort by price works fine. """

    page = AirTickets(web_browser)

    # Entering country of departure
    page.from_where.click()
    page.write_from_where = 'Москва'
    time.sleep(0.5)
    page.write_from_where.push_enter()

    # Entering country of arrival
    page.to_where.click()
    page.write_to_where = 'Лос-Анджелес'
    time.sleep(0.5)
    page.write_to_where.push_enter()

    page.start_day.click()
    page.select_start_day.click()

    page.search_button.click()
    page.results_list.wait_to_be_clickable()

    list_tickets_price = page.tickets_price.get_text()
    list_tickets_price = [(p.replace('₽', '')) for p in list_tickets_price]
    list_tickets_price = [int(p.replace(' ', '')) for p in list_tickets_price]

    # Make sure tickets are sorted by price correctly:
    assert list_tickets_price == sorted(list_tickets_price), "Sort by price doesn't work!"


def test_air_sort_by_transfer(web_browser):
    """ Make sure that sort by transfer works fine. """

    page = AirTickets(web_browser)

    # Entering country of departure
    page.from_where.click()
    page.write_from_where = 'Москва'
    time.sleep(0.5)
    page.write_from_where.push_enter()

    # Entering country of arrival
    page.to_where.click()
    page.write_to_where = 'Лос-Анджелес'
    time.sleep(0.5)
    page.write_to_where.push_enter()

    page.start_day.click()
    page.select_start_day.click()

    page.search_button.click()
    page.results_list.wait_to_be_clickable()

    if page.transfer_0.is_visible():
        page.transfer_0.click()
    if page.transfer_2.is_visible():
        page.transfer_2.click()
    transfers = page.check_transfer.get_text()

    # Check sort is work
    for i in transfers:
        assert i == '1 пересадка'


def test_air_sort_by_baggage(web_browser):
    """ Make sure that sort by baggage works fine. """

    page = AirTickets(web_browser)

    # Entering country of departure
    page.from_where.click()
    page.write_from_where = 'Москва'
    time.sleep(0.5)
    page.write_from_where.push_enter()

    # Entering country of arrival
    page.to_where.click()
    page.write_to_where = 'Лос-Анджелес'
    time.sleep(0.5)
    page.write_to_where.push_enter()

    page.start_day.click()
    page.select_start_day.click()

    page.search_button.click()
    page.results_list.wait_to_be_clickable()

    page.baggage.click()
    baggage_list = page.check_baggage.get_text()

    # Check sort is work
    for i in baggage_list:
        assert i == 'Без багажа'
