from bot import bot, max_file


from pyrogram import filters, types
import os


@bot.on_message(  filters.incoming )
async def delete(bot, message):
    await message.reply_text("⏳")
    await message.delete("")
    file_size = message.audio or message.video or message.voice
    file = await message.download(f'{bot.rnd_id()}.mp3')
    r = (await bot.recognize(file)).get('track', None)
    os.remove(file)
    if r is None:
        await message.reply_text(
            '**⚠️ Cannot recognize the audio**'
        )
        return
    out = f'**Title**: `{r["title"]}`\n'
    out += f'**Artist**: `{r["subtitle"]}`\n'
    buttons = [
            [
                types.InlineKeyboardButton(
                    '🎼 Related Songs',
                    switch_inline_query_current_chat=f'related {r["key"]}',
                ),
                types.InlineKeyboardButton(
                    '🔗 Share',
                    url=f'{r["share"]["html"]}'
                )
            ],
            [
                types.InlineKeyboardButton(
                    '🎵 Listen',
                    url=f'{r["url"]}'
                )
            ],        
        ]
    response = r.get('artists', None)
    if response:
        buttons.append(
            [
                types.InlineKeyboardButton(
                    f'💿 More Tracks from {r["subtitle"]}',
                    switch_inline_query_current_chat=f'tracks {r["artists"][0]["id"]}',
                )
            ]
        )
    await message.reply_photo(
        r['images']['coverarthq'],
        caption=out,
        reply_markup=types.InlineKeyboardMarkup(buttons)
    )
