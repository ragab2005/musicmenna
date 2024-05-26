import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["مصنع","مصنع رجب","المصنع","مصنع السورس"], ""))
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/114450080dcc214a4541f.jpg",
        caption=f"""[• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 .](https://t.me/uo_vn) 

• اهلا بك عزيزي {message.from_user.mention()} اليك مصانع سورس براند""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "سورس براند", url=f"https://t.me/uo_vn"),
                   ],
                   [
                    InlineKeyboardButton(
                       "لتنصيب بوت ميوزك", url=f"https://t.me/lPlJI"),
                   ],
                   [     
                    InlineKeyboardButton(
                        "لتنصيب بوت حماية", url=f"https://t.me/RaaGaBboT"),    
                   InlineKeyboardButton(
                        "إغلاق", callback_data="close"),
               ],
          ]
        ),
    )