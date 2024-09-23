## Этап 2. Переменные окружения, логирование и маршрутизация

# Дополнительный гайд по aiogram3 https://mastergroosha.github.io/aiogram-3-guide/
# Документация по aiogram3 https://docs.aiogram.dev/en/latest/
# Ссылка на форум aiogram в тг: https://t.me/aiogram

# 0. Установить зависимости
# pip install aiogram
# pip install python-dotenv

# TODOs-list
# OK - настроить переменные окружения
# TODO - добавить логирование (используя ветки)
# TODO - сделать маршрутизацию вместо декораторов

# 1. Импорт
import logging  # чтобы отследить состояние бота, используем логи
import asyncio  # асинхронный ввод-вывод
from aiogram import Bot, Dispatcher, types, filters  # класс бота и диспетчера
from config import TOKEN


# 3. Установить общий уровень логирования и создали экземпляр лога
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# 3. Экзампляры бота и диспетчера
bot = Bot(TOKEN)
dp = Dispatcher()

# Все обработчики должны быть подключены к маршрутизатору (или диспетчеру)
# Обработчики (handlers) — обработчик сообщений, который будет возвращать другое сообщение, указанное в функции


# 4. Создание обработчиков
# -- Обработчики (handler) --
@dp.message(filters.CommandStart())  # декоратора диспетчера
async def command_start_handler(message: types.Message) -> None:
    """команда /start"""
    # await message.answer("Hello!")
    await message.answer(f"Hello, {message.from_user.username}!")
    logger.info(f"user {message.from_user.id} starts bot!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """эхо-ответ"""
    await message.send_copy(chat_id=message.chat.id)
    logger.info(f"user {message.from_user.id} send text and get echo!")


# -- Вспомогательная функция (utils) --
async def main() -> None:
    """polling-запуск проекта"""

    # polling-запуск
    await dp.start_polling(bot)


# 5. Запуск
if __name__ == "__main__":
    asyncio.run(main())
