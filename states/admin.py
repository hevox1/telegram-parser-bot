from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from database import db
from keyboards.inline import inline_keyboard_confirm, inline_keyboard_cancel

router = Router()

class AdminAddSource(StatesGroup):
    waiting_for_name = State()
    waiting_for_url = State()
    confirm = State()


@router.callback_query(F.data=="new_source")
async def start_add_source(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminAddSource.waiting_for_name)
    await callback.message.answer('Введите название источника: ',
                                  reply_markup=inline_keyboard_cancel)

@router.message(AdminAddSource.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AdminAddSource.waiting_for_url)
    await message.answer("Отправьте ссылку: ",
                         reply_markup=inline_keyboard_cancel)

@router.message(AdminAddSource.waiting_for_url)
async def process_url(message: Message, state: FSMContext):
    await state.update_data(url=message.text)

    data = await state.get_data()

    await message.answer(f"Подтверждаете?\nНазвание:  {data['name']}, \nURL:  {data['url']}",
                         reply_markup = inline_keyboard_confirm)

    await state.set_state(AdminAddSource.confirm)


@router.callback_query(AdminAddSource.confirm, F.data=="yes_confirm")
async def confirm_add(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
#     сохранение в бд
    await db.add_source(data['name'], data['url'])

    await state.clear()
    await callback.message.answer("✅Источник добавлен!")


@router.callback_query(AdminAddSource.confirm, F.data=="no_confirm")
async def confirm_add(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(AdminAddSource.waiting_for_name)
    await callback.message.answer('Хорошо, тогда начнем заново.\nВведите название источника: ')


@router.callback_query(F.data=="cancel")
async def cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer('❌Действие отменено')

