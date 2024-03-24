#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("**ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ғᴏʀ ᴛʜᴜᴍʙɴᴀɪʟ 🖼**")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("**sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ:** ɴᴏ ᴍᴇᴅɪᴀ ғᴏᴜɴᴅ 😒")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("**sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ:** ɴᴏ ᴍᴇᴅɪᴀ ғᴏᴜɴᴅ 😒")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("ᴛᴇᴍᴘᴏʀᴀʀʏ ᴛʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('ᴛʀʏɪɴɢ')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('ᴍᴇᴅɪᴀ ʀᴇᴍᴏᴠᴇᴅ!')
    except Exception:
        await event.edit("ɴᴏ sᴀᴠᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "**ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴄʟᴏɴᴇ ʜᴇʀᴇ, ғᴏʀ ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ sᴇɴᴅ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ**\n\n**SUPPORT:** @WantedBots"
    await start_srb(event, text)
    
