from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="My Sites")],
],
    resize_keyboard=True,
    input_field_placeholder="Menu..."
)