import aiosqlite


class Database:

    def __init__(self, db_path):
        self.path = db_path
        self.connection = None
        self.cursor = None


    async def connect(self):
        self.connection = await aiosqlite.connect(self.path)
        self.cursor = await self.connection.cursor()


    async def close(self):
        await self.cursor.close()
        await self.connection.close()
