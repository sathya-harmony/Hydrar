import discord
import os
import requests
import json
import ast
import asyncio
from discord.ext import commands
#import pyjokes

prefix = '-'
client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      intents=discord.Intents.all())


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


class Quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def quote(self, ctx):
        async with ctx.channel.typing():
            await asyncio.sleep(0.5)
        response = requests.get("https://py-quoters.herokuapp.com/")
        wl = response.text
        quod = ast.literal_eval(wl)
        quote = quod["quote"]

        await ctx.send(f"**Here's a Quote to Inspire you:**\n{quote}")

    '''@commands.command()
    async def joke(self, ctx):
        async with ctx.channel.typing():
            await asyncio.sleep(0.5)
        await ctx.send((pyjokes.get_joke()))'''


def setup(client):
    client.add_cog(Quote(client))
