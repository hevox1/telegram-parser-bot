import asyncio
import logging
from loader import dp, bot

# Импорт роутеров
from handlers.user import router as user_router
from handlers.admin import router as admin_router
from states.admin import router as state_admin_router

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    # подключаем роутеры
    dp.include_router(user_router)
    dp.include_router(admin_router)
    dp.include_router(state_admin_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info('Бот успешно запущен')
    asyncio.run(main())
