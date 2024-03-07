import json


# Функция для чтения и вывода содержимого JSON файла
def read_and_print_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        print(type(data))
        # # Вывод ключей верхнего уровня
        print("Ключи верхнего уровня в JSON файле:", list(data.keys()))
        #
        # # Пример вывода количества элементов для первой таблицы (первого ключа)
        if data.keys():
            first_key = list(data.keys())[2]
            print(f"Количество записей в '{first_key}':", len(data[first_key]))
        #
        #     # Вывести первую запись из первой таблицы для примера
            if len(data[first_key]) > 0:
                print(f"Первая запись из '{first_key}':", data[first_key][0])


# Путь к вашему JSON файлу
# file_path = 'products.json'
# read_and_print_json(file_path)
