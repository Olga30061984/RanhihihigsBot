__all__ = [
    "commands_for_bot"
]

from aiogram import types

bot_commands = (
    ("help", "Справка по боту"),
    ("status", "Показывает статус пользователя"),
    ("register", "Регистрирует пользователя"),
)

commands_for_bot = []
for cmd, descr in bot_commands:
    commands_for_bot.append(types.BotCommand(command=cmd, description=descr))
