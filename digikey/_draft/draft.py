import requests
from bs4 import BeautifulSoup

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

"""
https://www.digikey.es/en/products/filter/coaxial-connectors-rf/coaxial-connector-rf-adapters/374
https://www.digikey.es/en/products/filter/barrel-connector-cables/barrel-audio-cables/463
?s=N4IgrCBcoA5QjAGhDOl4AYMF9tA эта часть похоже на то что бы отображалось по 100 элементов на странице

"""


# response = requests.get(
#     'https://www.digikey.es/en/products/filter/coaxial-connectors-rf/coaxial-connector-rf-adapters/374?s=N4IgrCBcoA5QjAGhDOl4AYMF9tA',
#     headers=headers,
# )
#
# with open('coaxial-connector-rf-adapters.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)

def download_image(url, filename):
    '''
    download image
    :param url:
    :param filename:
    :return:
    '''
    with requests.get(url, headers=headers, stream=True) as response:
        response.raise_for_status()  # Проверка на успешный ответ
        with open(f"{filename}.jpg", 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

def download_pdf(url, filename):
    '''
    download pdf datasheet
    :param url:
    :param filename:
    :return:
    '''
    with requests.get(url, headers=headers, stream=True) as response:
        response.raise_for_status()  # Проверка на успешный ответ
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


def find_links_to_product(page):
    with open(page, 'r') as f:
        html_content = f.read()

        soup = BeautifulSoup(html_content, 'lxml')
        all_containers = soup.find_all('div', attrs={
            'class': 'MuiGrid-root MuiGrid-container MuiGrid-wrap-xs-nowrap css-jgm9a3'})
        for container in all_containers:
            description_element_first = container.find(class_=lambda value: value and 'Description' in value).get_text(
                strip=True)
            link_raw = container.find('a', attrs={'data-product-id': True})
            link = 'https://www.digikey.es' + link_raw['href']
            if link_raw:
                image = link_raw.find('img')
                if image:
                    image_link = 'https:' + image['data-standard-url']
                    link_text = image.get('alt')
                else:
                    image_link = None
                    link_text = None
            download_image(url=image_link, filename=link_text)
            print(link_text)
            print(description_element_first)
            print(link)
            print(image_link)
            break


# page = 'barrel-audio-cables.html'
# find_links_to_product(page=page)



all_links_to_categories_digikey = {
    ""
}



def make_dict_with_categories(data: dict):
    """
    N4IgrCBcAEoA5WgRgDTRHBMkAYcF98g this is the first page with 500 items on page
    надо потом проверить как создаются ссылки
    :param data:
    :return:
    """
    new_dict_with_links = {}
    c = 0
    for cat_name1, value in data.items():
        if isinstance(value, dict):
            for subCategories, value2 in value.items():
                for cat_name2, value3 in value2.items():
                    cat_number = value3['url'].split('/')[-1]

                    url_to_download = f"https://www.digikey.es/products/api/v5/filter-page/products-download/{cat_number}"
                    # print(value3['url'])
                    c += 1
                    new_dict_with_links[f"category_{c}"] = {'name_for_table': cat_name2, 'category_name': cat_name1,
                                                            'url_to_download': url_to_download, 'old_url': value3['url']}
                    # if isinstance(value3, dict):
                    #     print(value3)
    return new_dict_with_links
