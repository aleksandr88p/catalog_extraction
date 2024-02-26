import json


first_file_path = 'digikey_links.json'

# Открываем файл в режиме чтения
with open(first_file_path, 'r') as f:
    # Загружаем содержимое файла JSON в переменную cats
    cats = json.load(f)

c = 0
for cat_number, cat_value in cats.items():
    category_code = cat_value['old_url'].split('/')[-1]
    c += 1

print(c)