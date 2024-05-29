import asyncio
from ZeMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_NAME

italy = ["لبيه يا {nameuser}",
         "اسمي {BOT_NAME} 😒.",
         "بوت بحلقك",
         "شفيك",
         "شتبي مني",
         "زعلان",
         "{BOT_NAME} يلعنك يا {nameuser}",
         "ايش 😒",
         "يارب يكون شي مهم 🙄",
         "حوت يكلك"]

@app.on_message(filters.text & filters.regex(r"(^|\W)بوت(\W|$)"))
async def Italymusic(client, message):
    if "بوت" in message.text:
        response = random.choice(italy)
        response = response.format(nameuser=message.from_user.first_name, BOT_NAME=BOT_NAME)
        await message.reply(response)
