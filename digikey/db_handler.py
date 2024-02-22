import asyncio
import asyncpg


async def run():
    conn = await asyncpg.connect(user="catalog_user", password="catalogUSERpassword", database="draftcatalog",
                                 host="localhost", port=5432)

    print(f"Connected to{conn}")

    await conn.close()


async def create_table_with_columns(conn, table_name, columns):
    # Убедитесь, что каждый столбец имеет тип данных
    columns_with_type = [f'"{col}" text' for col in columns]

    # Удаляем дублирование добавления 'category_name text', 'subcategory_name text', если они уже есть в columns
    # columns_with_type уже содержит 'category_name' и 'subcategory_name' с типом данных 'text'

    columns_str = ', '.join(columns_with_type)  # Строка со столбцами и типами данных для SQL запроса
    query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_str});'
    print(query)  # Для отладки
    await conn.execute(query)


async def insert_data(conn, table_name, columns, data):
    # Генерация списка значений и строки запроса для вставки данных
    placeholders = ', '.join(f'${i+1}' for i in range(len(columns)))
    query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
    print(query)
    await conn.execute(query, *data)
