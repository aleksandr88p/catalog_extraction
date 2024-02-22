import random
from db_handler import create_table_with_columns, insert_data
import asyncpg
from utils import make_compress_pagination, fetch_with_pagination, format_identifier
import json
import asyncio
import csv
import io


async def main():
    # Создание пула соединений
    pool = await asyncpg.create_pool(user="catalog_user", password="catalogUSERpassword", database="draftcatalog", host="localhost", port=5432)
    print(f"Pool created")


    all_links_path = 'digikey_links.json'
    with open(all_links_path) as f:
        all_links = json.load(f)

    # ЗДЕСь надо переберать страницы или нет?
    for category in all_links:
        name_for_table = all_links[category]['name_for_table']  # нужно для создания таблицы с этим именем
        category_name = all_links[category]['category_name']  # нужно для имени колонки в БД
        subcategory_name = all_links[category]['name_for_table']  # нужно для имени колонки в БД
        url_to_download = all_links[category]['url_to_download']  # нужно парсинга
        old_url = all_links[category]['old_url']  # для хедерсов
        # Форматирование
        formatted_name_for_table = format_identifier(name_for_table)
        formatted_category_name = format_identifier(category_name)
        formatted_subcategory_name = format_identifier(subcategory_name)

        async with pool.acquire() as conn:
            # Теперь conn - это соединение из пула
            max_attempts = 10  # Максимальное количество попыток
            attempt = 0  # Счётчик попыток


            while attempt < max_attempts:
                wait_time = random.randint(1, 3)  # Время ожидания перед повторным запросом в секундах
                content, status = await fetch_with_pagination(url_to_download=url_to_download, old_ulr=old_url, page=1,
                                                              proxy_url='http://5.79.66.2:13010')
                if status == 200 and content:

                    # with open(f"testfile.csv", 'w') as f:
                    #     f.write(content)
                    print(f"*******{status}*******")
                    f = io.StringIO(content)
                    reader = csv.DictReader(f)
                    column_names = reader.fieldnames
                    formatted_column_names = [format_identifier(name) for name in column_names]

                    # После получения formatted_column_names и до цикла чтения строк CSV
                    await create_table_with_columns(conn, formatted_name_for_table,
                                                    formatted_column_names + ['category_name', 'subcategory_name'])

                    for i, row in enumerate(reader):
                        # print(f'row {i + 1}')
                        # Внутри цикла чтения строк CSV
                        data = [row[col] for col in column_names] + [category_name, subcategory_name]
                        await insert_data(conn, formatted_name_for_table,
                                          formatted_column_names + ['category_name', 'subcategory_name'], data)

                    break
                elif status == 204:
                    break
                elif status in [403, 500, 502, 503, 504]:
                    attempt += 1
                    print(f"Ошибка {status}, попытка {attempt} из {max_attempts}. Повтор через {wait_time} секунд...")
                    await asyncio.sleep(wait_time)

                elif status in [429]:
                    attempt += 1
                    print(f"Ошибка {status}, попытка {attempt} из {max_attempts}")
                    await asyncio.sleep(10)

                else:
                    print(f"Непредвиденный статус ответа: {status}. Прекращение попыток.")
                    break  # Прекращение попыток при получении непредвиденного статуса


        break
    # Закрытие пула соединений
    await pool.close()

# asyncio.run(main())


def test_csv_processing():
    with open("fileN4IgrCBcAEoA5WgRgDTRHBMkAYcF98g.csv", 'r') as file:
        reader = csv.DictReader(file)

        column_names = reader.fieldnames
        print('column names:', column_names)

        for i, row in enumerate(reader):
            print(f'row {i + 1}')
            for col_name in column_names:
                print(f"{col_name}: {row[col_name]}")

            if i == 3:
                break
        print('column names:', column_names)

# test_csv_processing()


# async def main():
#     conn = await asyncpg.connect(user="catalog_user", password="catalogUSERpassword", database="draftcatalog",
#                                  host="localhost", port=5432)
#
#     all_links_path = 'digikey_links.json'
#     with open(all_links_path) as f:
#         all_links = json.load(f)
#
#     # ЗДЕСь надо переберать страницы или нет?
#     for category in all_links:
#         name_for_table = all_links[category]['name_for_table']  # нужно для создания таблицы с этим именем
#         category_name = all_links[category]['category_name']  # нужно для имени колонки в БД
#         subcategory_name = all_links[category]['name_for_table']  # нужно для имени колонки в БД
#         url_to_download = all_links[category]['url_to_download']  # нужно парсинга
#         old_url = all_links[category]['old_url']  # для хедерсов
#         # Форматирование
#         formatted_name_for_table = format_identifier(name_for_table)
#         formatted_category_name = format_identifier(category_name)
#         formatted_subcategory_name = format_identifier(subcategory_name)
#         # print(formatted_name_for_table)
#         # print(formatted_category_name)
#         # print(formatted_subcategory_name)
#         # print(name_for_table)
#         # print(category_name)
#         # print(subcategory_name)
#         # print(url_to_download)
#         # print(old_url)
#
#
#         max_attempts = 10  # Максимальное количество попыток
#         attempt = 0  # Счётчик попыток
#
#
#         while attempt < max_attempts:
#             wait_time = random.randint(1, 3)  # Время ожидания перед повторным запросом в секундах
#             content, status = await fetch_with_pagination(url_to_download=url_to_download, old_ulr=old_url, page=1,
#                                                           proxy_url='http://5.79.66.2:13010')
#
#             if status == 200 and content:
#                 print(f"*******{status}*******")
#                 f = io.StringIO(content)
#                 reader = csv.DictReader(f)
#                 column_names = reader.fieldnames
#                 formatted_column_names = [format_identifier(name) for name in column_names]
#
#                 # print('column names:', column_names)
#                 # print(formatted_column_names)
#                 # После получения formatted_column_names и до цикла чтения строк CSV
#                 await create_table_with_columns(conn, formatted_name_for_table,
#                                                 formatted_column_names + ['category_name', 'subcategory_name'])
#
#                 for i, row in enumerate(reader):
#                     print(f'row {i + 1}')
#                     for col_name in column_names:
#                         # Внутри цикла чтения строк CSV
#                         data = [row[col] for col in column_names] + [category_name, subcategory_name]
#                         await insert_data(conn, formatted_name_for_table,
#                                           formatted_column_names + ['category_name', 'subcategory_name'], data)
#                         # print(f"{col_name}: {row[col_name]}")
#                 # print('column names:', column_names)
#                 break
#             elif status == 204:
#                 break
#             elif status in [403, 500, 502, 503, 504]:
#                 attempt += 1
#                 print(f"Ошибка {status}, попытка {attempt} из {max_attempts}. Повтор через {wait_time} секунд...")
#                 await asyncio.sleep(wait_time)
#
#             elif status in [429]:
#                 attempt += 1
#                 print(f"Ошибка {status}, попытка {attempt} из {max_attempts}")
#                 await asyncio.sleep(10)
#
#             else:
#                 print(f"Непредвиденный статус ответа: {status}. Прекращение попыток.")
#                 break  # Прекращение попыток при получении непредвиденного статуса
#
#
#         break
#     await conn.close()
#
# asyncio.run(main())
