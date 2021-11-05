import asyncio
from discord.errors import HTTPException
#from re import T
from discord.ext import commands  # ipc
import discord
from fractions import *
from discord.ext.commands.cog import Cog
import traceback
import sys
from alexa_reply import reply
import os
from discord.ext.commands.errors import CommandInvokeError
from discord_components import DiscordComponents
import io
import textwrap
import contextlib
from traceback import format_exception
from discord.ext.buttons import Paginator
from modules.common import *
#import threading
#from sympy.interactive import printing
import urllib
from PIL import Image as im
import datetime
import random


'''import numpy as np
import sympy as sp
printing.init_printing(use_latex=True)
'''
#from discord.ext import ipc
#from discord_slash_components_bridge import SlashCommand


print('Hydrargyrum is loading...')
# cluster = MongoClient(
#     "mongodb+srv://Hydra:CihVirus123@economy.2xn9e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

Prefixes_MongoDB = cluster["Extras"]["Prefix"]
'''intents = discord.Intents().default()
intents.presences = True
intents.members = True
'''


'''class MyBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self, secret_key="Sath")

    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("Ipc server is ready.")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        print(endpoint, "raised", error)'''


#api_key = "RRcoNdt3Qs8k"
#rs = RandomStuff(async_mode = True, api_key = api_key)
def get_prefix(client, message):
    '''if type(user_id) in [int, float]:
            user_id = str(int(user_id))'''

    Prefixes = Prefixes_MongoDB.find_one(
        {"guild_id": str(message.guild.id)})

    if Prefixes is None:
        Prefixes = {"guild_id": str(message.guild.id),
                    "Prefix": '-'}
        Prefixes_MongoDB.insert_one(Prefixes)

    prefix = Prefixes['Prefix']

    return prefix


'''def strip_prefix(prefix):
    prefix = get_prefix
    if len(prefix) > 1:
        return True
'''

client = commands.Bot(command_prefix=get_prefix,
                      strip_after_prefix=True,
                      case_insensitive=True,
                      intents=discord.Intents.all())


#slash = discord_slash.SlashCommand(client, sync_commands=True)

client.remove_command('help')


@client.event
async def on_guild_join(guild):
    Prefixes = Prefixes_MongoDB.find_one(
        {"guild_id": str(guild.id)})
    if Prefixes is None:
        new_guild = {"guild_id": str(guild.id),
                     "Prefix": '-'}
        Prefixes = Prefixes_MongoDB.insert_one(new_guild)


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


owner_perms = [611210739830620165, 538983723950014474]
client.sniped_messages = {}
YOURLIST = []


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (
        message.content, message.author, message.channel.name, message.created_at)


@client.event
async def on_message(msg):
    try:
        # print(msg.content)
        if client.user.id in (member.id for member in msg.mentions) and len(msg.mentions) == 1:
            Prefixes = Prefixes_MongoDB.find_one(
                {"guild_id": str(msg.guild.id)})
            if Prefixes is None:
                new_guild = {"guild_id": str(msg.guild.id),
                             "Prefix": '-'}
                Prefixes = Prefixes_MongoDB.insert_one(new_guild)
            prefix = Prefixes["Prefix"]
            await msg.channel.send(f"My Prefix for this server is `{prefix}`")
            return
    except:
        pass

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


'''@slash.slash(name='Snipe', description="Retreieve the most recently deleted message!")
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents,
                          color=discord.Color.purple(), timestamp=time)
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.send(embed=embed)'''

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
# client.load_extension('Cogs.TTSCog')
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
        log_channel = await client.fetch_channel(896428684158844928)

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


@client.command()
@owner_or_perm(administrator=True)
async def changeprefix(ctx, prefix):
    Prefixes = Prefixes_MongoDB.find_one(
        {"guild_id": str(ctx.guild.id)})
    if Prefixes is None:
        new_guild = {"guild_id": str(ctx.guild.id),
                     "Prefix": '-'}
        Prefixes = Prefixes_MongoDB.insert_one(new_guild)
        return Prefixes

    Prefixes["Prefix"] = prefix
    _prefix = Prefixes["Prefix"]
    await ctx.message.reply(f"Prefix for {client.user.mention} was changed to **{_prefix}**")
    Prefixes_MongoDB.update_one(
        {"guild_id": str(ctx.guild.id)}, {"$set": Prefixes})


