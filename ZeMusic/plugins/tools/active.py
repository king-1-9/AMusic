# \activevc معرفه المكالمات المشغله حاليا
from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from ZeMusic import app
from ZeMusic.misc import SUDOERS
from ZeMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice", "الاتصالات","المكالمات"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» جاري البحث عن مكالمات ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» لاتوجد اتصالات الان.\n  {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» الأتصالات النشطة حاليا :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo", "الفيديوهات"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» جاري البحث عن فيديوهات متوفرة ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» لاتوجد فيديوهات الان.\n  {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» الفيديوهات النشطة حاليا :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
