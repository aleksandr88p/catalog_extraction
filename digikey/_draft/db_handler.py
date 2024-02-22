# import asyncio
# import asyncpg
#
#
# async def run():
#     conn = await asyncpg.connect(user="catalog_user", password="catalogUSERpassword", database="draftcatalog",
#                                  host="localhost", port=5432)
#
#     print(f"Connected to{conn}")
#
#     await conn.close()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())



import asyncio
import asyncpg
import logging

logging.basicConfig(filename='parsing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def create_table_if_not_exists(conn, table_name, columns):
    column_str = ', '.join([f"{col} TEXT" for col in columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_str});"
    await conn.execute(create_table_query)
    logging.info(f"Table {table_name} checked/created.")

async def insert_data(conn, table_name, columns, data):
    values_placeholder = ', '.join(['$' + str(i+1) for i in range(len(columns))])
    insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values_placeholder})"
    await conn.execute(insert_query, *data)
    logging.info(f"Data inserted into {table_name}.")