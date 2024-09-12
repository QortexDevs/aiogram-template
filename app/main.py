import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from core import settings
from handlers import commons

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Starting bot")

    default_bot_properties: DefaultBotProperties = DefaultBotProperties(
        parse_mode="HTML"
    )
    bot: Bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, default=default_bot_properties)
    logger.info(f"settings.REDIS_URL: {settings.REDIS_URL}")
    dp: Dispatcher = Dispatcher(storage=RedisStorage.from_url(settings.REDIS_URL))

    dp.include_router(commons.router)

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
