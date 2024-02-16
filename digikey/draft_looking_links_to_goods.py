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

стр 14 - 
стр 13 - 
стр 12 - N4IgrCBcoA5QjAJgDQhnS8AMWC%2Bug
стр 11 - N4IgrCBcoA5QjPANCGdLwAyYL46A
стр 10 - N4IgrCBcoA5QjABgDQhnSTEF9tA
стр 9 -  N4IgrCBcoA5QnAGhDOkCMAGTBfHQ
стр 8 -  N4IgrCBcoA5QHAGhDOkCMAGTBfHQ
стр 7 -  N4IgrCBcoA5Q7AGhDOkCMAGTBfHQ
стр 6 -  N4IgrCBcoA5QbAGhDOkCMAGTBfHQ
стр 5 -  N4IgrCBcoA5WAaEM6QIwAYMF9tA
стр 4 -  N4IgrCBcoA5QLAGhDOkCMAGTBfHQ
стр 3 -  N4IgrCBcoA5QzAGhDOkCMAGTBfHQ
стр 2 -  N4IgrCBcoA5QTAGhDOkCMAGTBfHQ
стр 1 -  N4IgrCBcoA5QjAGhDOl4AYMF9tA

"""
params = {
    's': 'N4IgrCBcoA5QjAGhDOl4AYMF9tA',

}

response = requests.get('https://www.digikey.es/en/products/filter/chassis-mount-resistors/54', params=params, headers=headers)


with open('probe.html', 'w') as f:
    f.write(response.text)