from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from keyboards.reply import reply_kb_menu
from data.text import start_text, help_text, opportunities_text

# Создание роутера, с помощью которого в будущем будут произведены импорты хэндлеров
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    """Стандартный запуск бота"""
    await message.answer(text=start_text,
                         reply_markup=reply_kb_menu)


@router.message(Command("help"))
@router.message(F.text == "ℹ️ Помощь")
async def help_command(message: Message):
    """help команда, помогает пользователя понять,
    для чего предназначен бот и какие команды сейчас доступны"""
    await message.answer(text=help_text)

@router.message(F.text == "📊 Возможности")
async def opportunities(message: Message):
    await message.answer(text=opportunities_text)

@router.message(F.text == "❌ Скрыть меню")
async def cleaning_menu(message: Message):
    """Удаляем реплай клавиатуру у конкретного пользователя"""
    await message.answer('Меню скрыто ✅',
    reply_markup = ReplyKeyboardRemove(selective=True)) # selective=True - скрывает только у конкретного пользователя
