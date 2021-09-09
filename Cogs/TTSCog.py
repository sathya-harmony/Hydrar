import os
import random
from discord.ext import commands
import math
import discord
import asyncio
#import google_trans_new
#from google_trans_new import google_translator
import translate
from translate import Translator
import gtts
import json

#import google_currency


@commands.Cog.listener()
async def on_command_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.message.reply('Please give proper input.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.message.reply(
            "You don't have the permissions to execute this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.reply('Please give proper input.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.reply("Invalid command.")


class TTS(commands.Cog):
    def __init__(self,  client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, translatorr: str, *, args: str):
        #result = google_translator().translate(args, lang_tgt=lang)
        # await ctx.message.reply(result)

        translator = Translator(to_lang=translatorr)
        translation = translator.translate(args)
        await ctx.message.reply(translation)

    @commands.command()
    async def tts(self, ctx, lng, *txt):
        file = gtts.gTTS(text=" ".join(txt), lang=lng, slow=False)
        file.save("Cogs.Audio.audio.mp3")
        await ctx.message.reply(file=discord.File("Cogs.Audio.audio.mp3"))


def setup(client):
    client.add_cog(TTS(client))
