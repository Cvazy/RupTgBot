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
    user = check_user_into_students(message.from_user.id)
    text_message = responses.get('start').format(message.from_user.full_name)

    if len(user) == 0:
        keyboard = await make_keyboard_sign_up()
        text_message += f"\n\n{responses.get('need_to_pass_registration')}"
    else:
        keyboard = await make_keyboard_get_data_and_upload_data()
        text_message += f"\n\n{responses.get('choose_action')}"

    await state.clear()

    await message.answer(
        text = text_message,
        reply_markup = keyboard
    )
