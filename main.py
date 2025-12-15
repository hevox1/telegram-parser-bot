from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import logging
from loader import dp, bot

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("Привет, я бот парсер.\nПока я нахожусь в разработке и доступны лишь немногие функции")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info('Бот успешно запущен')
    asyncio.run(main())
