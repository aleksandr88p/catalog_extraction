"""
ищу закондированную пагинацию с помощью плейврайт
нужно сделать самый первый раз playwright install
"""
import time

from playwright.sync_api import Playwright, sync_playwright

def block_resources(route, patterns):
    should_block = any(pattern in route.request.url for pattern in patterns)
    if should_block:
        route.abort()
    else:
        route.continue_()
patterns_to_block = ['image', '.css']  # Список паттернов URL для блокировки



# Запуск Playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        proxy={'server': 'http://37.48.118.4:13010'},
        headless=False
    )
    # Заголовки
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        # "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    page = browser.new_page()
    page.route('**/*', lambda route: block_resources(route, patterns_to_block))
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    page.set_extra_http_headers(headers=headers2)


    page.goto("https://www.digikey.es/en/products/filter/ceramic-capacitors/60?s=N4IgrCBcoA5QjAGhDOl4AYMF9tA")

    time.sleep(20)
    next_button_selector = '[data-testid="btn-next-page"]'  # Селектор для кнопки "Next Page"
    print(next_button_selector)
    current_url = page.url  # Получение текущего URL страницы
    print(f"Текущий URL: {current_url}")  # Вывод URL для анализа
    for _ in range(10):  # Пример для 10 страниц
        if page.is_visible(next_button_selector, timeout=5000):  # Проверка видимости кнопки "Следующая страница"
            page.wait_for_selector(next_button_selector)  # Ожидание, пока кнопка не станет доступна

            page.click(next_button_selector)  # Клик по кнопке "Следующая страница"
            page.wait_for_navigation()  # Ожидание завершения перехода на новую страницу
            # Ваш код для обработки страницы здесь

        else:
            print("Кнопка для перехода на следующую страницу не найдена.")
            break


    browser.close()