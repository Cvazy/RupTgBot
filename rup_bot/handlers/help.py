from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from rup_bot.phrases import responses, contact_info
from rup_bot.db.db_queries import check_user_into_students, \
    get_list_faculties

help_router = Router()

@help_router.message(Command('help'))
async def command_upload_info_handler(message: Message) -> None:
    get_user = check_user_into_students(message.from_user.id)

    if len(get_user) != 0:
        faculty = get_list_faculties(param = get_user[0].get('faculty'))
        await message.answer(
            text = f"{responses.get('help')}\n\n{responses.get('contact_info_by_faculty')}\n\n{contact_info.get(faculty.get('name'))}"
        )
    else:
        await message.answer(text = f"{responses.get('help')}")