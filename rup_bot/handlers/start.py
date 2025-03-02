from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from rup_bot.db.db_queries import check_user_into_students
from rup_bot.utils.keyboard_builder import make_keyboard_sign_up, \
    make_keyboard_get_data_and_upload_data

from rup_bot.phrases import responses

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    if len(check_user_into_students(message.from_user.id)) == 0:
        keyboard = await make_keyboard_sign_up()
    else:
        keyboard = await make_keyboard_get_data_and_upload_data()

    await state.clear()

    await message.answer(
        text = responses.get('start').format(message.from_user.full_name),
        reply_markup = keyboard
    )
