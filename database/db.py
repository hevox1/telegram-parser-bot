class Database:
    def __init__(self, pool):
        self.pool = pool

    async def add_source(self, name: str, url: str):
        query = """
        INSERT INTO sources (name, url)
        VALUES (1$, 2$)
        """
        async with self.pool.acquire() as conn:
            await conn.execute(query, name, url)
