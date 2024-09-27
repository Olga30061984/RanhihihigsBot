from aiogram.types import CallbackQuery
from db import async_session

async def callback_continue(callback: CallbackQuery):
    """Ответ на кнопку продолжить"""

    async with async_session() as session:
        # Что-то проиходит
        await session.commit()
    await callback.message.answer("Успешно!")
