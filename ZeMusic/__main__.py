import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ZeMusic import LOGGER, app, userbot
from ZeMusic.core.call import Mody
from ZeMusic.misc import sudo
from ZeMusic.plugins import ALL_MODULES
from ZeMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ZeMusic.plugins" + all_module)
    LOGGER("ZeMusic.plugins").info("تنزيل معلومات السورس سورس ادمان...")
    await userbot.start()
    await Mody.start()
    try:
        await Mody.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ZeMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Mody.decorators()
    LOGGER("ZeMusic").info(
        "جاري تشغيل البوت\nتم التنصيب على سورس ادمان بنجاح\nقناة السورس https://t.me/TI_M_ll"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    await azkar()
    LOGGER("ZeMusic").info("Stopping Ze Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
