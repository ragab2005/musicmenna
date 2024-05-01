import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app, Telegram
from AnonXMusic.misc import SUDOERS
from pyrogram.enums import ChatType
from config import OWNER_ID, SUPPORT_CHANNEL, SUPPORT_CHAT

async def huhh(client: Client, message: Message): 
    await message.reply_photo(
        photo=f"https://telegra.ph/file/550cad095c1da597bcb47.jpg",
        caption=f"• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 🎸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Dev¹", user_id=6810952789),
                    InlineKeyboardButton(
                        "Dev²", user_id=6199134030),
                ],
                [
                    
                    InlineKeyboardButton(
                        "𓏺 𝖲𝗈𝗎𝗋𝖼𝖾 𝖡𝗋𝖺𝗇𝖽 .", url="https://t.me/uo_vn"),
                    
                ],

            ]

        ),

    )



@app.on_message(
    filters.command(["سورس$","السورس$","صورص$"],"")
)
async def source(c, msg):
  if msg.chat.type == ChatType.CHANNEL:
      await huhh(c, msg)
  else:
    if not msg.sender_chat:
       await huhh(c, msg)

