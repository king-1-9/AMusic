from pyrogram import filters
from pyrogram.types import Message

from ZeMusic import app
from ZeMusic.core.call import Mody
from ZeMusic.utils.database import set_loop
from ZeMusic.utils.decorators import AdminRightsCheck
from ZeMusic.utils.inline import close_markup
from config import BANNED_USERS
from strings.filters import command
from strings import get_string
#import config

#Nem = config.BOT_NAME + " اسكت"
#Men = config.BOT_NAME + " ايقاف"
@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS
)
@app.on_message(
    command(["اسكت","ايقاف"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Mody.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format((message.from_user.mention if message.from_user else message.chat.title)), reply_markup=close_markup(_)
    )



@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.channel & ~BANNED_USERS
)
@app.on_message(
    command(["اسكت","ايقاف"]) & filters.channel & ~BANNED_USERS
)
async def stop_music(cli, message: Message):
    try:
        await message.delete()
    except:
        pass

    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    if message.command[0][0] == "c":
        chat_id = await get_cmode(message.chat.id)
        if chat_id is None:
            return await message.reply_text(_["setting_7"])
        try:
            await app.get_chat(chat_id)
        except:
            return await message.reply_text(_["cplay_4"])
    else:
        chat_id = message.chat.id
    if not len(message.command) == 1:
        return
    await Mody.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format((message.from_user.mention if message.from_user else message.chat.title)), reply_markup=close_markup(_)
    )
