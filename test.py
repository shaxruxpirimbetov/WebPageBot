from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio

bot = Bot(token="8158445939:AAHmoesq6Em6F5QdxcNhRJYSVL2pTLpUyn0")
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
	await message.reply("Hi!")


@dp.message(F.text == "/start")
async def cmd_start2(message: Message):
	await message.reply("Hi!")


async def main():
	await bot.send_message(chat_id=6181120570, text="I'm here!!")
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())