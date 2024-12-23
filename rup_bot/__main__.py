import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties

from core import consts
from core.logger import logger

from handlers.start import start_router
from handlers.get_rup_data import get_info_router
from handlers.upload_rup_data import upload_info_router
from handlers.help import help_router
from handlers.exception import exception_router
from rup_bot.fsm.fsm_init_user import fsm_init_user_router

ROUTERS = (
    start_router,
    get_info_router,
    upload_info_router,
    help_router,
    fsm_init_user_router,
    exception_router
)


bot_commands = [
    BotCommand(command = '/start', description = 'Запустить бота'),
    BotCommand(command = '/get', description = 'Получить информацию'),
    BotCommand(command = '/upload', description = 'Загрузить информацию'),
    BotCommand(command = '/reminder', description = 'Установить напоминание'),
    BotCommand(command = '/help', description = 'Помощь')
]


bot = Bot(
    token = consts.TELEGRAM_BOT_TOKEN,
    default = DefaultBotProperties(parse_mode = ParseMode.HTML)
)


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(*ROUTERS)

    await bot.set_my_commands(bot_commands)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception:
        import traceback

        logger.error(traceback.format_exc())
