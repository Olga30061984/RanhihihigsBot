# -- Обработчики (handlers) --
# Все обработчики должны быть подключены к маршрутизатору (или диспетчеру)
# Обработчики (handlers) — обработчик сообщений, который будет возвращать другое сообщение, указанное в функции

__all__ = [
    "register_message_handler"
]

# Установить общий уровень логирования и создали экземпляр лога
import logging
from aiogram import Router, types, filters, F
from db import async_session, User
from sqlalchemy import select, insert
from .keyboards import keyboard_continue
from .callbacks import callback_continue


# справочная информация
help_string = """
Вас приветствует бот YaDiskBot!
ℹ️ Вы можете вывести справочную информацию по боту — /help
👨🏻‍🦱 Узнать статус пользователя — /status
"""

# настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def command_start_handler(message: types.Message) -> None:
    """Команда регистрации и справки /start, /help"""

    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        user_exists = await session.execute(query)

        if user_exists.scalars().all():
            await message.answer(help_string)
        else:
            new_user = {
                'user_id': message.from_user.id,
                'username': message.from_user.username,
            }
            insert_query = insert(User).values(**new_user)
            await session.execute(insert_query)
            await session.commit()
            await message.answer(help_string)
            logger.info(f"register new user {message.from_user.id}")


async def command_status_handler(message: types.Message) -> None:
    """Команда информации о пользователе /status"""

    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        result = await session.execute(query)
        user = result.scalar()
        info = (f"<b>UserId</b>: <i>{user.user_id}</i>\n"
                f"<b>UserName</b>: <i>{user.username}</i>)\n"
                f"<b>Registration Date</b>: <i>{user.reg_date}</i>")
        await message.answer(info, parse_mode="HTML")
        logger.info(f"user {message.from_user.id} asks for status!")

    await message.reply("Хотите продолжить?", reply_markup=keyboard_continue)


async def process_unknown_command(message: types.Message) -> None:
    """эхо-ответ"""
    await message.reply(text="Неподдерживаемая команда. Введите /help для справки.")
    logger.info(f"user {message.from_user.id} send unknown message or command!")


async def register_message_handler(router: Router):
    """Маршрутизация"""
    router.message.register(command_start_handler, filters.Command(commands=["help", "start"]))
    router.message.register(command_status_handler, filters.Command(commands=["status"]))
    router.callback_query.register(callback_continue, F.data.startswith("continue_"))
    router.message.register(process_unknown_command)