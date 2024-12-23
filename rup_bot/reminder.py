from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from rup_bot.phrases import responses


async def make_reminder_markup() -> ReplyKeyboardMarkup:
    return ReplyKeyboardBuilder().row(
        KeyboardButton(text = responses.get('set_reminder')),
        KeyboardButton(text = responses.get('unset_reminder')),
    ).as_markup(resize_keyboard = True)
