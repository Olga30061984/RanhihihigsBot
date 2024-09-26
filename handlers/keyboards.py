from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_continue = InlineKeyboardButton(
    text="Далле",
    callback_data="continue_button_pressed"
)

keyboard_continue = InlineKeyboardMarkup(inline_keyboard=[[button_continue]])
