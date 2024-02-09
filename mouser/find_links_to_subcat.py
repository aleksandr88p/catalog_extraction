import time
import random
import json
from bs4 import BeautifulSoup

links = ['https://www.mouser.com/c/semiconductors/', 'https://www.mouser.com/c/circuit-protection/',
'https://www.mouser.com/c/connectors/', 'https://www.mouser.com/c/electromechanical/', 'https://www.mouser.com/c/embedded-solutions/',
'https://www.mouser.com/c/optoelectronics/',
'https://www.mouser.com/c/passive-components/', 'https://www.mouser.com/c/rf-wireless/', 'https://www.mouser.com/c/sensors/']


import requests

cookies = {
    'datadome': 'JeFyqlfq~8Dcz~TbxqsT6T879MC0v~mAELNJk9jaMjJsnhHdXjGPs5Vl4X5SPwVuCDzSxELsNRgXgcXT0VDMIYvK4c3R3NrlpOZIoTFp76pShjp0JyiDaJ0W_JKhhLUo',
    'CARTCOOKIEUUID': '49a8b42c-c718-4e96-9190-e1c41b4edd00',
    'preferences': 'pl=en-GB&pc_eu=EUR&ps=eu',
    'sbsd': 'sn8bqS/Kf1YJzXqQRn0PIVuWCcDJYsOIZIvx0Q0h5k8R3+a9Kh4OluSXSkscGX8H1vj+uV/7xvfElE6LnDeZapsxqPMxMURaSCVkl9xJga9LBOuD+mfRnifqz0+5BZuzd+z6JoMo39d7eN08gLUB+Bg==',
    '_abck': 'FAD54878A75E40B024DE461242ECFDA8~-1~YAAQ4W1lX4FPhkmNAQAAO6LWegvmWqwmxdJfwbaJGQjkKLnf9yNup+q6dYfyuPkVxUjflhD4/8x02m6pOfd2baz8aQUgt1k5iCIUEVWG1+HF1EovAteXoEJmuo10PRozJEau93K1yex6vBoZMpTSxW9Wk1297B5TShL4Bw6zf57900gRL+QczFDav+yOw7mzudd+Sl9fQnba44Zwfreu7Z2OdpUjiFMYKo5KDhv+/TERJzkbqKsLNMYiAx7HjO14cFe1MQg2/D1bimIBfjEVr5Px8Bk0929Q5Nc/NZG8f2GO8LbDK6Hc2MDPEj7LM6Bi50vKrDZOT3jFctEwSVstINXDsbMifRfy1/gcyS7vS67v3hw4/IFisclvdU4bal3GNHwPgtg52pUSRzdsw9zU0qOc7zYVvw1qvY2P4p7CK2VgM88RUA==~-1~-1~-1',
    '_gcl_au': '1.1.441325644.1707162635',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Feb+05+2024+20%3A55%3A02+GMT%2B0100+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1689a969-b332-4547-ac7f-47779784b2cd&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=ES%3BVC&AwaitingReconsent=false',
    'RT': '"z=1&dm=mouser.com&si=d579bf9d-c7d4-4552-82f2-8baa18624e56&ss=ls9cjxix&sl=3&tt=4ni&bcn=%2F%2F684dd326.akstat.io%2F&ld=5tab&ul=9g2k"',
    '_fbp': 'fb.1.1707162636217.1262047902',
    'LPVID': 'YxNTA1YTE0YmFhMjFiOWQ0',
    'OptanonAlertBoxClosed': '2024-02-05T19:52:26.907Z',
    '_ga': 'GA1.2.363016698.1707162747',
    '_gid': 'GA1.2.1265808665.1707162747',
    '_ga_1KQLCYKRX3': 'GS1.1.1707162747.1.1.1707163073.0.0.0',
    '_ga_15W4STQT4T': 'GS1.1.1707162747.1.1.1707163073.60.0.0',
    'fs_uid': '#Z1BBJ#e3bd787f-1bb2-4497-ba8c-b625a5aa2ea5:8ce9186f-aef7-4b93-af41-8fb132a3ac15:1707162747635::3#/1738698747',
    '_rdt_uuid': '1707162635139.61239934-34b6-4f17-bfbe-e8d0015e6fb3',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'datadome=JeFyqlfq~8Dcz~TbxqsT6T879MC0v~mAELNJk9jaMjJsnhHdXjGPs5Vl4X5SPwVuCDzSxELsNRgXgcXT0VDMIYvK4c3R3NrlpOZIoTFp76pShjp0JyiDaJ0W_JKhhLUo; CARTCOOKIEUUID=49a8b42c-c718-4e96-9190-e1c41b4edd00; preferences=pl=en-GB&pc_eu=EUR&ps=eu; sbsd=sn8bqS/Kf1YJzXqQRn0PIVuWCcDJYsOIZIvx0Q0h5k8R3+a9Kh4OluSXSkscGX8H1vj+uV/7xvfElE6LnDeZapsxqPMxMURaSCVkl9xJga9LBOuD+mfRnifqz0+5BZuzd+z6JoMo39d7eN08gLUB+Bg==; _abck=FAD54878A75E40B024DE461242ECFDA8~-1~YAAQ4W1lX4FPhkmNAQAAO6LWegvmWqwmxdJfwbaJGQjkKLnf9yNup+q6dYfyuPkVxUjflhD4/8x02m6pOfd2baz8aQUgt1k5iCIUEVWG1+HF1EovAteXoEJmuo10PRozJEau93K1yex6vBoZMpTSxW9Wk1297B5TShL4Bw6zf57900gRL+QczFDav+yOw7mzudd+Sl9fQnba44Zwfreu7Z2OdpUjiFMYKo5KDhv+/TERJzkbqKsLNMYiAx7HjO14cFe1MQg2/D1bimIBfjEVr5Px8Bk0929Q5Nc/NZG8f2GO8LbDK6Hc2MDPEj7LM6Bi50vKrDZOT3jFctEwSVstINXDsbMifRfy1/gcyS7vS67v3hw4/IFisclvdU4bal3GNHwPgtg52pUSRzdsw9zU0qOc7zYVvw1qvY2P4p7CK2VgM88RUA==~-1~-1~-1; _gcl_au=1.1.441325644.1707162635; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Feb+05+2024+20%3A55%3A02+GMT%2B0100+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1689a969-b332-4547-ac7f-47779784b2cd&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=ES%3BVC&AwaitingReconsent=false; RT="z=1&dm=mouser.com&si=d579bf9d-c7d4-4552-82f2-8baa18624e56&ss=ls9cjxix&sl=3&tt=4ni&bcn=%2F%2F684dd326.akstat.io%2F&ld=5tab&ul=9g2k"; _fbp=fb.1.1707162636217.1262047902; LPVID=YxNTA1YTE0YmFhMjFiOWQ0; OptanonAlertBoxClosed=2024-02-05T19:52:26.907Z; _ga=GA1.2.363016698.1707162747; _gid=GA1.2.1265808665.1707162747; _ga_1KQLCYKRX3=GS1.1.1707162747.1.1.1707163073.0.0.0; _ga_15W4STQT4T=GS1.1.1707162747.1.1.1707163073.60.0.0; fs_uid=#Z1BBJ#e3bd787f-1bb2-4497-ba8c-b625a5aa2ea5:8ce9186f-aef7-4b93-af41-8fb132a3ac15:1707162747635::3#/1738698747; _rdt_uuid=1707162635139.61239934-34b6-4f17-bfbe-e8d0015e6fb3',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}


