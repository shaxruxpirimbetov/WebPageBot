from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Deploy Site")],
],
    resize_keyboard=True,
    input_field_placeholder="Menu..."
)