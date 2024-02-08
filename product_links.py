import random
import time

import requests
from bs4 import BeautifulSoup
import re
import typing
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}
#
# response = requests.get('https://www.mouser.com/c/semiconductors/discrete-semiconductors/diodes-rectifiers/', headers=headers)
#
# with open('diodes-rectifiers.html', 'w') as f:
#     f.write(response.text)


with open('diodes-rectifiers.html', 'r') as f:
    html_code = f.read()


# def get_product_links(link):
#     '''
#     фунгкция вернет все ссылки на товары
#     :param link:
#     :return:
#     '''
#
#
#     soup = BeautifulSoup(html_code,'lxml')
#
#     all_products = soup.find_all('a', attrs={'id': re.compile('lnkMfrPartNumber')})
#     print(len(all_products))
#
#
#     # ссылка на следующую страницу
#     next_page = soup.find('a', attrs={'id': 'lnkPager_lnkNext'})
#     print(next_page['href'])
#
#
# prod_link = get_product_links(html_code)


def get_product_links(start_url: str) -> typing.List[str]:
    '''
    возвращает все ссылки на каждый товар, перебирая страницу с пагинацией
    :param start_url: начальная страница
    :return: список ссылок на товары
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    links = []  # список для сбора ссылок
    next_page = start_url  # Начало с первой страницы каталога
    session = requests.Session()  # Используем сессию для поддержки cookies и заголовков

    while next_page:
        response = session.get(next_page, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        products = soup.find_all('a', attrs={'id': re.compile('lnkMfrPartNumber')})
        links.extend(product['href'] for product in products)

        # поиск следующей страницы
        next_page_tag = soup.find('a', attrs={'id': 'lnkPager_lnkNext'})
        next_page = next_page_tag['href'] if next_page_tag else None  # Обновляем ссылку на след. страницу или завершаем
        time.sleep(random.randint(3, 7))
    return links


filename = 'links_semiconductors.json'
with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

# print(data['semiconductors']['sub_category'].keys())
def links_all_semicond():

    for k, v in data['semiconductors']['sub_category'].items():
        # print(k, v)
        print(f"***************{k}*************")
        # print(type(v))
        # print(v[0])
        for dict_inside in v:
            for key_sub, link_sub in dict_inside.items():
                print(key_sub)
                print(link_sub)

def generate_new_json(input_json):
    new_json = {"semiconductors": {"sub_category": {}}}
    for category, subcategories in input_json["semiconductors"]["sub_category"].items():
        new_json["semiconductors"]["sub_category"][category] = []
        for subcategory_dict in subcategories:
            for subcategory_name, subcategory_link in subcategory_dict.items():
                print(f"Processing {subcategory_name}...")
                product_links = get_product_links(subcategory_link)
                # product_links = 'checking that'
                new_subcategory_dict = {subcategory_name: product_links}
                new_json["semiconductors"]["sub_category"][category].append(new_subcategory_dict)
    return new_json



new_json = generate_new_json(data)

# Сохранение нового JSON файла
output_filename = 'product_links_semiconductors.json'
with open(output_filename, 'w', encoding='utf-8') as outfile:
    json.dump(new_json, outfile, ensure_ascii=False, indent=4)