import os
import random
import discord
from discord.ext import commands


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


class says(commands.Cog):
    def __init__(self,  client):
        self.client = client

    # say
    @commands.command()
    async def say(self, ctx, *, text):
        if ctx.message.author.id == 611210739830620165:
            message = ctx.message
            await message.delete()

            await ctx.message.reply(f"{text}")
        else:
            await ctx.message.reply(f"Nope, Not today mate. Ask the owner for permissions ;)")


def setup(client):
    client.add_cog(says(client))
