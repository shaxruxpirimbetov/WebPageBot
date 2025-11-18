from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import buttons as btn
import config as conf
import database as db
import funcs as fnc
import os

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi", reply_markup=btn.menu)
    print(db.create_user(message.from_user))


@router.message(F.text == "Deploy Site")
async def deploy_site_func(message: Message):
    await message.answer("Send ")


@router.message(F.text == "My sites")
async def my_sites_func(message: Message):
    await message.reply("Wait...")


@router.message(F.document)
async def get_doc_func(message: Message):
    file = message.document
    print(file)
    file_path = await conf.bot.get_file(file.file_id)
    download_path = f"downloads/{file.file_id}.html"
    await conf.bot.download_file(file_path.file_path, download_path)

    with open(download_path, "r") as f:
        text = f.read()
        fnc.deploy_site(title="First", html=text, user_id=message.from_user.id)

    os.remove(download_path)