# import sqlite3
#
# class Database:
#     def __init__(self):
#         self.conn = sqlite3.connect("database.db")
#         self.cursor = self.conn.cursor()
#
#     def create_tables(self):
#         self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS sources (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             url TEXT
#         )
#         """)
#
#         self.conn.commit()
#
#     def add_source(self, name, url):
#         self.cursor.execute(
#             "INSERT INTO sources (name, url) VALUES (?, ?)",
#             (name, url)
#         )
#
#         self.conn.commit()

import asyncpg

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user='postgres',
            password='hevox_postgresql',
            database='hevox_bot_parser',
            host='localhost',
            port=5432,
            min_size=1,
            max_size=5
        )

    async def add_source(self, name, url):
        query = """
        INSERT INTO sources (name, url) 
        VALUES ($1, $2)
        """
        """берём соединение из пула"""
        async with self.pool.acquire() as conn:
            await conn.execute(query, name, url)
