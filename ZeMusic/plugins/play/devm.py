import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID
import config

lnk= "https://t.me/" +config.CHANNEL_LINK
@app.on_message(command(["مطور", "المطور"]))
async def devid(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
       
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>⌯ 𝙳𝚎𝚟 :</b> <a href= tg://user?id={OWNER_ID} >{name}</a>\n\n<b>⌯ 𝚄𝚂𝙴𝚁 :</b> @{usrnam}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(name, url=f"tg://user?id={uid}"),
                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk),
                ],
            ]
        ),
    )
