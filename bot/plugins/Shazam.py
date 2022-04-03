from bot import bot
from pyrogram import filters


@bot.on_message(
    filters.command("shazam")
)
async def alive(_, message):
    await message.reply(
f"Send Ur song here and wait  a while ....! ⚙️🥀  It may take some seconds...!")
