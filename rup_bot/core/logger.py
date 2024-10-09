import logging

from rup_bot.core.enums import LoggerName

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(LoggerName.bot)
