import csv

import requests

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
    # 'Cookie': 'search=%7B%22usage%22%3A%7B%22dailyCount%22%3A3%2C%22lastRequest%22%3A%222024-02-16T18%3A08%3A10.125Z%22%7D%2C%22version%22%3A1%7D; ai_user=nPmofiOQHynSNXmv2dKD5v|2024-02-15T01:03:08.185Z; _pxhd=9862e1044edd564f12a996d2fd9fd226fa1f4acfe583a4aee3e676d2feb5e26d:fb35fd4a-cb9d-11ee-be19-791effb23b8c; utag_main=v_id:018daa49fcec000256b1785e8cb40504e006301100bd0$_sn:4$_se:2$_ss:0$_st:1708108726017$ses_id:1708106893948%3Bexp-session$_pn:1%3Bexp-session; dk_tagxi=undefined.0.1708031280; _pxvid=fb35fd4a-cb9d-11ee-be19-791effb23b8c; ping-accept-language=en-ES; dk_item_data=item_list_id=60&item_list_name=PS-FAM; _ga_1TEG8CV4XM=GS1.1.1708106894.4.0.1708106894.60.0.0; _ga=GA1.2.546556993.1707958994; EG-U-ID=A969aa8c2f-70cf-4a59-97e0-bba89f761788; _gid=GA1.2.1194005933.1707959162; _gcl_au=1.1.97676242.1707959162; _fbp=fb.1.1707959162374.211955395; _evga_3cfa=0c9e8b0c6616c025.; ai_session=iX4oA5sncdNq30+HEmLf1b|1708106890127|1708106893960; TS01173021=013feb5604ec5c2a3494fb67f66c572a65fca1355524f01cdead1426ed24dd77c8436a21e582bbd77bc744cdbd6cad97809bfdf3d2; TS112fb876027=080716a071ab200061f99e464706c172696b4e93cc0b260ec66914d2b8cfa317a83e0023d7a7175a08449b9c3d11300065c2e069e3b344003aa6de4e9b943b923fe79a7843dca9ba3b90997dc2dfd2d089b87a25508e4739fa27db2d8a211eda; dkc_tracker=3639919109761; _dd_s=rum=2&id=34b53e2c-8cd9-4a28-b96c-1abe24086a1c&created=1708106902271&expire=1708107826186; EG-S-ID=C891ebaf1a-b7fe-4039-b31e-53af6331f268; pxcts=59ab10a5-ccf6-11ee-aae5-88173e501329; _pxde=2679b19d7207392c9d891460cb0bdebf65168eecba5afae2cc7b0af8ec742217:eyJ0aW1lc3RhbXAiOjE3MDgxMDY5MDIxMTcsImZfa2IiOjAsImlwY19pZCI6W10sImluY19pZCI6WyIyNjA4YWQ1ZjhlMmY3ZjJkMWRlZjI2NjVkN2Q1OGM2YiJdfQ==; search_prefs=%7B%22theme%22%3A%22light%22%7D; _cs_mk=0.10566726348165478_1708106926020; _px2=eyJ1IjoiNTk4NjAzMDAtY2NmNi0xMWVlLWFjYmMtMDdjOWZlOGZmYWY4IiwidiI6ImZiMzVmZDRhLWNiOWQtMTFlZS1iZTE5LTc5MWVmZmIyM2I4YyIsInQiOjE3MDgxMDcxOTU1NjAsImgiOiJkZTFmMjVhYjY0Y2Y0MmFjZDgxY2E3ZmRjZDVlMDE1ZDBiNWEzMDlmOGMxYjMxMTgwZWI2ODRjMTcxNzRiODllIn0=; _uetsid=630ff420cb9e11eeacdb5f8159546f10; _uetvid=630ffaa0cb9e11ee924dc53d77b8cd6a; TS019f5e6c=01c72bed21c254c0841c4c4a122bac5d6eee02b7ef3f7ddf3f20c1c5d800cc62c74558fdf6f366170dceddf019889493ec4f510e48; TSbafe380b027=08a1509f8aab2000e1209efcdccb9ddb75125705d869f6f7e8da5abf559f9e4a6ede49912fe114ff08641526ed113000b72951d83078f427c16d7399c39a16d82d1f8f06954bcab5154086414715958d26e2cafd9ed0f67ce9ac609754b3798f; TS016ca11c=01c72bed219f10a1200916585d2357e86ae5759d8af45a1a97f7ab221f9fd323a4677e072a4f2f7e15aa92cdfec63df3198a09e306; TSc580adf4027=08a1509f8aab2000194bb1aa857b61529f77a5b161cea1515c830f8a29d04fff2534e63eb38cfb62082dba08c3113000e6ebfd90e2e41a2ec16d7399c39a16d8a671d6d7ae1fe4e4b6ca2e88561d2200af0f074791b5ac5b75a877e326d5c9d1; _gat_Production=1; QSI_HistorySession=; utm_data_x=html_element1%3Ddownload-table-popup-trigger-button%2Chtml_element2%3Ddownload-table-popup-trigger%2Chtml_element3%3DMuiGrid-root%20MuiGrid-item%20tss-16xinpl-downloadButton%20css-1wxaqej%2Chtml_element4%3DMuiGrid-root%20MuiGrid-container%20css-1d3bbye%2Cundefined%3Dtss-nt9krt-tableControl%2CExtRun%3D450.1%7C409.2%7C429.2%7C428.1%7C428.5%7C450.1%2Cref_page_type%3DPS%2Cref_page_sub_type%3DFAM%2Cref_page_id%3D60%2Cccookie%3D2024-02-15T01%3A06%3A01.989Z%2Cref_page_state%3DSort%20Order%20Test%20-%20Default%2Cref_pers_state%3D%7B%22%5C%22PLS%5C%22%22%3A%22Scrolling%22%7D%2Cref_part_search_term%3D%2Cref_part_search_term_ext%3D%2CExtRun%3D450.1%7C409.2%7C429.2%7C428.1%7C428.5%7C450.1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    's': 'N4IgrCBcoA5QjAFgEwBoQzpeAGHBffIA',
}

# response = requests.get(
#     'https://www.digikey.es/products/api/v5/filter-page/products-download/60',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )
#
#
# if response.status_code == 200:
#     # Записываем содержимое ответа в файл
#     with open('file.csv', 'wb') as file:
#         file.write(response.content)
#     print("CSV файл успешно сохранён.")
# else:
#     print(f"Ошибка получения данных: Код статуса {response.status_code}")
#
# url = 'https://www.digikey.es/products/api/v5/filter-page/products-download/60?s=N4IgrCBcoA5QjAFgEwBoQzpeAGHBffIA'