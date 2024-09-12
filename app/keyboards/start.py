from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

# fmt: off
START_KEYBOARD = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="0-10"),
                KeyboardButton(text="10-18"),
                KeyboardButton(text="18-30"),
                KeyboardButton(text="30-50"),
                KeyboardButton(text="50 and older"),
            ]
        ],
        resize_keyboard=True,
    )
# fmt: on
