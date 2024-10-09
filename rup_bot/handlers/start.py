from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

from rup_bot.phrases import responses

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text = responses.get('get_info')),
        KeyboardButton(text = responses.get('upload_info')),
    )

    await message.answer(
        text = responses.get('start').format(message.from_user.full_name),
        reply_markup = builder.as_markup(resize_keyboard = True)
    )
