from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Логисты"),
        ],
        [
            KeyboardButton(text="Менеджеры"),
        ],
        [
            KeyboardButton(text="Операторы"),
        ]
    ],
    resize_keyboard=True
)