# Execute this whenever the bot is ready.
@client.event
async def on_ready():

    activity = discord.Game(name="-help | Busy Helping People!😊", type=5)
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    print('The bot has booted up.')
    await log('The bot, Running on **Local Machine** is **Online**')
    DiscordComponents(client)
    #slash  =  discord_slash.SlashCommand(client, sync_commands=True)


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
                for ext in os.listdir("./Cogs/"):
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
                ext = f"{cog}.py"
                if not os.path.exists(f"./Cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
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
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content


class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass


@client.command(name="eval", aliases=["exec", "do"])
async def _eval(ctx, *, code):
    if await op(ctx):
        code = clean_code(code)

        local_variables = {
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
                    f"async def functions():\n{textwrap.indent(code, '      ')}", local_variables,
                )

                obj = await local_variables["functions"]()

                result = f"{stdout.getvalue()}\n-- {obj}\n"

        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        pager = Pag(
            timeout=100,
            entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
            length=1,
            prefix="```py\n",
            suffix="```"
        )

        await pager.start(ctx)


@client.command()
async def chat(ctx, *, message):
    owner = "Sathya"
    bot = "Hydrargyrum"
    resp = reply(message, bot, owner)
    await ctx.message.reply(resp)


@client.command()
async def latex(ctx, *, code):
    '''def f(x):

        return np.sin(x)
    func = sp.Function('func')
    x = sp.Symbol('x')
    func = sp.sin(x)
    await ctx.send(func)'''
    #
    code = code.replace(" ", "&space;")
    code = code.replace("+", "&plus;")
    code = code.replace("<", "%3C")
    code = code.replace(">", "%3E")
    code = code.replace("#", "%23")
    code = code.replace("%", "%25")
    code = code.replace("{", "%7B")
    code = code.replace("}", "%7D")
    code = code.replace("|", "%7C")
    code = code.replace("\\", "%5C")
    code = code.replace("^", "%5E")
    code = code.replace("~", "%7E")
    code = code.replace("[", "%5B")
    code = code.replace("]", "%5D")
    code = code.replace("'", "%60")
    code = code.replace(";", "%3B")
    code = code.replace("/", "%2F")
    code = code.replace("?", "%3F")
    code = code.replace(":", "%3A")
    code = code.replace("@", "%40")
    code = code.replace("=", "%3D")
    code = code.replace("&", "%26")
    code = code.replace("$", "%24")
    settings = r'\bg_white\dpi{700}'
    try:
        urllib.request.urlretrieve(
            f"https://latex.codecogs.com/png.image?{settings}{code}", "image.png")
    except urllib.error.HTTPError:
        await ctx.message.reply("**Compilation Error❌**\nPlease check your input!")
        return
    '''Image = im.open("image.png")
    Image.resize((790, 200))'''

    #Image = Image.resize((200, 200))
    await ctx.message.reply(file=discord.File("image.png"))


@client.command()
async def gstart(ctx, mins: int, *, prize: str):
    embed = discord.Embed(
        title="🎉Giveaway", description=f"{prize}", color=ctx.author.color)
    end = int(datetime.datetime.utcnow() +
              datetime.timedelta(seconds=float(mins*60)))
    embed.add_field(name="Ends At:", value=f"{end} UTC")
    embed.set_footer(text=f"Ends in {mins} from now!")

    my_msg = await ctx.send(embed=embed)
    await my_msg.add_reaction("🎉")
    time = int(mins*60)
    await asyncio.sleep(time)

    new_msg = await ctx.channel.fetch_message(my_msg.id)
    users = await new_msg[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)
    await ctx.send(f"Congrats {winner.mention}!! You won {prize}")


# client.ipc.start()
Token = 'ODQ0ODEzMzE2NTA1MDc1NzEy.YKX3tg.AGjRaxwtYgBiOeHWfPEupR-FypU'
client.run(Token)
