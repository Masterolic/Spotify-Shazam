from bot import bot
from pyrogram import filters


@bot.on_message(
    filters.command("start")
)
async def alive(_, message):
    await message.reply(
       f"𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦 /n__support Spotify  url__ /n__~A single song /n~Albums /n~Playlists /n~Artists__ /n𝗬𝗢𝗨𝗧𝗨𝗕𝗘 /n__Type song name__ /n𝗦𝗢𝗡𝗚 /n__Just send the music name__ /neg `Dil ko karar` /n𝗦𝗛𝗔𝗭𝗔𝗠 /n__Send your song here and wait ....!__ /n𝗚𝗥𝗢𝗨𝗣𝗦 /nYou can add me in groups 🥳🥳🥳 njoy 🥳🥳 more functions in group just type name....!"
    )
