from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from rup_bot.phrases import responses
from rup_bot.db.db_queries import check_user_into_students, \
    get_file_from_rup_files

get_info_router = Router()


@get_info_router.message(Command('get'))
@get_info_router.message(F.text == responses.get('get_data'))
async def command_get_data_handler(message: Message) -> None:
    if len(check_user_into_students(tg_id = message.from_user.id)) == 0:
        await message.answer(text = responses.get('pass_auth'))
        return

    files_list = get_file_from_rup_files(message.from_user.id)

    if len(files_list) == 0:
        await message.answer(text=responses.get('rup_file_not_found'))
        return

    for item in files_list:
        if item.get('tg_file_id') is not None:
            await message.answer_document(item.get('tg_file_id'))
