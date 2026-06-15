import asyncio

from aiogram import Bot, Dispatcher

from app.core.config import BOT_TOKEN
from app.bot.handlers.start import router as start_router
from app.bot.handlers.youtube import router as youtube_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(youtube_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())