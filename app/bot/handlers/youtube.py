from aiogram import Router
from aiogram.types import Message
from app.services.youtube_service import get_video_title
from app.services.summary_service import summarize
from app.services.transcript_service import (
    extract_video_id,
    get_transcript
)

router = Router()


@router.message()
async def youtube_link(message: Message):
    text = message.text

    if "youtube.com" not in text and "youtu.be" not in text:
        return

    try:
        status = await message.answer(
            "📖 Получаю субтитры..."
        )

        video_id = extract_video_id(text)

        transcript = get_transcript(video_id)

        await status.edit_text(
            "🤖 Делаю конспект..."
        )

        summary = summarize(transcript)
    
        if len(summary) > 4000:
            summary = summary[:4000] + "\n\n..."
            

        await status.edit_text(summary)

    except Exception as e:
            print(e)

            await status.edit_text(
                 "❌ Для этого видео не удалось получить субтитры.\n\n"
                "Попробуйте другое видео."
        )