from aiogram import Router, F
from aiogram.types import Message

from rup_bot.phrases import responses

exception_router = Router()

@exception_router.message(F.text)
async def command_upload_info_handler(message: Message) -> None:
    await message.answer(text = responses.get('exception'))