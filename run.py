import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.bot.handlers import start_handler, scan_handler
from app.config import BOT_TOKEN

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

dp.message.register(start_handler, lambda msg: msg.text == "/start")
dp.message.register(scan_handler)


async def main():
    print("🚀 Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Bot stopped")