from pyrogram import filters, Client
from AnonXMusic import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)

@app.on_message(filters.regex("مين في الكول","مين ف الكول"))
async def strcall(client, message):
    assistant = await group_assistant(Anony,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./assets/vega.mp3"), stream_type=StreamType().pulse_stream)
        text="الموجودين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث"
            else:
                mut="ساكت"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}•{user.mention}•{mut}\n"
        text += f"\nعددهم : {len(participants)}\n¡"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"الكول مقفول حاليا")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكلة في السيرفر او راسل مطور البوت لحلها : @lPlJI")
    except AlreadyJoinedError:
        text="الموجودين في الكول:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث"
            else:
                mut="ساكت"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}•{user.mention}•{mut}\n"
        text += f"\nعددهم : {len(participants)}\n¿"    
        await message.reply(f"{text}")