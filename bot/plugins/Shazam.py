from bot import bot
from pyrogram import filters


@bot.on_message(
    filters.command("shazam")
)
async def alive(_, message):
    await message.reply(
f"Send your song and wait ....! It may take some seconds...!")
