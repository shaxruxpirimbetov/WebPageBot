from aiogram import Bot, Dispatcher
import config as conf
import asyncio, handlers

async def main():
    await conf.bot.send_message(chat_id=6181120570, text="I`m here")
    await conf.dp.start_polling(conf.bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Done with {e}")