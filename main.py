import asyncio
from data.log import logger
from loader import dp, bot, db

# Импорт роутеров
from handlers.user import router as user_router
from handlers.admin import router as admin_router
from states.admin import router as state_admin_router


async def main():
    """коннектим бд, подключаемся к роутерам, запускаем бота"""
    await db.connect()

    dp.include_router(user_router)
    dp.include_router(admin_router)
    dp.include_router(state_admin_router)

    logger.info('Бот успешно запущен')
    # log(1, 'Бот успешно запущен', '','type.INFO')

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
