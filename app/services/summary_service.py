from google import genai

from app.core.config import GEMINI_API_KEY



client = genai.Client(api_key=GEMINI_API_KEY)


def summarize(text: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
Сделай краткий конспект этого видео.

Верни:

1. Основная тема
2. Ключевые идеи
3. Практические выводы

Текст:

{text[:30000]}
"""
    )

    return response.text