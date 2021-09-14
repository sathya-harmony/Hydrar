from logging import error, exception
import os
import random
from discord.ext import commands
import math
import discord
import asyncio
from discord.ext.commands.errors import CommandInvokeError
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
     # try:
        translator = Translator(to_lang=translatorr)
        translation = translator.translate(args)
        if "INVALID TARGET" in translation:
            await ctx.message.reply("Invalid target language. Please click on this link to view the languages supported by us:- <https://cloud.google.com/translate/docs/languages>")
        else:
            await ctx.message.reply(translation)

     # except pass

    '''@commands.command()
    async def tts(self, ctx, lng: str, *txt: str):
        try:
            file = gtts.gTTS(text="".join(txt), lang=lng, slow=False)

        except error:
            pass
        file.save(f"{ctx.author.name}'s divine words.mp3")
        await ctx.message.reply(file=discord.File(f"{ctx.author.name}'s divine words.mp3"))'''


def setup(client):
    client.add_cog(TTS(client))
