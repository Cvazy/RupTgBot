import io

from typing import Callable

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State

from rup_bot.phrases import responses
from rup_bot.utils.file_validator import validator_exel_files
from rup_bot.utils.file_validator import validator_pdf_files
from rup_bot.utils.keyboard_builder import make_keyboard_get_data_and_upload_data
from rup_bot.db.db_queries import check_user_into_students, \
    upload_file_into_rup_files

upload_info_router = Router()


class Uploader(StatesGroup):
    waiting_file = State()


def validate_file(file: io.BytesIO, func: Callable[[io.BytesIO], bool]) -> bool:
    return func(file)


async def download_file_from_tg(bot, file_id: str) -> io.BytesIO:
    return await bot.download_file(
        (await bot.get_file(file_id)).file_path
    )


@upload_info_router.message(Uploader.waiting_file, F.document)
async def handle_file(message: Message, state: FSMContext) -> None:
    from rup_bot.__main__ import bot

    match message.document.mime_type:
        case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            validated = validate_file(
                await download_file_from_tg(bot, message.document.file_id),
                validator_exel_files
            )

            if not validated:
                await message.answer(text = responses.get('unsuccessful_upload'))
                return

        case 'application/pdf':
            validated = validate_file(
                await download_file_from_tg(bot, message.document.file_id),
                validator_pdf_files
            )

            if not validated:
                await message.answer(text = responses.get('unsuccessful_upload'))
                return

        case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            pass

        case _:
            await message.answer(text = responses.get('uploaded_other_format'))
            return

    await state.update_data(file = message.document)

    upload_file_into_rup_files(
        (await state.get_data()).get('file'),
        await download_file_from_tg(bot, message.document.file_id),
        message.from_user.id,
        message.document.file_id
    )

    await message.answer(
        text = responses.get('success_upload'),
        reply_markup = await make_keyboard_get_data_and_upload_data()
    )

    await state.clear()


@upload_info_router.message(Uploader.waiting_file, F.photo)
async def handle_photo(message: Message, state: FSMContext) -> None:
    from rup_bot.__main__ import bot

    class File:
        file_name = f'{message.photo[-1].file_unique_id}_img.png'

    await state.update_data(file = message.photo)

    upload_file_into_rup_files(
        File,
        await download_file_from_tg(bot, message.photo[-1].file_id),
        message.from_user.id,
        message.photo[-1].file_id
    )

    await message.answer(
        text = responses.get('success_upload'),
        reply_markup = await make_keyboard_get_data_and_upload_data()
    )

    await state.clear()


@upload_info_router.message(Uploader.waiting_file, ~F.text.startswith('/'))
async def handle_file_incorrectly(message: Message) -> None:
    await message.answer(text = responses.get('uploaded_other_format'))


@upload_info_router.message(Command('upload'))
@upload_info_router.message(F.text == responses.get('upload_data'))
async def command_upload_data_handler(message: Message, state: FSMContext) -> None:
    if len(check_user_into_students(tg_id = message.from_user.id)) == 0:
        await message.answer(text = responses.get('pass_auth'))
        return

    await message.answer(
        text = responses.get('request_data'),
        reply_markup = ReplyKeyboardRemove()
    )
    await state.set_state(Uploader.waiting_file)
