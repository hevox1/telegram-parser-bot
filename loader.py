from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=storage)