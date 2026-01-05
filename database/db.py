import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT
        )
        """)

        self.conn.commit()

    def add_source(self, name, url):
        self.cursor.execute(
            "INSERT INTO sources (name, url) VALUES (?, ?)",
            (name, url)
        )

        self.conn.commit()
