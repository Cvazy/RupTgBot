from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State

from rup_bot.phrases import responses
from rup_bot.handlers.reminder import make_reminder_markup

upload_info_router = Router()


class Uploader(StatesGroup):
    waiting_file = State()


# хэндлер, если пользователь отправил файл
@upload_info_router.message(Uploader.waiting_file, F.document)
async def handle_file(message: Message, state: FSMContext) -> None:
    await state.update_data(file = message.document)

    await message.answer(
        text = responses.get('success_upload'),
        reply_markup = await make_reminder_markup()
    )

    # вывод объекта загруженного файла
    print(await state.get_data())

    await state.clear()


# хэндлер, если пользователь отправил не файл, а что то другое
@upload_info_router.message(Uploader.waiting_file)
async def handle_file_incorrectly(message: Message, state: FSMContext) -> None:
    await message.answer(text = responses.get('unsuccessful_upload'))


async def setUploaderState(message: Message, state: FSMContext) -> None:
    await message.answer(text = responses.get('request_data'))
    await state.set_state(Uploader.waiting_file)


@upload_info_router.message(Command('upload'))
async def command_upload_data_handler(message: Message, state: FSMContext) -> None:
    await setUploaderState(message, state)


@upload_info_router.message(F.text == responses.get('upload_data'))
async def content_type_upload_data_handler(message: Message, state: FSMContext) -> None:
    await setUploaderState(message, state)