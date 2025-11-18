from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import buttons as btn
import config as conf
import os

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi", reply_markup=btn.menu)


@router.message(F.text == "Deploy Site")
async def deploy_site_func(message: Message):
    await message.answer("Send ")


@router.message(F.document)
async def get_doc_func(message: Message):
    file = message.document
    file_path = await conf.bot.get_file(file.file_id)
    download_path = f"downloads/{file.file_id}.html"
    await conf.bot.download_file(file_path.file_path, download_path)
    await message.answer("OK")
    os.remove(download_path)