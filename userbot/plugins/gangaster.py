from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("gangster ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**EVERYBODY**")
        await asyncio.sleep(2)
        await event.edit("**is**")
        await asyncio.sleep(2)
        await event.edit("**GANGSTER**")
        await asyncio.sleep(1)
        await event.edit("UNTILL")
        await asyncio.sleep(0.2)
        await event.edit("@ALONEGANGSTE4")
        await asyncio.sleep(2)
        await event.edit("**AARIVE**")
        await asyncio.sleep(2)
        await event.edit("😈")
        await asyncio.sleep(3)
        await event.edit("EVERYBODY IS GANGSTER UNTILL [GANGSTER](https://t.me/ALONEGANGSTE4) AARIVE 😈😈😈")
