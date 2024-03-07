import psycopg2
from dotenv import load_dotenv
import os
import csv
import json
load_dotenv()

DB_HOST = os.getenv("HOST_REMOTE")
DB_PORT = os.getenv("PORT_REMOTE")
DB_USER = os.getenv("USER_REMOTE")
DB_PASSWORD = os.getenv("PASSWORD_REMOTE")
DB_DATABASE = os.getenv("DB_NAME_REMOTE")


def show_table_names():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
    """)

    print(conn)
    print(cur)
    rows = cur.fetchall()

    table_names = []
    if rows:
        print("Таблицы в схеме 'public':")
        for row in rows:
            table_names.append(row[0])
    else:
        print("Таблиц в схеме 'public' не найдено.")

    cur.close()
    conn.close()
    return table_names


def show_table_schema(table_name):
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_schema = 'public' AND table_name = %s;
    """, (table_name,))

    print(f"Схема таблицы {table_name}:")
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(f"Столбец: {row[0]}, Тип: {row[1]}")
    else:
        print(f"Столбцы для таблицы {table_name} не найдены.")

    cur.close()
    conn.close()


def execute_select_query(table_name):
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    cur = conn.cursor()

    # Формирование безопасного запроса с использованием параметризации
    cur.execute(f"SELECT voltage_rating FROM public.{table_name};")

    print(f"Результаты запроса к таблице {table_name}:")
    rows = cur.fetchall()

    set_res = []
    if rows:
        for row in rows:
            print(row)
            set_res.append(row[0])
        print(len(rows))
        print(set(set_res))
    else:
        print(f"Данные по запросу к таблице {table_name} не найдены.")

    cur.close()
    conn.close()


def export_table_to_csv(table_name, csv_file_path):
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    cur = conn.cursor()

    try:
        with open(csv_file_path, 'w') as f:
            cur.copy_expert(f"COPY {table_name} TO STDOUT WITH CSV HEADER", f)
            print(f"Данные из таблицы {table_name} успешно экспортированы в {csv_file_path}")
    except Exception as e:
        print(f"Произошла ошибка при экспорте данных: {e}")
    finally:
        cur.close()
        conn.close()


"""category_name"""

# execute_select_query("heavy_duty_connector_inserts_modules")

# Пример использования:
table_name = 'only_images_for_project'
csv_file_path = f'{table_name}.csv'  # Укажите путь к файлу CSV
# export_table_to_csv(table_name, csv_file_path)

"""heavy_duty_connector_inserts_modules"""

def fetch_data_and_write_to_csv(table_names):
    # Подключение к БД
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    cur = conn.cursor()

    # Открываем файл для записи
    with open('categories_and_tables.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['table_name', 'category_name', 'subcategory_name'])

        for table in table_names:
            if table != 'only_images_for_project':
                try:
                    # Извлечение данных из каждой таблицы
                    cur.execute(f"SELECT category_name, subcategory_name FROM \"{table}\" LIMIT 1;")
                    result = cur.fetchone()
                    if result:
                        # Запись данных в файл
                        writer.writerow([table, result[0], result[1]])
                except Exception as e:
                    print(f"Ошибка при обработке таблицы {table}: {e}")
                    continue

    # Закрытие соединений
    cur.close()
    conn.close()



def fetch_data_and_incrementally_write_to_json(table_names):
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    cur = conn.cursor()

    with open('products.json', 'w', encoding='utf-8') as json_file:
        first_table = True
        json_file.write('{\n')  # Начало объекта JSON

        for i, table in enumerate(table_names):
            if table != 'only_images_for_project':
                try:
                    cur.execute(f"SELECT * FROM \"{table}\";")
                    rows = cur.fetchall()
                    column_names = [desc[0] for desc in cur.description]

                    table_data = [dict(zip(column_names, row)) for row in rows]

                    # Если это не первая таблица, добавляем запятую перед новым ключом
                    if not first_table:
                        json_file.write(',\n')
                    else:
                        first_table = False

                    # Преобразование данных таблицы в строку JSON и запись в файл
                    table_json = json.dumps({table: table_data}, ensure_ascii=False, indent=4)
                    json_file.write(table_json)

                    print(f'{table} готово!')
                except Exception as e:
                    print(f"Ошибка при обработке таблицы {table}: {e}")
                    continue

        json_file.write('\n}')  # Конец объекта JSON

    cur.close()
    conn.close()


tables = show_table_names()

fetch_data_and_incrementally_write_to_json(tables[:3])
# fetch_data_and_write_to_csv(tables)


