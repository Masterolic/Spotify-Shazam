from os import path
from configparser import ConfigParser
from pyrogram import Client
from shazamio import Shazam, exceptions, FactoryArtist, FactoryTrack
from dotenv import dotenv_values
from bot import plugins
import asyncio
import io
import json
import locale
import logging
import os
import re
import shutil
import traceback
from urllib.parse import quote

import deezloader.deezloader
import requests
from PIL import Image
from aiogram import Bot, Dispatcher, executor, types, exceptions
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle, InputMediaAudio
from aioify import aioify
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from yt_dlp import YoutubeDL
shazam = Shazam()


class bot(Client):
    def __init__(self, name):
        config_file = f"{name}.ini"
        config = ConfigParser()
        config.read(config_file)
        name = name.lower()
        plugins = {'root': path.join(__package__, 'plugins')} 
        api_id = "19566690"
        api_hash = "9f146b5dab7c76e7f8febec8e3df2501"
        super().__init__(
            name,
            api_id=api_id,
            api_hash=api_hash,
            config_file=config_file,
            workers=16,
            plugins=plugins,
            workdir="./",
        )

    async def start(self):
        await super().start()
        print("bot started. Hi.")

    async def stop(self, *args):
        await super().stop()
        print("bot stopped. Bye.")

    async def recognize(self, path):
        return await shazam.recognize_song(path)

    async def related(self, track_id):
        try:
            return (await shazam.related_tracks(track_id=track_id, limit=50, start_from=2))['tracks']
        except exceptions.FailedDecodeJson:
            return None
    
    async def get_artist(self, query: str):
        artists = await shazam.search_artist(query=query, limit=50)
        hits = []
        try:
            for artist in artists['artists']['hits']:
                hits.append(FactoryArtist(artist).serializer())
            return hits
        except KeyError:
            return None
        
    async def get_artist_tracks(self, artist_id: int):
        tracks = []
        tem = (await shazam.artist_top_tracks(artist_id=artist_id, limit=50))['tracks']
        try:
            for track in tem:
                tracks.append(FactoryTrack(data=track).serializer())
            return tracks
        except KeyError:
            return None
