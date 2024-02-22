import asyncpg
import asyncio


async def fetch_table_content(table_name: str):
    # Замените эти значения на свои параметры подключения
    conn = await asyncpg.connect(user="catalog_user", password="catalogUSERpassword", database="draftcatalog",
                                 host="localhost", port=5432)

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
    conn = await asyncpg.connect(user="catalog_user", password="catalogUSERpassword", database="draftcatalog",
                                 host="localhost", port=5432)

    # SQL запрос для получения списка имен таблиц
    # Этот запрос выбирает имена всех таблиц из схемы "public"
    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public' AND table_type='BASE TABLE';
    """

    # Выполняем запрос
    rows = await conn.fetch(query)

    # Выводим результаты
    print("List of tables in the database:")
    for row in rows:
        print(row['table_name'])

    # Закрываем соединение
    await conn.close()


async def fetch_table_schema(table_name: str):
    conn = await asyncpg.connect(user="catalog_user", password="catalogUSERpassword", database="draftcatalog",
                                 host="localhost", port=5432)
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
    conn = await asyncpg.connect(user="catalog_user", password="catalogUSERpassword", database="draftcatalog",
                                 host="localhost", port=5432)
    query = f"DROP TABLE IF EXISTS {table_name};"
    await conn.execute(query)
    print(f"Table {table_name} has been dropped.")
    await conn.close()

# asyncio.run(fetch_table_names())
res = asyncio.run(fetch_table_content(table_name='alarms_buzzers_and_sirens'))

# print(len(res))
# for index, row in enumerate(res):
#     print(row)
    # if index == 15:
    #     break

# res = asyncio.run(fetch_table_schema(table_name='alarms_buzzers_and_sirens'))
# print(len(res))
# asyncio.run(drop_table("alarms_buzzers_and_sirens"))
