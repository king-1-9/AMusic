import asyncio
from ZeMusic import app 
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_NAME

italy = [
         "لبيه وش اغني لك",
         "قول {BOT_NAME} غنيلي",
         "اصعد مكالمه",
         "لا تشغلني انا في المكالمه",
         "فاضي اصعد نتونس",
         "مو عاجبك {BOT_NAME}؟",
         "اروح قروب ثاني؟"
         ]

@app.on_message(filters.regex(r"^(بوت)$"))
async def Italymusic(client, message):
    if "بوت" in message.text:
        response = random.choice(italy)
        response = response.format(nameuser=message.from_user.first_name, BOT_NAME=BOT_NAME)
        await message.reply(response)
