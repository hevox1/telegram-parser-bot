from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from database.db import Database

bot = Bot(token=BOT_TOKEN)

# FSM хранится в памяти
storage = MemoryStorage()

dp = Dispatcher(storage=storage)

db = Database()
db.create_tables()