c = 1
links_name = ['page1', 'page2', 'page3', 'page4', 'page5', 'page6', 'page7', 'page8', 'page9']
# for link in links:
#     # response = requests.get('https://www.mouser.com/c/semiconductors/', cookies=cookies, headers=headers)
#     response = requests.get(link, cookies=cookies, headers=headers)
#
#     if response.status_code != 200:
#         print(response.status_code)
#     else:
#         print(response.status_code)
#         links_name.append(f'page{c}')
#         with open(f'page{str(c)}.html', 'w', encoding='utf-8') as file:
#             file.write(response.text)
#         c += 1
#         time.sleep(random.randint(5, 10))
# print(links_name)
semicond = {
    "semiconductors": {
        "sub_category": [
            {
                "Discrete Semiconductors": "https://www.mouser.com/c/semiconductors/discrete-semiconductors/"
            },
            {
                "Embedded Processors & Controllers": "https://www.mouser.com/c/semiconductors/integrated-circuits-ics/embedded-processors-controllers/"
            },
            {
                "Integrated Circuits - ICs": "https://www.mouser.com/c/semiconductors/integrated-circuits-ics/"
            },
            {
                "Memory ICs": "https://www.mouser.com/c/semiconductors/memory-ics/"
            },
            {
                "Wireless & RF Semiconductors": "https://www.mouser.com/c/semiconductors/wireless-rf-semiconductors/"
            }
        ]
    }
}


'''
significantLink  все ссылки

'''


dict_with_all_links = {'semiconductors': {'sub_category': {}}}

def find_sublinks_semiconductors(page):
    with open(f'{page}.html', 'r') as file:
        html = file.read()

    general_link = "https://www.mouser.com"
    soup = BeautifulSoup(html, 'html.parser')

    all_sub_cat_sections = soup.find_all('div', attrs={"class": "sub-category-section"})
    for sub_cat in all_sub_cat_sections:
        sub_cat_name = sub_cat.find('h3').find('a').get_text()
        sub_cat_link = general_link + sub_cat.find('a')['href']

        all_sub_subcategories_link = sub_cat.find_all(attrs={"itemprop": "significantLink"})
        sub_subcategories = []
        for l in all_sub_subcategories_link:
            sub_sub_cat_name = l.get_text(strip=True)
            sub_sub_cat_link = general_link + l['href']
            sub_subcategories.append({sub_sub_cat_name: sub_sub_cat_link})

        dict_with_all_links['semiconductors']['sub_category'][sub_cat_name] = sub_subcategories


dict_with_other_links = {}
def find_other_links(page):
    with open(f'{page}.html', 'r') as file:
        html = file.read()
        general_link = "https://www.mouser.com"
        soup = BeautifulSoup(html, 'html.parser')
        category_name = soup.find('h1').get_text().strip() # работает
        # dict_with_other_links[category_name.lower()] = {'sub_category': {}}
        # print(category_name)

        sub_cat_raw = soup.find_all('div', attrs={"class": "div-cat-title"})
        sub_categories = []
        for scr in sub_cat_raw:
            sub_cat_name = scr.get_text(strip=True).split('(')[0]
            sub_cat_link = general_link + scr.find('a')['href']
            sub_categories.append({sub_cat_name: sub_cat_link})
            # print(sub_cat_name, sub_cat_link)
        dict_with_other_links[category_name.lower()] = sub_categories




# for link in links_name[1::]:
#     find_other_links(link)



# with open('links_semiconductors.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_with_all_links, f, ensure_ascii=False, indent=4)


# with open('all_other_links.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_with_other_links, f, ensure_ascii=False, indent=4)