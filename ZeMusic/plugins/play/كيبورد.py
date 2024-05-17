import asyncio
from pyrogram import Client, filters
from strings.filters import command
from ZeMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "<b>- اهلا بك عزيزي اليك قائمه الاوامر</b>"




REPLY_MESSAGE_BUTTONS = [

          [

             ("‹ غنيلي ›"),

             ("‹ تلغراف ›")

          ],

          [

             ("‹ صور ›"),

             ("‹ انمي ›")

          ],

          [

             ("‹ متحركه ›"),

             ("‹ اقتباسات ›")

          ],

          [

             ("‹ افتارات شباب ›"),

             ("‹ افتار بنات ›")

          ],

          [

             ("‹ هيدرات ›"),

             ("‹ قران ›")

          ],
    
          [

             ("‹ اخفاء الكيبورد ›")

          ]

]




  

@app.on_message(filters.regex("^/cmds$") & filters.private)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("‹ اخفاء الكيبورد ›") & filters.private)
async def down(client, message):
          m = await message.reply("<b>- تم اغلاق الكيبورد.</b>", reply_markup= ReplyKeyboardRemove(selective=True))


#@app.on_message(filters.group & command("‹ ربط القنوات ›"))
#async def dowhmo(client: Client, message: Message):
    #await message.reply_text("""- هلا والله\n◌<b>عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌</b> :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { <b>ربط + يوزر القناة</b> }\n3 -› <b>اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل</b>.""",
        #reply_markup=InlineKeyboardMarkup(
            #[
                #[
                    #InlineKeyboardButton(
                        #"قناة السورس", url=f"https://t.me/EF_19"),
                #],[
                    #InlineKeyboardButton(
                        #"• ضيفني لقروبك 🎻", url=f"https://t.me/{app.username}?startgroup=true"),
                #],
            #]
        #),
        #disable_web_page_preview=True
    #)

