from aiogram import Bot, Dispatcher
import handlers

TOKEN="8158445939:AAHmoesq6Em6F5QdxcNhRJYSVL2pTLpUyn0"
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(handlers.router)