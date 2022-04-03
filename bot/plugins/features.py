from bot import bot

from pyrogram import filters
@bot.on_message(
    filters.command("shazam")
)
async def alive(_, message):
    await message.reply(
f"𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦 \n __support Spotify  url__ \n __~A single song \n ~Albums \n ~Playlists \n ~Artists__ \n\n 𝗬𝗢𝗨𝗧𝗨𝗕𝗘 \n __Type song name__ \n\n 𝗦𝗢𝗡𝗚 \n __Just send the music name__ \neg `Dil ko karar`\n\n 𝗦𝗛𝗔𝗭𝗔𝗠 \n __Send your song here and wait ....!__ \n\n 𝗚𝗥𝗢𝗨𝗣𝗦 \n You can add me in groups 🥳🥳🥳 njoy 🥳🥳 more functions in group just type name....!"
    )
