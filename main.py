import asyncio
import logging
from loader import dp, bot

# Импорт роутеров
from handlers.user import router as user_router

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


async def main():
    dp.include_router(user_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info('Бот успешно запущен')
    asyncio.run(main())
