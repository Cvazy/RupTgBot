from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from rup_bot.db.db_queries import get_file_from_rup_files

from rup_bot.phrases import responses

get_info_router = Router()


async def getRupData(message: Message) -> None:
    files_list = get_file_from_rup_files(message.from_user.id)

    for item in files_list:

        # !!! DELETE CONDITION item.get('tg_file_id') != '1170461380' AFTER CLEAN TABLE rup_files

        if item.get('tg_file_id') is not None and item.get('tg_file_id') != '1170461380':
            await message.answer_document(item.get('tg_file_id'))


@get_info_router.message(Command('get'))
async def command_get_data_handler(message: Message) -> None:
    await getRupData(message)


@get_info_router.message(F.text == responses.get('get_data'))
async def content_type_get_data_handler(message: Message) -> None:
    await getRupData(message)