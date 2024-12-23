from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

from rup_bot.db.db_queries import check_user_into_students

from rup_bot.phrases import responses

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if len(check_user_into_students(message.from_user.id)) == 0:
        builder = ReplyKeyboardBuilder().row(
            KeyboardButton(text = responses.get('sign_up'))
        ).as_markup(resize_keyboard = True)

    else:
        builder = ReplyKeyboardBuilder().row(
            KeyboardButton(text = responses.get('get_data')),
            KeyboardButton(text = responses.get('upload_data'))
        ).as_markup(resize_keyboard = True)

    await message.answer(
        text = responses.get('start').format(message.from_user.full_name),
        reply_markup = builder
    )