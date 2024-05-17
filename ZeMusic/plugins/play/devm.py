import asyncio
import os
import aiofiles
import requests
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID
import config

lnk = "https://t.me/" + config.CHANNEL_LINK

@app.on_message(command(["مطور", "المطور"]))
async def devid(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    uid = OWNER_ID

    photo_id = usr.photo.big_file_id
    photo_path = os.path.join("downloads", "developer.jpg")

    # Download photo asynchronously
    await app.download_media(photo_id, file_name=photo_path)

    # Reply to the message with the photo
    await message.reply_photo(
        photo=photo_path,
        caption=f"""<b>⌯ 𝙳𝚎𝚟 :</b> <a href= tg://user?id={uid} >{name}</a>\n\n<b>⌯ 𝚄𝚂𝙴𝚁 :</b> @{usrnam}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(name, url=f"tg://user?id={uid}")],
                [InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)],
            ]
        ),
    )

    # Optionally, remove the downloaded photo after sending it
    if os.path.exists(photo_path):
        os.remove(photo_path)
