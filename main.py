from aiogram import Bot, Dispatcher
import config as conf
import asyncio

bot = Bot(token=conf.TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())