import asyncpg
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")


async def fetch_table_content(table_name: str):
    # Замените эти значения на свои параметры подключения
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,
                                 host=DB_HOST, port=DB_PORT)

    # Замените "your_table_name" на имя вашей таблицы
    table_name = f"{table_name}"
    query = f"SELECT * FROM {table_name};"

    # Выполняем запрос
    rows = await conn.fetch(query)

    results = []
    # Выводим результаты
    for row in rows:
        results.append(row)

    # Не забудьте закрыть соединение
    await conn.close()

    return results


async def fetch_table_names():
    # Параметры подключения к базе данных
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,
                                 host=DB_HOST, port=DB_PORT)

    # SQL запрос для получения списка имен таблиц
    # Этот запрос выбирает имена всех таблиц из схемы "public"
    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public' AND table_type='BASE TABLE';
    """

    # Выполняем запрос
    rows = await conn.fetch(query)

    table_names = []
    # Выводим результаты
    # print("List of tables in the database:")
    for row in rows:
        table_names.append(row["table_name"])
        # print(row['table_name'])

    # Закрываем соединение
    await conn.close()
    return table_names


async def fetch_table_schema(table_name: str):
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,
                                 host=DB_HOST, port=DB_PORT)
    query = f"""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema='public' AND table_name='{table_name}';
    """
    rows = await conn.fetch(query)
    column_names = [row['column_name'] for row in rows]
    # Закрываем соединение
    await conn.close()
    return column_names


async def drop_table(table_name: str):
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,
                                 host=DB_HOST, port=DB_PORT)
    query = f"DROP TABLE IF EXISTS {table_name};"
    await conn.execute(query)
    print(f"Table {table_name} has been dropped.")
    await conn.close()


async def create_images_table():
    '''
    таблица для изображений
    :return:
    '''
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE, host=DB_HOST, port=DB_PORT)
    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS only_images_for_project (
                id SERIAL PRIMARY KEY,
                image_url VARCHAR(255) UNIQUE
            );
        ''')
        print("Table 'images' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await conn.close()

asyncio.run(create_images_table())
async def add_base64_column():
    '''
    когда соберу уникальные ссылки, тогда добавлю колонку
    :return:
    '''
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE, host=DB_HOST, port=DB_PORT)
    try:
        await conn.execute('''
            ALTER TABLE only_images_for_project ADD COLUMN image_base64 TEXT;
        ''')
        print("Column 'image_base64' added successfully to 'images' table.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await conn.close()


async def insert_unique_url(image_url: str):
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE, host=DB_HOST, port=DB_PORT)
    try:
        # Используем ON CONFLICT DO NOTHING, чтобы игнорировать попытку вставки дубликатов
        await conn.execute('''
            INSERT INTO only_images_for_project (image_url)
            VALUES ($1)
            ON CONFLICT (image_url) DO NOTHING;
        ''', image_url)
    except Exception as e:
        print(f"An error occurred while inserting URL: {e}")
    finally:
        await conn.close()




async def main():
    table_names = asyncio.run(fetch_table_names())
    for table_name in table_names:
        res = asyncio.run(fetch_table_content(table_name=table_name))
        # print(len(res))
        for index, row in enumerate(res):
            image_url = row['image']
            if "//mm.digikey.com" in image_url:
                await insert_unique_url(image_url=image_url)



# if __name__ == "__main__":
#     asyncio.run(main())



# print(f"There are {c} items")
# res = asyncio.run(fetch_table_schema(table_name='alarms_buzzers_and_sirens'))
# print(len(res))
# asyncio.run(drop_table("alarms_buzzers_and_sirens"))

# asyncio.run(drop_table("vcos_voltage_controlled_oscillators"))
