from aiogram import Bot, Dispatcher
import config as conf
import asyncio, handlers

bot = Bot(token=conf.TOKEN)
dp = Dispatcher()
dp.include_router(handlers.router)

async def main():
    await bot.send_message(chat_id=6181120570, text="I`m here")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Done with {e}")