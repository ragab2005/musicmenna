import asyncio


import asyncio
import aiohttp
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import enums
import config

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton





import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = 6810952789
OWNER = getenv("OWNER")



@app.on_message(filters.command(["مطور السورس", "رجب","سبايدر"], ""))
async def dev(client: Client, message: Message):
     bot_username = client.me.username
     user = await client.get_chat(6810952789)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"𓏺 𝖭𝖺𝗆𝖾 : {message.from_user.mention} \n 𓏺 𝖭𝖺𝗆𝖾 : {title}" if message.from_user else f"𝗂𝖣 : {message.chat.title}"
     try:
      await client.send_message(username, f"<b></b>\n حـد بينـادي عليك\n{chat_title}\nايدي الجروب : {message.chat.id}",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"<b>• مطور السورس ◟</b>\n\n<b>• 𝖭𝖺𝗆𝖾 : {name}</b>\n<b>• 𝖴𝗌𝖾 : @{username}</b>\n<b>• 𝖡𝗂𝗈 : {bio}</b>",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()


OWNER_ID = 6717529449
OWNER = getenv("OWNER")



@app.on_message(filters.command(["قلب رجب", "مورفينة","مورفين"], ""))
async def dev(client: Client, message: Message):
     bot_username = client.me.username
     user = await client.get_chat(6717529449)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"𓏺 𝖭𝖺𝗆𝖾 : {message.from_user.mention} \n 𓏺 𝖭𝖺𝗆𝖾 : {title}" if message.from_user else f"𝗂𝖣 : {message.chat.title}"
     try:
      await client.send_message(username, f"<b></b>\n حـد بينـادي عليك\n{chat_title}\nايدي الجروب : {message.chat.id}",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"<b>• معلومات قلب رجب ◟</b>\n\n<b>• 𝖭𝖺𝗆𝖾 : {name}</b>\n<b>• 𝖴𝗌𝖾 : @{username}</b>\n<b>• 𝖡𝗂𝗈 : {bio}</b>",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = getenv("OWNER_ID")
OWNER = getenv("OWNER")



@app.on_message(filters.command(["المطور", "مطور البوت"], ""))
async def dev(client: Client, message: Message):
     bot_username = client.me.username
     user = await client.get_chat(OWNER_ID)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"𓏺 𝖭𝖺𝗆𝖾 : {message.from_user.mention} \n 𓏺 𝖭𝖺𝗆𝖾 : {title}" if message.from_user else f"𝗂𝖣 : {message.chat.title}"
     try:
      await client.send_message(username, f"<b></b>\n حـد بينـادي عليك\n{chat_title}\nايدي الجروب : {message.chat.id}",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"<b>• مطور البوت ◟</b>\n\n<b>• 𝖭𝖺𝗆𝖾 : {name}</b>\n<b>• 𝖴𝗌𝖾 : @{username}</b>\n<b>• 𝖡𝗂𝗈 : {bio}</b>",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
