import io

from typing import Callable

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State

from rup_bot.phrases import responses
from rup_bot.reminder import make_reminder_markup
from rup_bot.utils.file_validator import validator_exel_files
from rup_bot.utils.file_validator import validator_pdf_files

from rup_bot.db.db_queries import upload_file_into_rup_files

upload_info_router = Router()


class Uploader(StatesGroup):
    waiting_file = State()


# хэндлер, если пользователь отправил файл
@upload_info_router.message(Uploader.waiting_file, F.document)
async def handle_file(message: Message, state: FSMContext) -> None:
    from rup_bot.__main__ import bot

    def validate_file(file: io.BytesIO, func: Callable[[io.BytesIO], bool]) -> bool:
        return func(file)

    async def download_file_from_tg(file_id: str) -> io.BytesIO:
        return await bot.download_file(
            (await bot.get_file(file_id)).file_path
        )
                
    match message.document.mime_type:
        case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            validated = validate_file(
                await download_file_from_tg(message.document.file_id),
                validator_exel_files
            )

            if not validated:
                await message.answer(text = responses.get('unsuccessful_upload'))
                return

        case 'application/pdf':
            validated = validate_file(
                await download_file_from_tg(message.document.file_id),
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
        await download_file_from_tg(message.document.file_id),
        message.from_user.id,
        message.document.file_id
    )

    await message.answer(
        text = responses.get('success_upload'),
        reply_markup = await make_reminder_markup()
    )

    await state.clear()


# хэндлер, если пользователь отправил не файл, а что то другое
@upload_info_router.message(Uploader.waiting_file)
async def handle_file_incorrectly(message: Message) -> None:
    await message.answer(text = responses.get('uploaded_other_format'))


async def setUploaderState(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('request_data'),
        reply_markup = ReplyKeyboardRemove()
    )
    await state.set_state(Uploader.waiting_file)


@upload_info_router.message(Command('upload'))
async def command_upload_data_handler(message: Message, state: FSMContext) -> None:
    await setUploaderState(message, state)


@upload_info_router.message(F.text == responses.get('upload_data'))
async def content_type_upload_data_handler(message: Message, state: FSMContext) -> None:
    await setUploaderState(message, state)