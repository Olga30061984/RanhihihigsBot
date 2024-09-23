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
from handlers import register_message_handler


async def main() -> None:
    """polling-запуск проекта"""

    # Установить общий уровень логирования
    logging.basicConfig(level=logging.DEBUG)

    # Экзампляры бота и диспетчера
    bot = Bot(TOKEN)
    dp = Dispatcher()

    # Функция для вызова обработчиков
    await register_message_handler(dp)

    # polling-запуск
    await dp.start_polling(bot)


# 5. Запуск
if __name__ == "__main__":
    asyncio.run(main())
