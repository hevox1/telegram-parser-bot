from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Создание роутера, с помощью которого в будущем будут произведены импорты хэндлеров
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    """Стандартный запуск бота"""
    await message.answer('Привет, я бот парсер.\
    \nПока я нахожусь в разработке и доступны лишь немногие функции')


@router.message(Command("help"))
async def help(message: Message):
    """help команда, помогает пользователя понять,
    для чего предназначен бот и какие команды сейчас доступны"""
    await message.answer('Я бот, предназначенный для автоматического\
    парсинга данных с сайтов, их хранения в базе данных.\
    \nВсе доступные команды на данный момент ты можешь посмотреть в нижнем левом углу!')
