import json
import requests
from bs4 import BeautifulSoup

filename = 'links_semiconductors.json'
with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data['semiconductors']['sub_category'].keys())

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

# links_all_semicond()
"""https://www.mouser.com/c/semiconductors/discrete-semiconductors/diodes-rectifiers/"""