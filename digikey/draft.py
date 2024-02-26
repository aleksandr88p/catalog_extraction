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

# print(c)


col_names = ['Datasheet', 'Image', 'DK Part #', 'Mfr Part#', 'Mfr', 'Supplier', 'Description', 'Stock', "Price",
             '@ qty', 'Tuning Voltage', '(VDC)', '2nd Harmonic Typ', '(dBc) '
             ]

def format_identifier2(identifier):
    """
    Форматирует строку для использования в качестве названия таблицы или колонки в SQL.
    """
    formatted = ''.join(char if char.isalnum() or char == ' ' else '' for char in identifier).replace(' ', '_').lower()
    # Добавляем префикс 'c_' если имя начинается с цифры
    if formatted and formatted[0].isdigit():
        formatted = 'c_' + formatted
    return formatted


def format_identifier1(identifier):
    """
    Форматирует строку для использования в качестве названия таблицы или колонки в SQL.
    Удаляет специальные символы, заменяет пробелы на подчеркивания и приводит к нижнему регистру.
    """
    # Удаляем специальные символы и заменяем пробелы на подчеркивания
    formatted = ''.join(char if char.isalnum() or char == ' ' else '' for char in identifier).replace(' ', '_').lower()
    return formatted

#
# for col in col_names:
#     print(format_identifier2(col))

# print(format_identifier2('VCOs (Voltage Controlled Oscillators)'))