## Этап 1. Начало работы с aiogram3

# Дополнительный гайд по aiogram3 https://mastergroosha.github.io/aiogram-3-guide/
# Документация по aiogram3 https://docs.aiogram.dev/en/latest/
# Ссылка на форум aiogram в тг: https://t.me/aiogram

# 0. Установить зависимости
# pip install aiogram
# pip install python-dotenv

# 1. Импорт
import asyncio  # асинхронный ввод-вывод
from aiogram import Bot, Dispatcher, types, filters  # класс бота и диспетчера
from config import TOKEN

# 2. Экзампляры бота и диспетчера
bot = Bot(TOKEN)
dp = Dispatcher()

# Все обработчики должны быть подключены к маршрутизатору (или диспетчеру)
# Обработчики (handlers) — обработчик сообщений, который будет возвращать другое сообщение, указанное в функции


# 3. Создание обработчиков
# -- Обработчики (handler) --
@dp.message(filters.CommandStart())  # декоратора диспетчера
async def command_start_handler(message: types.Message) -> None:
    """команда /start"""
    # await message.answer("Hello!")
    await message.answer(f"Hello, {message.from_user.username}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """эхо-ответ"""
    await message.send_copy(chat_id=message.chat.id)


# -- Вспомогательная функция (utils) --
async def main() -> None:
    """polling-запуск проекта"""
    await dp.start_polling(bot)


# 4. Запуск
if __name__ == "__main__":
    asyncio.run(main())
