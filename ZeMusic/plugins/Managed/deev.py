import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint
                
@app.on_message(filters.regex(r"^(.)$"))
async def huhh(client: Client, message: Message):
    dev_id = 5145609515
    dev = await client.get_users(dev_id)
    name = dev.first_name
    
    await message.reply_photo(
        caption=f"""<b>Dev ↠ <a href='tg://user?id={dev_id}'>{name}</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙺𝙸𝙽𝙶", url=f"https://t.me/EF_19"),
                ],
            ]
        ),
    )
