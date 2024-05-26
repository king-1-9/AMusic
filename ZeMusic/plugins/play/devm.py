import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
from config import OWNER_ID
import config

lnk = "https://t.me/" + config.CHANNEL_LINK

@app.on_message(filters.regex(r"^(المطور|مطور)$"))
async def devid(client: Client, message: Message):
    try:
        usr = await client.get_users(OWNER_ID)
        name = usr.first_name
        usrnam = usr.username
        photo_path = os.path.join("downloads", "developer.jpg")
        await app.download_media(usr.photo.big_file_id, file_name=photo_path)
        await message.reply_photo(
            photo=photo_path,
            caption=f"""<b>⌯ 𝙳𝚎𝚟 :</b> <a href='tg://user?id={OWNER_ID}'>{name}</a>\n\n<b>⌯ 𝚄𝚂𝙴𝚁 :</b> @{usrnam}""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(name, url=f"tg://user?id={OWNER_ID}"),
                    ],
                    [
                        InlineKeyboardButton(
                            text=config.CHANNEL_NAME, url=lnk),
                    ],
                ]
            ),
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        
