"""
import asyncio
from ZeMusic import app 
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_NAME

italy = ["لبيه يا {nameuser}",
         "سم يا {nameuser}",
         "مين مزعلك يعيوني 🥺",
         "قلبي ودقاته وكل حياته 🥺",
         "شتبي مني",
         "ادري عاجبك اسمي",
         "عيون {BOT_NAME}",
         "يالبى اسمي من فمك ❤️‍🔥.",
         "يارب يكون شي مهم",
         "عيوني تحولت قلوب 🥺❤️.",
         "مو فاضي",
         "روح {BOT_NAME} ❤️",
         "قلب {BOT_NAME} 🫀"
         ]

@app.on_message(filters.text & filters.regex(rf"(^|\W){BOT_NAME}(\W|$)"))
async def Italymusic(client, message):
    if BOT_NAME in message.text:
        response = random.choice(italy)
        response = response.format(nameuser=message.from_user.first_name, BOT_NAME=BOT_NAME)
        await message.reply(response)
        """
