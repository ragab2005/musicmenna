from pyrogram import filters, Client
from AnonXMusic import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)

@app.on_message(filters.command(["مين في الكول","مين ف الكول","الموجودين في الكول"], "")
& filters.group
)
async def strcall(client, message):
    assistant = await group_assistant(Anony,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("AnonXMusic/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="<b>• الاعضاء المتواجدين في الكول :</b>\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="<b>• بيتكلم</b>"
            else:
                mut="<b>ساكت</b>"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"<b>{k}• {user.mention}➤{mut}</b>\n"
        text += f"<b>\n• عددهم : {len(participants)}\n</b>"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"<b>• الكول مقفول\n<b>")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في السيرفر\n")