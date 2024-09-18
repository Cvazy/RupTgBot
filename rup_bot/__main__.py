import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from rup_bot.core import consts
from rup_bot.core.logger import logger
from rup_bot.handlers.echo import echo_router
from rup_bot.handlers.start import start_router

ROUTERS = (
    start_router,
    echo_router,
)


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(*ROUTERS)
    bot = Bot(
        token=consts.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception:
        import traceback

        logger.error(traceback.format_exc())
