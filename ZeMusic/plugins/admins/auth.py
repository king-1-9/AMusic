from pyrogram import filters
from pyrogram.types import Message

from ZeMusic import app
from ZeMusic.utils import extract_user, int_to_alpha
from ZeMusic.utils.database import (
    delete_authuser,
    get_authuser,
    get_authuser_names,
    save_authuser,
)
from ZeMusic.utils.decorators import AdminActual, language
from ZeMusic.utils.inline import close_markup
from config import BANNED_USERS, adminlist


@app.on_message(filters.command(("رفع ادمن"),"") & filters.group & ~BANNED_USERS)
@AdminActual
async def auth(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
        user = message.text.split(None, 2)[2]
        if "@" in user:
            user = user.replace("@", "")
        else:
            return await message.reply_text(_["general_1"])
        
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = len(_check)
        if int(count) == 50:
            return await message.reply_text(_["auth_1"])
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            get = adminlist.get(message.chat.id)
            if get:
                if user.id not in get:
                    get.append(user.id)
            await save_authuser(message.chat.id, token, assis)
            return await message.reply_text(_["auth_2"].format(user.mention))
        else:
            await message.reply_text(_["auth_3"].format(user.mention))
        return

    user = await extract_user(message)
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 50:
        return await message.reply_text(_["auth_1"])
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        get = adminlist.get(message.chat.id)
        if get:
            if user_id not in get:
                get.append(user_id)
        await save_authuser(message.chat.id, token, assis)
        return await message.reply_text(_["auth_2"].format(user.mention))
    else:
        await message.reply_text(_["auth_3"].format(user.mention))

                                                           
@app.on_message(filters.command(["تنزيل ادمن"],"") & filters.group & ~BANNED_USERS)
@AdminActual
async def unauthusers(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
        user = message.text.split(None, 2)[2]
        if "@" in user:
            user = user.replace("@", "")
        else:
            return await message.reply_text(_["general_1"])
            
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        get = adminlist.get(message.chat.id)
        if get:
            if user.id in get:
                get.remove(user.id)
        if deleted:
            return await message.reply_text(_["auth_4"].format(user.mention))
        else:
            return await message.reply_text(_["auth_5"].format(user.mention))

    user = await extract_user(message)
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    get = adminlist.get(message.chat.id)
    if get:
        if user_id in get:
            get.remove(user_id)
    if deleted:
        return await message.reply_text(_["auth_4"].format(user.mention))
    else:
        return await message.reply_text(_["auth_5"].format(user.mention))


@app.on_message(
    filters.command(["الادمنيه", "الادمن"]) & filters.group & ~BANNED_USERS
)
@language
async def authusers(client, message: Message, _):
    _wtf = await get_authuser_names(message.chat.id)
    if not _wtf:
        return await message.reply_text(_["setting_4"])
    else:
        j = 0
        mystic = await message.reply_text(_["auth_6"])
        text = _["auth_7"].format(message.chat.title)
        for umm in _wtf:
            _umm = await get_authuser(message.chat.id, umm)
            user_id = _umm["auth_user_id"]
            admin_id = _umm["admin_id"]
            admin_name = _umm["admin_name"]
            try:
                user = (await app.get_users(user_id)).first_name
                j += 1
            except:
                continue
            text += f"{j} - {user}\n"
            text += f"   {_['auth_8']}\n {admin_name}\n\n"
        await mystic.edit_text(text, reply_markup=close_markup(_))
