from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

"""Подтверждение FSM"""
inline_keyboard_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Верно", callback_data="yes_confirm")],
        [InlineKeyboardButton(text="Нет", callback_data='no_confirm')]
    ]
)

"""Клавиатура для отмены действия FSM"""
inline_keyboard_cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌Отмена", callback_data="cancel")],
    ]
)