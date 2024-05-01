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

@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member, group=847)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 6810952789 # حط ايديك هنا
    if response.from_user.id == dev_id:
        info = await app.get_chat(dev_id)
        name = info.first_name
        bio = info.bio
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(name, user_id=dev_id)]
        ])
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f"• تم انضمام {name} الي هنا\n- {bio}"
        )
