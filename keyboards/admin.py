from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

"""Inline Клавиатура меню, которая будет высвечиваться админу после команды /admin"""
inline_kb_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="➕ Добавить источник", callback_data='new_source'),
         InlineKeyboardButton(text="📋 Список источников", callback_data='list_of_source')],
        [InlineKeyboardButton(text="❌ Выйти", callback_data='close_admin_menu')],
    ],
)