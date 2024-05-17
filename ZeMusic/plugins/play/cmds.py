import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID, START_IMG_URL
import config
Lnk= "https://t.me/" +config.CHANNEL_LINK

@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=START_IMG_URL,
        caption=f"""<b>» مرحبـاً بك عـزيـزي </b> {message.from_user.mention} .\n\n<b>» استخـدم الازرار بالاسفـل 𝄞\n» لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامـر القنـاة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=Lnk),
                ],
            ]
        ),
    )
