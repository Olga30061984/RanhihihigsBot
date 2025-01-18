from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_continue = InlineKeyboardButton(
    text="Далее",
    callback_data="continue_button_pressed"
)

keyboard_continue = InlineKeyboardMarkup(inline_keyboard=[[button_continue]])

button_p = InlineKeyboardButton(
    text="Преподаватель",
    callback_data="who_button_pressed"
)

button_s = InlineKeyboardButton(
    text="Cтудент",
    callback_data="who_button_pressed"
)

keyboard_who = InlineKeyboardMarkup(inline_keyboard=[[button_p,button_s]])
