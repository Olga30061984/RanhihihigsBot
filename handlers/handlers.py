# -- Обработчики (handlers) --
# Все обработчики должны быть подключены к маршрутизатору (или диспетчеру)
# Обработчики (handlers) — обработчик сообщений, который будет возвращать другое сообщение, указанное в функции


# Установить общий уровень логирования и создали экземпляр лога
import logging
from aiogram import Router, types, filters


# настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def command_start_handler(message: types.Message) -> None:
    """Команда /start"""
    await message.answer(f"Hello, {message.from_user.username}!")
    logger.info(f"user {message.from_user.id} starts bot!")


# async def echo_handler(message: types.Message) -> None:
#     """эхо-ответ"""
#     await message.send_copy(chat_id=message.chat.id)
#     logger.info(f"user {message.from_user.id} send text and get echo!")


async def register_message_handler(router: Router):
    """Маршрутизация"""
    router.message.register(command_start_handler, filters.CommandStart())