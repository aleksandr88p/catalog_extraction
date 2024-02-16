import requests
import json

cookies = {}

headers = {
    'authority': 'www.digikey.es',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer',
    'cache-control': 'no-cache',
    'dnt': '1',
    'lang': 'en',
    'pragma': 'no-cache',
    'referer': 'https://www.digikey.es/en/products/filter/chassis-mount-resistors/54',
    'request-context': 'appId=cid-v1:40371992-8794-4ad9-9011-4552f68fdb07',
    'request-id': '|8782348e871142bea3975fea52961bb5.491aef15380d483d',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'site': 'es',
    'traceparent': '00-8782348e871142bea3975fea52961bb5-491aef15380d483d-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-currency': 'EUR',
    'x-request-id': '633639bb-cf97-418f-a6b2-7c98eb7dd14f',
}

params = {
    's': 'N4IgrCBcAEoA5WgRgCwCYA00RwTJADAQL7FA',
}


def make_resp():
    response = requests.get('https://www.digikey.es/products/api/v5/filter-page/60', params=params, cookies=cookies,
                            headers=headers)
    with open('response_with_json.json', 'w') as f:
        f.write(response.text)


with open('response_with_json.json', 'r') as file:
    draft_file = json.load(file)

# with open('response_with_jsonINDENT.json', 'w') as file:
#     json.dump(draft_file, file, indent=4)
"""
data 
dict_keys(['products', 'longTail', 'categoryInfo', 'productCount', 'commonFilters', 
'filters', 'productHeaders', 'category', 'breadcrumb', 'pageMetaCollection'])


"""
# print(draft_file['data'].keys())
with open('new_json.json', 'w') as f:
    json.dump(draft_file['data']['products'], f, indent=4)

for index, item in enumerate(draft_file['data']['products']):
    if index == 0:
        # print(item[2])
        productID_1 = item[0]['value'].get('productId', None)
        productID_2 = item[1]['value'].get('productId', None)
        productNumber = item[1]['value'].get('productNumber', None)
        datasheetUrl = item[1]['value'].get('datasheetUrl', None)
        description = item[1]['value'].get('description', None)
        detailUrl = item[1]['value'].get('detailUrl', None)

        image_label = item[1]['value'].get('image', {}).get('label', None)
        image_standard_url = item[1]['value'].get('image', {}).get('standard', None)
        image_thumb_url = item[1]['value'].get('image', {}).get('thumb', None)

        manufacturer_type = item[1]['value'].get('manufacturer', {}).get('type', None)
        manufacturer_label = item[1]['value'].get('manufacturer', {}).get('value', {}).get('label', None)
        manufacturer_url = item[1]['value'].get('manufacturer', {}).get('value', {}).get('url', None)
        manufacturer_type_val = item[1]['value'].get('manufacturer', {}).get('value', {}).get('type', None)
        manufacturer_external = item[1]['value'].get('manufacturer', {}).get('value', {}).get('external', None)
        manufacturer_id = item[1]['value'].get('manufacturer', {}).get('id', None)
        manufacturer_analyticsTag = item[1]['value'].get('manufacturer', {}).get('analyticsTag', None)

        quantity = item[2]['value'][0].get('quantity', None)
        quantity_label = item[2]['value'][0].get('label', None)

        price_list = item[3]['value']
        pricing_raw = price_list
        price_dict = {}
        for index, price_item in enumerate(price_list):
            unit_price = price_item['unitPrice']
            quantity = price_item['quantity']
            label = price_item['label']
            price_dict[f"price {index + 1}"] = {'unit_price': unit_price, 'quantity': quantity, 'label': label}
        price_dict['pricing_raw'] = pricing_raw

        # TODO остановился на этом. Это номер 4 в json
        # link_to_digi_manufact =

        print(f"productID_1: {productID_1}")
        print(f"productID_2: {productID_2}")
        print(f"productNumber: {productNumber}")
        print(f"datasheetUrl: {datasheetUrl}")
        print(f"description: {description}")
        print(f"detailUrl: {detailUrl}")
        print(f"image_label: {image_label}")
        print(f"image_standard_url: {image_standard_url}")
        print(f"image_thumb_url: {image_thumb_url}")
        print(f"manufacturer_type: {manufacturer_type}")
        print(f"manufacturer_label: {manufacturer_label}")
        print(f"manufacturer_url: {manufacturer_url}")
        print(f"manufacturer_type_val: {manufacturer_type_val}")
        print(f"manufacturer_external: {manufacturer_external}")
        print(f"manufacturer_id: {manufacturer_id}")
        print(f"manufacturer_analyticsTag: {manufacturer_analyticsTag}")
        print(f"quantity: {quantity}")
        print(f"quantity_label: {quantity_label}")
        print(f"price dict: {price_dict}")


def parse_json_recursive(json_object, path=''):
    """Рекурсивно обходит JSON объект, сохраняя все ключи и их значения."""
    if isinstance(json_object, dict):
        for k, v in json_object.items():
            current_path = f"{path}.{k}" if path else k
            if isinstance(v, (dict, list)):
                parse_json_recursive(v, current_path)
            else:
                # Здесь вы можете обработать и сохранить пару ключ-значение
                print(f"Ключ: {current_path} - Значение: {v}")
    elif isinstance(json_object, list):
        for i, item in enumerate(json_object):
            parse_json_recursive(item, f"{path}[{i}]")

# parse_json_recursive(draft_file['data']['products'])
