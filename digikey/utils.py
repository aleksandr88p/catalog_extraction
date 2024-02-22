import asyncio
import json
from fake_useragent import UserAgent
import lzstring
import csv
import json
import requests
import aiohttp
import ssl
from aiohttp_socks import ProxyConnector

import logging

# Настройка логгера для ошибок запросов
error_logger = logging.getLogger("request_errors_in_utils")
error_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("request_errors_in_utils.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
error_logger.addHandler(file_handler)


def make_compress_pagination(page: int):
    '''

    :param page: number of page
    :return: compress pagination page
    '''
    lz = lzstring.LZString()

    data = {"5": {"p": page, "pp": 500}}
    """N4IgrCBcAEoA5WgRgCwCYA00RwTJADAQL7FA страница  142
    N4IgrCBcAEoA5WgRgAxvQGmiOCapQF9Cg страница  1000000
    N4IgrCBcAEoA5WgRgDTRHBMkAYcF98g страница  1
    """
    json_string = json.dumps(data)
    lz = lzstring.LZString()
    compressed_string = lz.compressToEncodedURIComponent(json_string)
    return compressed_string

# p = make_compress_pagination(1)
# print(p)
async def fetch_with_pagination(url_to_download: str, page:int, old_ulr: str, proxy_url: str = None):

    pagination = make_compress_pagination(page)
    ua = UserAgent()
    headers = {
        'User-Agent': ua.chrome,
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': f'{old_ulr}?s={pagination}',
        'authorization': 'Bearer',
        'lang': 'en',
        'request-context': 'appId=cid-v1:40371992-8794-4ad9-9011-4552f68fdb07',
        'request-id': '|3705c704a62a48cf83785ee4fe4897dd.d515992e3c5e485a',
        'site': 'es',
        'traceparent': '00-3705c704a62a48cf83785ee4fe4897dd-d515992e3c5e485a-01',
        'x-currency': 'EUR',
        'x-request-id': 'e167b9cd-22ed-43a2-a19b-8e5ff45e9f73',
        'Alt-Used': 'www.digikey.es',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    # Создание SSL контекста
    sslcontext = ssl.create_default_context()
    # Использование ProxyConnector, если указан proxy_url
    connector = ProxyConnector.from_url(proxy_url) if proxy_url else None
    params = {}

    max_attempt = 5
    attempt = 0
    while attempt < max_attempt:
        try:
            async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
                async with session.get(f'{url_to_download}?s={pagination}', ssl=sslcontext, params=params) as response:
                    if response.status == 200:
                        text = await response.text()
                        print(f'********************\n{old_ulr}?s={pagination}\n{url_to_download}?s={pagination}**********')
                        # with open(f'file{pagination}.csv', 'w') as f:
                        #     f.write(text)
                        return text, 200
                    elif response.status == 204:
                        return None, 204
                    return None, response.status
        except Exception as e:
            error_logger.error(f"Ошибка при запросе к {url_to_download}: {e}")
            attempt += 1
            await asyncio.sleep(20)


def format_identifier(identifier):
    """
    Форматирует строку для использования в качестве названия таблицы или колонки в SQL.
    Удаляет специальные символы, заменяет пробелы на подчеркивания и приводит к нижнему регистру.
    """
    # Удаляем специальные символы и заменяем пробелы на подчеркивания
    formatted = ''.join(char if char.isalnum() or char == ' ' else '' for char in identifier).replace(' ', '_').lower()
    return formatted


# async def fetch_with_pagination(url_to_download: str, page: int, old_ulr: str, proxy_url: str = None):
#     async with aiohttp.ClientSession() as session:
#
#         pagination = make_compress_pagination(page)
#         ua = UserAgent()
#         cookies = {
#         }
#
#         headers = {
#             'User-Agent': ua.chrome,
#             'Accept': '*/*',
#             'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#             # 'Accept-Encoding': 'gzip, deflate, br',
#             'Referer': f'{old_ulr}?s={pagination}',
#             'authorization': 'Bearer',
#             'lang': 'en',
#             'request-context': 'appId=cid-v1:40371992-8794-4ad9-9011-4552f68fdb07',
#             'request-id': '|3705c704a62a48cf83785ee4fe4897dd.d515992e3c5e485a',
#             'site': 'es',
#             'traceparent': '00-3705c704a62a48cf83785ee4fe4897dd-d515992e3c5e485a-01',
#             'x-currency': 'EUR',
#             'x-request-id': 'e167b9cd-22ed-43a2-a19b-8e5ff45e9f73',
#             'Alt-Used': 'www.digikey.es',
#             'Connection': 'keep-alive',
#             'Sec-Fetch-Dest': 'empty',
#             'Sec-Fetch-Mode': 'cors',
#             'Sec-Fetch-Site': 'same-origin',
#         }
#
#         ssl_context = ssl.create_default_context()
#
#         connector = ProxyConnector.from_url(proxy_url) if proxy_url else None
#         params = {
#         }
#
#         async with session.get(f'{url_to_download}?s={pagination}',
#                                headers=headers, params=params) as response:
#             if response.status == 200:
#                 text = await response.text()
#                 print(f'********************\n{old_ulr}?s={pagination}\n{url_to_download}?s={pagination}**********')
#                 # with open(f'file{pagination}.csv', 'w') as f:
#                 #     f.write(text)
#                 return text, 200
#             elif response.status == 204:
#                 return None, 204
#             return None, response.status
#
#




def work_exel(pagination):
    ua = UserAgent()

    cookies = {
    }

    headers = {
        'User-Agent': ua.chrome,
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.digikey.es/en/products/filter/ceramic-capacitors/60?s=N4IgrCBcAEoA5WgRgCwCYA00RwTJADAQL7FA',
        'authorization': 'Bearer',
        'lang': 'en',
        'request-context': 'appId=cid-v1:40371992-8794-4ad9-9011-4552f68fdb07',
        'request-id': '|3705c704a62a48cf83785ee4fe4897dd.d515992e3c5e485a',
        'site': 'es',
        'traceparent': '00-3705c704a62a48cf83785ee4fe4897dd-d515992e3c5e485a-01',
        'x-currency': 'EUR',
        'x-request-id': 'e167b9cd-22ed-43a2-a19b-8e5ff45e9f73',
        'Alt-Used': 'www.digikey.es',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
    }
    response = requests.get(
        f'https://www.digikey.es/products/api/v5/filter-page/products-download/157?s={pagination}',
        params=params,
        cookies=cookies,
        headers=headers,
    )


    if response.status_code == 200:
        # ЗДЕСЬ НАДО КАК ТО СДЕЛАТЬ ЛОГИКУ ДЛЯ БД
        pass
    elif response.status_code == 204:
        # ТУТ НУЖНО КАК ТО СДЕЛАТЬ ЧТО МЫ ЗАКАНЧИВАЕМ С ЭТОЙ КАТЕГОРИЕЙ
        pass
    else:
        # Я ПРАВИЛЬНО ПОНЯЛ ЧТО ЗДЕСЬ НАМ НАДО ЗАНОВО ЗАПРОС КАК ТО ОТПРАВИТЬ?
        pass
        print(f"Ошибка получения данных: Код статуса {response.status_code}")


