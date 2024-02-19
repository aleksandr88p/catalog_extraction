from bs4 import BeautifulSoup
import json
sourse = 'digi.html'

with open(sourse) as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cats_to_scrape = ['Audio Products',
                  'Battery Products',
                  'Capacitors',
                  'Circuit Protection',
                  'Connectors, Interconnects',
                  'Crystals, Oscillators, Resonators',
                  'Discrete Semiconductor Products',
                  'Inductors, Coils, Chokes',
                  'Integrated Circuits (ICs)',
                  'Isolators',
                  'Optoelectronics',
                  'Power Supplies - Board Mount',
                  'Relays',
                  'Resistors',
                  'RF and Wireless',
                  'Sensors, Transducers',
                  'Switches']





final_dict = {}
category_containers = soup.find_all("div", class_="tss-t78qa5-categoryContainer")
for container in category_containers:
    category_link = container.find("a", class_="tss-rl8wyr-root-categoryLink")
    category_name = category_link.text.strip()
    category_url = "https://www.digikey.es" + category_link['href']
    if category_name in cats_to_scrape:
        final_dict[category_name] = {"subCategories": {}}
        sub_categories = container.find_all("li", class_="tss-jir0y-NthLevelCategory-categoryListItem")
        for sub_cat in sub_categories:
            nested_sub_categories = sub_cat.find("ul")  # Ищем вложенные категории здесь
            sub_sub_cat_dict = {}
            if nested_sub_categories:
                nested_sub_cats = nested_sub_categories.find_all("li")
                for one_nested_cat in nested_sub_cats:
                    nested_sub_cat_link = one_nested_cat.find("a")
                    count_items = nested_sub_cat_link.find('span').text
                    nested_sub_cat_name = nested_sub_cat_link.text.replace(count_items, "").strip()
                    nested_sub_cat_url = "https://www.digikey.es" + nested_sub_cat_link['href']
                    sub_sub_cat_dict[nested_sub_cat_name] = {"url": nested_sub_cat_url}
            sub_category_link = sub_cat.find("a", class_="tss-gqjq9w-root-NthLevelCategory-categoryAnchor")
            cnt_itm = sub_category_link.find('span').text
            sub_category_name = sub_category_link.text.strip().replace(cnt_itm, '').strip()
            sub_category_url = "https://www.digikey.es" + sub_category_link['href']
            final_dict[category_name]["subCategories"][sub_category_name] = {"url": sub_category_url, "subSubCategories": sub_sub_cat_dict}





# print(json.dumps(final_dict, indent=4))


# with open('links_to_scrape_OLD_DRAFT.json', 'w', encoding='utf-8') as f:
#     # Используем json.dump для записи данных. Указываем indent=4 для красивого форматирования
#     json.dump(final_dict, f, ensure_ascii=False, indent=4)