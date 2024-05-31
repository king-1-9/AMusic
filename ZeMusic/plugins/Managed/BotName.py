import re
import asyncio
from ZeMusic import app 
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_NAME

Nb = BOT_NAME

italy = [
         "لبيه وش اغني لك",
         "قول {BOT_NAME} غنيلي",
         "{nameuser} اصعد مكالمه",
         "لا تشغلني اصعد مكالمه",
         "قول {BOT_NAME} شغل احبك",
         "قول {BOT_NAME} ابحث احبك",
         "اغني في قروب ثاني 🦦.",
         "عيون {BOT_NAME} ايش تحب تسمع",
         "ادري عاجبك اسمي ❤️",
         "يارب يكون شي مهم"
         ]

@app.on_message(filters.regex(r"^(" + re.escape(Nb) + r")$"))

async def Italymusic(client, message):
    if Nb in message.text:
        response = random.choice(italy)
        response = response.format(nameuser=message.from_user.first_name, BOT_NAME=BOT_NAME)
        await message.reply(response)
