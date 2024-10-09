from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from rup_bot.phrases import responses

help_router = Router()

@help_router.message(Command('help'))
async def command_upload_info_handler(message: Message) -> None:
    await message.answer(text = responses.get('help'))