from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

from rup_bot.phrases import responses

async def make_keyboard_yes_or_no() -> InlineKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
        KeyboardButton(text = responses.get('answer_yes')),
        KeyboardButton(text = responses.get('answer_no')),
    ).as_markup(resize_keyboard = True)


async def make_keyboard_sign_up() -> InlineKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
        KeyboardButton(text = responses.get('sign_up'))
    ).as_markup(resize_keyboard = True)


async def make_keyboard_get_data_and_upload_data() -> InlineKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
    KeyboardButton(text = responses.get('get_data')),
        KeyboardButton(text = responses.get('upload_data'))
    ).as_markup(resize_keyboard=True)