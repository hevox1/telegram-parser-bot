from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncpg
from aiogram.fsm.storage.memory import MemoryStorage
from config import *
from database.db import Database

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def init_db():
    pool = await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        database=DB_NAME,
        password=DB_PASS
        )
    return Database(pool)
