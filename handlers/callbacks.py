from aiogram.types import CallbackQuery
from db import async_session, User
from sqlalchemy import select, insert
#from handlers import register_message_handler, commands_for_bot

async def callback_continue(callback: CallbackQuery):
    """Ответ на кнопку продолжить"""

    async with async_session() as session:
        # Что-то проиходит
        await session.commit()
    await callback.message.answer("Успешно!")

async def callback_who(callback: CallbackQuery):
    """Ответ на кнопку преподаватель"""

    async with async_session() as session:
        # Что-то проиходит
        new_user = {
            'user_id': callback.from_user.id,
            'username': callback.from_user.username,
            'reg_date': callback.data,
            }
        insert_query = insert(User).values(**new_user)
        await session.execute(insert_query)
        await session.commit()
#        await message.answer(help_string)
#        logger.info(f"register new user {message.from_user.id}")

#        await session.commit()
    await callback.message.answer("Есть!")
