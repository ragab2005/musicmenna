import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app, Telegram
from AnonXMusic.misc import SUDOERS
from pyrogram.enums import ChatType
from config import OWNER_ID, SUPPORT_CHANNEL, SUPPORT_CHAT

async def huhh(client: Client, message: Message): 
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3f3e8043368a35b98fa78.jpg",
        caption=f"• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 🎸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- 𝖲𝗈𝖴𝖱𝖢𝖾 .", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton(
                        "- Help .", url=SUPPORT_CHAT),
                    
                ],[
                    InlineKeyboardButton(
                        "- DeVeLoPeRS .", callback_data=f"developers {message.from_user.id}" if message.chat.type != ChatType.CHANNEL else "developers ch"),
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

