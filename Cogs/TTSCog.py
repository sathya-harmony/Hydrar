import os
import random
from discord.ext import commands
import math
import discord
import asyncio
import googletrans
from googletrans import Translator

#import google_currency


@commands.Cog.listener()
async def on_command_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send('Please give proper input.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "You don't have the permissions to execute this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please give proper input.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command.")


class TTS(commands.Cog):
    def __init__(self,  client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, lang, *, args):
        t = Translator
        a = t.translate(args, dest=lang)
        await ctx.send(a.text)\



def setup(client):
    client.add_cog(TTS(client))
