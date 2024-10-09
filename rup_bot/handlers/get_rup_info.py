from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from rup_bot.phrases import responses

get_info_router = Router()

async def getRupInfo(message: Message) -> None:
    await message.answer(text = 'Бот отправил вам файл')


@get_info_router.message(Command('get'))
async def command_get_info_handler(message: Message) -> None:
    await getRupInfo(message)


@get_info_router.message(F.text == responses.get('get_info'))
async def content_type_get_info_handler(message: Message) -> None:
    await getRupInfo(message)