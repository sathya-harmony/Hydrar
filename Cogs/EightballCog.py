import os
import random
import discord
from discord.ext import commands
#from discord_slash import *
#from discord_slash.utils.manage_commands import *


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


class eightball(commands.Cog):

    def __init__(self, client):
        #slash = SlashCommand(self.client, sync_commands=True)
        self.client = client

    @commands.command(aliases=['8B', '8Ball'])
    async def eightball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful.",
                     "Yes, I can."]
        await ctx.message.reply(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(client):
    client.add_cog(eightball(client))
