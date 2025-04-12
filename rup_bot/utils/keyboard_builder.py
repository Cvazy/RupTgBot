from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

from rup_bot.phrases import responses
from rup_bot.db.db_queries import get_list_faculties

async def make_keyboard_yes_or_no() -> ReplyKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
        KeyboardButton(text = responses.get('answer_yes')),
        KeyboardButton(text = responses.get('answer_no')),
    ).as_markup(resize_keyboard = True)


async def make_keyboard_sign_up() -> ReplyKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
        KeyboardButton(text = responses.get('sign_up'))
    ).as_markup(resize_keyboard = True)


async def make_keyboard_get_data_and_upload_data() -> ReplyKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
    KeyboardButton(text = responses.get('get_data')),
        KeyboardButton(text = responses.get('upload_data'))
    ).as_markup(resize_keyboard = True)


async def make_keyboard_list_faculties() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    for item in get_list_faculties():
        builder.button(text = item.get('name'))

    return builder.adjust(1).as_markup(resize_keyboard = True)


async def make_keyboard_send_phone_number() -> ReplyKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
        KeyboardButton(text = responses.get('fsm_input_phone'), request_contact = True)
    ).as_markup(resize_keyboard = True)