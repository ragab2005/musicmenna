import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["سورس","السورس","براند"], ""))
async def source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/44b1318d300c651d14a45.jpg",
        caption=f"• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 🎸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
               "𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗉𝗌 .", url=f"https://t.me/{bot_username}?startgroup=true"),
                   ],
                   [
                   InlineKeyboardButton(
                   "‹ 𝖲𝗎𝗉𝗉𝗈𝗎𝗋𝗍 ›", url=f"https://t.me/viiiiix"),
                    InlineKeyboardButton(
                        "‹ 𝖲𝗈𝗎𝗋𝖼𝖾 ›", url=f"https://t.me/uo_vn"),
                   ],
                   [
                    InlineKeyboardButton(
                       "‹ 𝖣𝖾𝗏¹ ›", user_id=6810952789),
                    InlineKeyboardButton(
                        "‹ 𝖣𝖾𝗏² ›", user_id=6199134030),    
                   InlineKeyboardButton(
                   ],
                   [
                        "‹ اغلاق ›", callback_data="close"),
               ],
          ]
        ),
    )