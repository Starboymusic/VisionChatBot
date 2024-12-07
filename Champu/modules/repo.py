import asyncio
import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import IMG
from Champu import ChampuBot


start_txt = """**
✪ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗦𝘁𝗮𝗿𝗯𝗼𝘆 𝗥𝗲𝗽𝗼𝘀 ✪

➲ ᴇᴀsʏ ʜᴇʀᴏᴋᴜ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ✰  
➲ ɴᴏ ʙᴀɴ ɪssᴜᴇs ✰  
➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰  
➲ 𝟸𝟺/𝟽 ʟᴀɢ-ғʀᴇᴇ ✰

► sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍs!
**"""




@ChampuBot.on_cmd("repo")
async def repo(_, m: Message):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{ChampuBot.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("YKD", url="https://t.me/YKD_KOREAN_DRAMA"),
          InlineKeyboardButton("STARBOY", url="https://t.me/Star_Boy_96_vibes"),
          ],
               [
                InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Starboy_012"),

],
[
              InlineKeyboardButton("YKD", url=f"https://t.me/YKD_KOREAN_DRAMA"),
              InlineKeyboardButton("STARBOY", url=f"https://t.me/Star_Boy_96_vibes")
              ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await m.reply_photo(
        photo=random.choice(IMG),
        caption=start_txt,
        reply_markup=reply_markup
    )
