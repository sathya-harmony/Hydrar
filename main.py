from datetime import datetime
from typing import Optional
from discord import Member
from discord.ext import commands
import discord
import math
from fractions import *
from discord.ext.commands.cog import Cog
import wolframalpha
import os
import asyncio
from alexa_reply import reply


#from prsaw import RandomStuff

prefix = '-'
#api_key = "RRcoNdt3Qs8k"
#rs = RandomStuff(async_mode = True, api_key = api_key)

client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      intents=discord.Intents.all())
client.remove_command('help')

owner_perms = {611210739830620165}

# Log Channel.
log_channel = None


@client.event
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

intents = discord.Intents.default()
intents.members = True


@client.event
async def on_member_join(member):
    guild = client.get_guild(846947170782281729)
    channel = guild.get_channel(846947170782281732)
    intro = guild.get_channel(847508482454323270)
    await channel.send(f"Welcome to {guild.name} {member.mention}! Please Introduce yourself in {intro}")


# help command
client.load_extension('Cogs.HelpCog')
# ping
client.load_extension('Cogs.PingCog')
# 8ball
client.load_extension('Cogs.EightballCog')
# say
client.load_extension('Cogs.SayCog')
# kick_ban_unban
client.load_extension('Cogs.Kick_BanCog')
# spam_Cspam
client.load_extension('Cogs.Spam_CspamCog')
# clear
client.load_extension('Cogs.ClearCog')
# Server_User
client.load_extension('Cogs.Server_UserCog')
# Math
client.load_extension('Cogs.MathCog')
# Quote
client.load_extension('Cogs.QuoteCog')
# Wanted
client.load_extension('Cogs.WantedCog')
# Facts
client.load_extension('Cogs.FactsCog')
#
client.load_extension('Cogs.LevelsCog')
# tts
client.load_extension('Cogs.TTSCog')


def cop(ctx):
    if ctx.author.id in owner_perms:
        return True

    return False


# Owner Permissions.
async def op(ctx, msg=None):
    if ctx.author.id in owner_perms:

        if msg is not None:
            await ctx.send(msg)
        return True

    await ctx.send("Only bot owner(s) can use this command.")
    return False


# Log.
async def log(*args, **kwargs):
    global log_channel

    if log_channel is None:
        log_channel = await client.fetch_channel(844871857169760306)

    # Return the logged message.
    return await log_channel.send(*args, **kwargs)


def owner_or_perm(**perms):
    original = commands.has_guild_permissions(**perms).predicate

    async def extended_check(ctx):
        if ctx.guild is None:
            return False

        is_bot_owner = cop(ctx)

        return (ctx.guild.owner_id == ctx.author.id
                or is_bot_owner) or await original(ctx)

    return commands.check(extended_check)


# Execute this whenever the bot is ready.
@client.event
async def on_ready():
    activity = discord.Game(name="-help | Busy Helping People!😊", type=3)
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    print('The bot has booted up.')
    await log('The bot is online.')


@client.command()
async def chat(ctx, *, message):
    owner = "Sathya"
    bot = "Hydrargyrum"
    resp = reply(message, bot, owner)
    await ctx.send(resp)


'''@client.event
async def on_message(message):
  try:
      if client.user == message.author:
         return
      if message.channel.id == 844871857169760306 : 
          response = await rs.get_ai_response(message.content)
          await message.reply(response[0]['message'])

          await client.process_commands(message)
  except ValueError:
    pass'''


# keep_alive()
#my_secret = os.environ['Hydra']
# client.run(my_secret)


Token = 'ODQ0ODEzMzE2NTA1MDc1NzEy.YKX3tg.0eYGwHfkQMKEbF71c8dVDmGVlBI'
client.run(Token)
