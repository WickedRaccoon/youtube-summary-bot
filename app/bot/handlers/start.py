from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! 👋 Отправь ссылку на YouTube, и я сделаю конспект видео."
    )