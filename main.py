import asyncio
#from re import T
from discord.ext import commands  # ipc
import discord
from fractions import *
from discord.ext.commands.cog import Cog
import traceback
import sys
from alexa_reply import reply
import pymongo
import os
#from discord_buttons_plugin.__main__ import ButtonsClient
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType
import aiohttp
import io
import textwrap
import contextlib
from traceback import format_exception

#import Cogs.EconomyCog
#import Dashboard.main


'''from passwordmeter import test
from urllib import urlopenx 
from os.path import isfile
from random import choice, randint'''


#from prsaw import RandomStuff


'''class MyBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self, secret_key="Ssath")

    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("Ipc server is ready.")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        print(endpoint, "raised", error)'''


prefix = '-'
#api_key = "RRcoNdt3Qs8k"
#rs = RandomStuff(async_mode = True, api_key = api_key)


client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      intents=discord.Intents.all())
#buttons = ButtonsClient(client)

client.remove_command('help')


'''@client.ipc.route()
async def get_guild_count(data):
    return len(client.guilds)  # returns the len of the guilds to the client


@client.ipc.route()
async def get_guild_ids(data):
    final = []
    for guild in client.guilds:
        final.append(guild.id)
    return final  # returns the guild ids to the client


@client.ipc.route()
async def get_guild(data):
    guild = client.get_guild(data.guild_id)
    if guild is None:
        return None

    guild_data = {
        "name": guild.name,
        "id": guild.id,
        "prefix": "-"
    }

    return guild_data'''


owner_perms = {611210739830620165}
client.sniped_messages = {}
YOURLIST = []


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (
        message.content, message.author, message.channel.name, message.created_at)


@client.event
async def on_message(msg):
    if msg.author.id not in YOURLIST:
        await client.process_commands(msg)


@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.message.reply("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents,
                          color=discord.Color.purple(), timestamp=time)
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.message.reply(embed=embed)


# Log Channel.
log_channel = None


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.message.reply('Please give proper input.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.message.reply(
            "You don't have the permissions to execute this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.reply('Please give proper input.')
    elif isinstance(error, commands.CommandNotFound):
        pass

    elif isinstance(error, commands.CommandOnCooldown):
        pass
    else:
        print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr)
        tb = ''.join(map(lambda x: x.replace('\\n', '\n'), traceback.format_exception(
            type(error), error, error.__traceback__)))
        await log(f"{error}\n{getattr(error, 'original', error)}\n\n```{tb}```")

#intents = discord.Intents.all()
#intents.members = True


'''@client.event
async def on_member_join(member):
    guild = client.get_guild(846947170782281729)
    channel = guild.get_channel(846947170782281732)
    intro = "<#847508482454323270>"
    await channel.send(f"Welcome to {guild.name} {member.mention}! Please Introduce yourself in {intro}")'''


# help command
client.load_extension('Cogs.HelpCog_test')
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
# Economy system
client.load_extension('Cogs.EconomyCog')
# music
# lient.load_extension('Supporting.MusicCog')


'''@client.command()
async def password(ctx, amount: int):'''


def cop(ctx):
    if ctx.author.id in owner_perms:
        return True

    return False


# Owner Permissions.
async def op(ctx, msg=None):
    if ctx.author.id in owner_perms:

        if msg is not None:
            await ctx.message.reply(msg)
        return True

    await ctx.message.reply("Only bot owner(s) can use this command.")
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

    activity = discord.Game(name="-help | Busy Helping People!😊", type=5)
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    print('The bot has booted up.')
    await log('The bot, Running on **Local Machine** is **Online**')
    DiscordComponents(client)
    '''while True:
        await asyncio.sleep(10)
        with open("Cogs/spamdetect.txt", "r+") as file:
            file.truncate(0)'''


'''@client.event
async def on_message(message):
    counter = 0
    with open("Cogs/spamdetect.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter += 1

        file.writelines(f"{str(message.author.id)}\n")
        if counter > 3:
            role = discord.Role('muted')
            await discord.Member.add_roles(role)
            await asyncio.sleep(300)'''


'''@client.command()
async def do(ctx, *, python_code):
    if await op(ctx):

        x = eval(python_code)
        await ctx.send(x)'''


@client.command()
async def disable(ctx, member: discord.Member):
    if await op(ctx):
        YOURLIST.append(member.id)


@client.command(name="toggle")
async def toggle(ctx, *, command):
    command = client.get_command(command)
    if command is None:
        await ctx.send("bruh how to do you expect me to toggle no command??")
    elif ctx.command == command:
        await ctx.send("You cannot disable this command")
    else:
        command.enabled = not command.enabled
        ternary = "enabled" if command.enabled else "disabled"
        ternary2 = "disabled" if command.enabled else "enabled"
        await ctx.send(f"I have {ternary} {command.qualified_name}. Until this command is {ternary2}")


@client.command()
async def rcogs(ctx, cog=None):
    if await op(ctx):
        if not cog:
            # No cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir(r"Cogs"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            client.unload_extension(f"Cogs.{ext[:-3]}")
                            client.load_extension(f"Cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded: `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog}"
                if not os.path.exists(f"Cogs.{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif os.path.exists(f"Cogs.{ext}") and ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        client.unload_extension(f"Cogs.{ext[:-3]}")
                        client.load_extension(f"Cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.send(embed=embed)


def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:][:-3])
    return content


@client.command(name="do")
async def _do(ctx, *, code):
    if await op(ctx):
        code = clean_code(code)
        local_var = {
            "discord": discord,
            "commands": commands,
            "client": client,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message

        }
        stdout = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_var
                )
                obj = await local_var["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}\n"

        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        embed = discord.Embed(
            Title="Successfully ran your code!!", description=result)


@client.command()
async def chat(ctx, *, message):
    owner = "Sathya"
    bot = "Hydrargyrum"
    resp = reply(message, bot, owner)
    await ctx.message.reply(resp)


# client.ipc.start()
Token = 'ODQ0ODEzMzE2NTA1MDc1NzEy.YKX3tg.AGjRaxwtYgBiOeHWfPEupR-FypU'
client.run(Token)
