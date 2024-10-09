from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from rup_bot.phrases import responses

upload_info_router = Router()

async def uploadRupInfo(message: Message) -> None:
    await message.answer(text = 'Вы успешно загрузили файл')


@upload_info_router.message(Command('upload'))
async def command_upload_info_handler(message: Message) -> None:
    await uploadRupInfo(message)


@upload_info_router.message(F.text == responses.get('upload_info'))
async def content_type_upload_info_handler(message: Message) -> None:
    await uploadRupInfo(message)