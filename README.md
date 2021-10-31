Финальное тестовое задание
-----

Тестирование интернет-магазина Wildberries (https://www.wildberries.ru/)


Файлы
-----

[conftest.py](conftest.py) содержит необходимый код, чтобы отлавливать неудачные тестовые случаи и делать снимок экрана
страницы.

[pages/base.py](pages/base.py) содержит реализацию шаблона PageObject для Python.

[pages/elements.py](pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[tests/test_smoke_wildberries_market.py](tests/test_smoke_wildberries_market.py) содержит smoke тесты

[tests/test_filter_items_wildberries.py](tests/test_filter_items_wildberries.py) содержит тесты фильтрации поиска

[tests/test_categories_wildberries.py](tests/test_categories_wildberries.py) содержит тесты категорий

[tests/test_air_tickets_wildberries.py](tests/test_air_tickets_wildberries.py) содержит тесты фильтрации поиска авиабилетов


Как запустить тесты
----------------

1) Установить requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Скачать Selenium WebDriver https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)

3) Запуск тестов:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chromedriver.exe tests/*
    ```

