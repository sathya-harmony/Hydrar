import randfacts
import discord
import os
import requests
import json
import ast
from discord.ext import commands
prefix = '-'
client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      intents=discord.Intents.all())


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


class Facts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['facts'])
    async def fact(self, ctx):
        x = randfacts.getFact()
        await ctx.message.reply(x)


def setup(client):
    client.add_cog(Facts(client))
