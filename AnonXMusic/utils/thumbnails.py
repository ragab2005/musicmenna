import os
import re

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch

from AnonXMusic import app
from config import YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(videoid, photo):
    if os.path.isfile(f"{photo}.png"):
        return f"{photo}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"thumb{videoid}.png")
        Shadow = Image.open(f"{photo}")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = Shadow.width / 2
        Ycenter = Shadow.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = Shadow.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(f"AnonXMusic/assets/font.ttf", 40)
        font2 = ImageFont.truetype(f"AnonXMusic/assets/font.ttf", 70)
        arial = ImageFont.truetype(f"AnonXMusic/assets/font.ttf", 30)
        name_font = ImageFont.truetype(f"AnonXMusic/assets/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (600, 150),
            "BRAND PLAYING",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 340),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 280),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )

        draw.text(
            (600, 450),
            f"Views : {views[:23]}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Duration : {duration[:23]} Mins",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"Channel : {channel}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"{photo}")
            os.remove(f"thumb{videoid}.png")
        except:
            pass
        background.save(f"{photo}.png")
        return f"{photo}.png"
    except Exception:
        return FAILED 


async def gen_bot(c: Client, BOT_USERNAME, photo):
        if os.path.isfile(f"{BOT_USERNAME}.png"):
           return f"{BOT_USERNAME}.png"
        users = len(r.smembers(f"{BOT_ID}:users"))
        chats = len(r.smembers(f"{BOT_ID}:groups"))
        url = f"https://www.youtube.com/watch?v=gKA2XFkJZhI"
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"thumb{BOT_USERNAME}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"{photo}")
        a = Image.open(f"{photo}")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = a.width / 2
        Ycenter = a.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = a.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(f"AnonXMusic/assets/font.ttf", 40)
        font2 = ImageFont.truetype(f"AnonXMusic/assets/font.ttf", 70)
        arial = ImageFont.truetype(f"AnonXMusic/assets/font.ttf", 30)
        name_font = ImageFont.truetype(f"AnonXMusic/AnonXMusic/font.ttf", 30)
        draw.text(
            (600, 150),
            "Music Player BoT",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        draw.text(
            (600, 340),
            f"Dev: Ragab",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        draw.text(
            (600, 280),
            f"Playing Music & Video",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )

        draw.text(
            (600, 400),
            f"users: {users}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 450),
            f"chats: {chats}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Version: 0.2.0",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"BoT: t.me\{BOT_USERNAME}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"thumb{BOT_USERNAME}.png")
        except:
            pass
        background.save(f"{BOT_USERNAME}.png")
        return f"{BOT_USERNAME}.png"
