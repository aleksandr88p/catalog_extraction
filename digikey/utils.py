import json

path_with_links = 'links_to_scrape.json'

with open(path_with_links, 'r') as f:
    links = json.load(f)

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

# new_dict_links = make_dict_with_categories(links)
# with open('digikey_links.json', 'w') as outfile:
#     json.dump(new_dict_links, outfile, indent=4)