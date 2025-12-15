from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import asyncio
import os
import logging

# Загружаем переменные из .env
load_dotenv()

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot=Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("Привет, я бот парсер.\nПока я нахожусь в разработке и доступны лишь немногие функции")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info('Бот успешно запущен')
    asyncio.run(main())
