from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

"""Клавиатура меню, которая будет высвечиваться пользователю после команды /start"""
reply_kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Возможности"), KeyboardButton(text="ℹ️ Помощь")],
        [KeyboardButton(text="❌ Скрыть меню")]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True # клавиатура автоматически скрывается после того, как пользователь нажмет на любую кнопку
)