from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from config import ADMIN_ID
from keyboards.admin import inline_kb_admin
from keyboards.reply import reply_kb_menu
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()

def is_admin(user_id: int) -> bool:
    """Проверяет, является ли пользователь админом"""
    return user_id in ADMIN_ID

@router.message(Command("admin"))
async def admin(message: Message):
    """Если пользователь является админом - предоставляем ему доступ в админ панель"""
    if is_admin(message.from_user.id):
        await message.answer("✅ Доступ разрешен",
                             reply_markup=inline_kb_admin),
        logger.info(f'В админ панель зашел пользователь, его айди: {message.from_user.id}')
    else:
        await message.answer("⛔ Требуются права администратора")
        logger.info(f'Зафиксирована попытка доступа в админ панель, айди пользователя: {message.from_user.id}')

@router.callback_query(F.data == "close_admin_menu")
async def close_admin_menu(callback: CallbackQuery):
    """Выход из админ панели с удалением сообщения"""
    await callback.message.delete()

    await callback.message.answer("Админ панель закрыта.",
                       reply_markup=reply_kb_menu)

    await callback.answer() # Убираем "часики" у кнопки