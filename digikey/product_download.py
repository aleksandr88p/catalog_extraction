import csv
import json

import requests



def download_exel():
    cookies = {
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
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
        's': 'N4IgrCBcoA5QjAFgEwBoQzpeAGHBffIA',
    }

    response = requests.get(
        'https://www.digikey.es/products/api/v5/filter-page/products-download/157?s=N4IgrCBcAEoA5WgRgDTRHBMkAYcF98g',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    """
    Ошибка получения данных: Код статуса 204  N4IgrCBcAEoA5WgRgAxvQGmiOCapQF9Cg
    CSV файл успешно сохранён. N4IgrCBcAEoA5WgRgDTRHBMkAYcF98g
    """

    if response.status_code == 200:
        # Записываем содержимое ответа в файл
        with open('file222.csv', 'wb') as file:
            file.write(response.content)
        print("CSV файл успешно сохранён.")
    else:
        print(f"Ошибка получения данных: Код статуса {response.status_code}")

url = 'https://www.digikey.es/products/api/v5/filter-page/products-download/60?s=N4IgrCBcoA5QjAFgEwBoQzpeAGHBffIA'

url2 = 'https://www.digikey.es/products/api/v5/filter-page/products-download/157?s=N4IgrCBcoA5QzAGhDOkCMAGTBfHQ'

# download_exel()


"""
403 Forbidden: Доступ к ресурсу запрещен.
429 Too Many Requests: Слишком много запросов.
503 Service Unavailable: Сервис недоступен.
"""

with open('file222.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Создание словаря для хранения информации о товарах
    products_info = {}

    # Итерация по строкам в CSV файле
    for i, row in enumerate(reader):
        product_key = f"good{i + 1}"
        # for k, v in row.items():
        #     if k == 'Image':
        #         print(v)


        products_info[product_key] = row
        # break


with open('_json_with_info.json', 'w') as file:
    json.dump(products_info, file, indent=4)

"""
у меня есть csv большой в нем на каждой строке в столбцах разная информация о том или ином товаре. 
я хочу пройти по нему циклом с помощью питона.
Мне нужно в итоге записать в БД информацию о каждом товаре отдельно в нужный столбец в таблеце БД.
Но пока что я хочу посмотреть как это будет выглядеть. и сделать словарик. Типа {товар1:{название столбца: значение для это товара},
и так для каждого столбца}

https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/2503/GOLDENMAX 300 C0G, NP0.jpg 
"""