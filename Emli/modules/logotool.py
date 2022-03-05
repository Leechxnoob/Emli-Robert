from pyrogram import filters
from pyrogram.types import Message
from Emli import pbot as app
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from PIL import Image
import io

caption = """
✍️ Generated Successfully✅
`◇───────────────◇`
👨‍💻 **Generated By** : [EMLI](https://t.me/Emili_CTbot)
🙋‍♂️ **Requestor** : {}
⚡️ **Powered By **  : [OMG_INFO](https://t.me/OMG_info)
`◇───────────────◇️ ` 
    """
JOIN_ASAP = f" **🚫 Access Denied**\n\n You Must Join [My News Channel](https://t.me/OMG_info)To Use Me. So, Please Join it & Try Again." 
FSUBB = InlineKeyboardMarkup( 
           [[ 
               InlineKeyboardButton(text="News Channel ", url=f"https://t.me/OMG_info") 
           ]] 
)

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

#logo creator
@app.on_message(filters.command("logo") & ~filters.bot)
async def logo(client, message):      
 try:
        await message._client.get_chat_member(int("-1001270357620"), message.from_user.id)
 except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return    
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "😶 **Please Give me A Text For The Logo**.")
     return
 m = await client.send_message(message.chat.id, "`⚙️ Creating Your logo..`")
 try:
    text = get_text(message)
    LOGO_API = f"https://api.single-developers.software/logo?name={text}"
    randc = (LOGO_API)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    murl = requests.get(f"https://api.single-developers.software/logo?name={text}").history[1].url
    fname = "emlibot.png"
    img.save(fname, "png")
    await client.send_photo(message.chat.id, photo=murl, caption = caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{murl}"
                    )
                ],
            ]
          ),
    )
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'Error, Report @nexleech, {e}')
    await m.delete()

#hq logo creator
@app.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001270357620"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    text = message.text.split(None, 1)[1]
    m = await app.send_message(message.chat.id, "`⚙️ Creating Your logo..`")
    photo = get(f"https://api.single-developers.software/logohq?name={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
    await m.delete()
#handwrite
@app.on_message(filters.command("write"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001270357620"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    text = message.text.split(None, 1)[1]
    m = await app.send_message(message.chat.id, "`⚙️ creating Your text..`")
    API = "https://api.single-developers.software/write"
    body = {     
     "text":f"{text}"     
    }
    req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)
    img = req.history[1].url
    await app.send_photo(message.chat.id, photo=img, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{img}"
                    )
                ]
            ]
          ),
    )
    await m.delete()
#wallpaper
@app.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001270357620"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    text = message.text.split(None, 1)[1]
    m=await app.send_message(message.chat.id, "`⚙️ Creating Your wall..`")
    photo = get(f"https://api.single-developers.software/wallpaper?search={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
    await m.delete()
#slogo
@app.on_message(filters.command("slogo"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001270357620"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    quew = get_text(message)
    if not quew:
        await message.reply_text(message.chat.id, "😶Please give a text.")
        return
    m = await app.send_message(message.chat.id, "`⚙️ Creating Your logo..`")    
    name = message.text.split(None, 1)[1]
    req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
    IMG = req.text
    rurl = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}").text    
    await app.send_photo(message.chat.id, photo=IMG, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{rurl}"
                    )
                ]
            ]
          ),
    )
    await m.delete()

__MODULE__ = "Logo-Tools"
__HELP__ = """
**Create Beautiful logos for your profile pictures from emli.**
×  /logo [TEXT]: Create a logo 
×  /logohq [TEXT]: Create a HQ logo 
×  /write [TEXT] : hand writer
×  /wall [TEXT] : search wallpapers
×  /slogo [TEXT] : New Beautiful trending logo
×  /rlogo [TEXT] : Creating rendom logo
 """

