import asyncio
import asyncpg
from dotenv import load_dotenv
import os
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")
PROXY_ADDRESS = os.getenv("PROXY_ADDRESS")
async def run():
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,
                                 host=DB_HOST, port=DB_PORT)

    print(f"Connected to{conn}")

    await conn.close()


async def update_table_structure(conn, table_name, columns):
    existing_columns = await fetch_table_columns(conn, table_name)
    missing_columns = [col for col in columns if col not in existing_columns]

    for column in missing_columns:
        await add_column_to_table(conn, table_name, column)

async def fetch_table_columns(conn, table_name):
    query = f"""SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';"""
    rows = await conn.fetch(query)
    return [row['column_name'] for row in rows]



async def add_column_to_table(conn, table_name, column_name):
    query = f"""ALTER TABLE "{table_name}" ADD COLUMN "{column_name}" TEXT;"""
    await conn.execute(query)



async def create_table_with_columns(conn, table_name, columns):
    columns_with_type = [f'"{col}" text' for col in columns]


    columns_str = ', '.join(columns_with_type)
    query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_str});'
    print(query)
    await conn.execute(query)

async def insert_data(conn, table_name, columns, data):
    await update_table_structure(conn, table_name, columns)


    placeholders = ', '.join(f'${i+1}' for i in range(len(columns)))
    query = f'INSERT INTO "{table_name}" ({", ".join(columns)}) VALUES ({placeholders})'
    await conn.execute(query, *data)

