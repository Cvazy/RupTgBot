import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties

from rup_bot.core import consts
from rup_bot.core.logger import logger

from rup_bot.handlers.start import start_router
from rup_bot.handlers.get_rup_info import get_info_router
from rup_bot.handlers.upload_rup_info import upload_info_router
from rup_bot.handlers.help import help_router
from rup_bot.handlers.exception import exception_router


ROUTERS = (
    start_router,
    get_info_router,
    upload_info_router,
    help_router,
    exception_router,
)


bot_commands = [
    BotCommand(command = '/start', description = 'Запустить бота'),
    BotCommand(command = '/get', description = 'Получить информацию'),
    BotCommand(command = '/upload', description = 'Загрузить информацию'),
    BotCommand(command = '/help', description = 'Помощь')
]


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(*ROUTERS)

    bot = Bot(
        token = consts.TELEGRAM_BOT_TOKEN,
        default = DefaultBotProperties(parse_mode = ParseMode.HTML)
    )

    await bot.set_my_commands(bot_commands)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception:
        import traceback

        logger.error(traceback.format_exc())
