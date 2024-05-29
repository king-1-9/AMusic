import asyncio
from ZeMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

italy = ["لبيه يا {nameuser}",
         "ءامر يا {nameuser}",
         "بوت بحلقك",
         "شفيك",
         "شتبي مني",
         "زعلان",
         "مريض"]

@app.on_message(filters.text & filters.regex(r"(^|\W)بوت(\W|$)"))
async def Italymusic(client, message):
    if "بوت" in message.text:
        response = random.choice(italy)
        response = response.format(nameuser=message.from_user.first_name)
        await message.reply(response)
