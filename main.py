import asyncio
from discord.ext import commands  # ipc
import discord
from fractions import *
from discord.ext.commands.cog import Cog
import traceback
from alexa_reply import reply
import os
from discord_components import DiscordComponents
import io
import textwrap
import contextlib
from traceback import format_exception
from discord.ext.buttons import Paginator
from modules.common import *
import urllib
from PIL import Image as im
from PIL import Image
import sys


print('Hydrargyrum is loading...')


Prefixes_MongoDB = cluster["Extras"]["Prefix"]
enableddisabled_db = cluster["Extras"]["Extras"]
#api_key = "RRcoNdt3Qs8k"
#rs = RandomStuff(async_mode = True, api_key = api_key)


def get_prefix(client, message):
    Prefixes = Prefixes_MongoDB.find_one(
        {"guild_id": str(message.guild.id)})

    if Prefixes is None:
        Prefixes = {"guild_id": str(message.guild.id),
                    "Prefix": '-'}
        Prefixes_MongoDB.insert_one(Prefixes)

    prefix = Prefixes['Prefix']

    return prefix


client = commands.Bot(command_prefix=get_prefix,
                      strip_after_prefix=True,
                      case_insensitive=True,
                      intents=discord.Intents.all())


client.remove_command('help')


@client.event
async def on_guild_join(guild):
    Prefixes = Prefixes_MongoDB.find_one(
        {"guild_id": str(guild.id)})
    if Prefixes is None:
        new_guild = {"guild_id": str(guild.id),
                     "Prefix": '-'}
        Prefixes = Prefixes_MongoDB.insert_one(new_guild)


#owner_perms = [611210739830620165, 538983723950014474]
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
        message = str(msg.content)
        if (f"<@{client.user.id}>") in message or (f"<@!{client.user.id}>") in message:
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


# Log Channel.
#log_channel = None


'''@client.event
async def on_command(ctx):
    # try:

    command = client.get_command(ctx.command)
    commands = enableddisabled_db.find_one({"guild_id": str(ctx.guild.id)})
    # for i in commands["disabled_commands"]:
    while command in commands["disabled_commands"]:
        command.enabled = False
    else:
        command.enabled = True'''


'''@client.event
async def on_command(ctx):
    commands = enableddisabled_db.find_one({"guild_id": str(ctx.guild.id)})

    if str(ctx.command) in commands["disabled_commands"]:
        # raise discord.ext.commands.DisabledCommandctx.
        command = client.get_command(ctx.command)
        command.enabled = False'''


'''@client.before_invoke
async def before_command(ctx):
    commands = enableddisabled_db.find_one({"guild_id": str(ctx.guild.id)})

    if str(ctx.command) in commands["disabled_commands"]:
        raise discord.ext.commands.DisabledCommand


@client.check
async def disabled_command_check(ctx):
    commands = enableddisabled_db.find_one({"guild_id": str(ctx.guild.id)})
    # if commands is not None:

    if str(ctx.command) in commands["disabled_commands"]:
        raise discord.ext.commands.DisabledCommand

    return True'''


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.name in PRIVATE_CMDS and not check_owner_perms(ctx):
            return

        await ctx.invoke(client.get_command("help"), cmd=ctx.command, txt=["Please pass in all required arguments."])

    elif isinstance(error, commands.CommandNotFound):
        pass
        # await ctx.send("Invalid Command.")

    elif isinstance(error, commands.MissingPermissions):
        missing = [perm.replace('_', ' ').replace(
            'guild', 'server').title() for perm in error.missing_permissions]

        if len(missing) > 2:
            fmt = '{}**, and **{}'.format(
                "**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = '** and **'.join(missing)

        _message = f'You need the **{fmt}** permission(s) to use this command.'
        await ctx.reply(_message)

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"That command is on cooldown. Try again in {error.retry_after:,.2f} secs.")

    elif isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace(
            'guild', 'server').title() for perm in error.missing_permissions]

        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)

        _message = f'I need the **{fmt}** permission(s) to run this command.'
        await ctx.reply(_message)

    elif isinstance(error, commands.DisabledCommand):
        await ctx.reply('This command has been disabled.')

    elif isinstance(error, commands.UserInputError):
        if ctx.command.name in PRIVATE_CMDS and not check_owner_perms(ctx):
            return

        await ctx.invoke(client.get_command("help"), cmd=ctx.command, txt=["Invalid Input."])

    elif isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.reply('This command cannot be used in direct messages.')
        except discord.Forbidden:
            pass

    elif isinstance(error, commands.CheckFailure):
        await ctx.reply("You do not have permission to use this command.")

    elif isinstance(error, commands.CommandInvokeError):
        if "Missing Permissions".lower() in str(getattr(error, 'original', error)).lower():
            try:
                await ctx.reply("I can't perform this action. Some **error** occurred. Maybe I don't have enough permissions.\n**Check my permissions properly.**\nReport to the owners if you think there is some problem.")
            except:
                pass
        else:
            await log_error(ctx, error)

    elif isinstance(error, NotAGuildError):
        try:
            await ctx.reply('This is a **Server Only** command.\nPlease go to a server to use this command.')
        except discord.Forbidden:
            pass

    else:
        await log_error(ctx, error)
#intents = discord.Intents.all()
#intents.members = True


async def log_error(ctx, error):
    print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
    traceback.print_exception(
        type(error), error, error.__traceback__, file=sys.stderr)
    tb = '```py\n' + ''.join(map(lambda x: x.replace('\\n', '\n'), traceback.format_exception(
        type(error), error, error.__traceback__))) + '```'
    print(type(error))


async def log(*args, **kwargs):
    log_channel = client.get_channel(LOG_CHANNEL_ID)
    return await log_channel.send(*args, **kwargs)


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
#client.load_extension('Cogs.timetable')


def cop(ctx):
    if ctx.author.id in OWNER_PERMS:
        return True

    return False


# Owner Permissions.
async def op(ctx, msg=None):
    if ctx.author.id in OWNER_PERMS:

        if msg is not None:
            await ctx.message.reply(msg)
        return True

    await ctx.message.reply("Only bot owner(s) can use this command.")
    return False


'''# Log.
async def log(*args, **kwargs):
    global log_channel

    if log_channel is None:
        log_channel = await client.fetch_channel(896428684158844928)

    # Return the logged message.
    return await log_channel.send(*args, **kwargs)'''


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


'''@client.command()
async def disable(ctx, member: discord.Member):
    if await op(ctx):
        YOURLIST.append(member.id)'''


'''@client.command(name="toggle")
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
        await ctx.send(f"I have {ternary} {command.qualified_name}. Until this command is {ternary2}")'''


@client.command()
async def disable(ctx, *, command: str):
    # try:
    command = command.lower()
    command = client.get_command(command)
    if command is None:
        await ctx.message.reply("This command doesn't exist. Type `-help` to know what commands this bot has.")
        return
    elif ctx.command == command:
        await ctx.message.reply("You can't expect me to disable the command which helps disabling other commands ;-;")
        return
    else:
        guild_data = enableddisabled_db.find_one(
            {"guild_id": str(ctx.guild.id)})
        if guild_data is None:
            guild_data = {"guild_id": str(ctx.guild.id),
                          "disabled_commands": [str(command.name)]}
            enableddisabled_db.insert_one(guild_data)
            #command.enabled = False
            await ctx.message.reply(f"Successfully disabled `{command.name}`! None of the members in the server can use this command any more until the admin enables it again.")
            return

        elif str(command.name) in guild_data["disabled_commands"]:
            await ctx.message.reply(f"The command `{command.name}` has already been disabled.")
            return

        else:
            guild_data["disabled_commands"].append(str(command.name))
            enableddisabled_db.update_one(
                {"guild_id": str(ctx.guild.id)}, {"$set": guild_data})

            #command.enbled = False
            await ctx.message.reply(f"Successfully disabled `{command.name}`! None of the members in the server can use this command any more until the admin enables it again.")

    # except:


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
        im = Image.open
    except urllib.error.HTTPError:
        await ctx.message.reply("**Compilation Error❌**\nPlease check your input!")
        return
    '''Image = im.open("image.png")
    Image.resize((790, 200))'''

    #Image = Image.resize((200, 200))
    await ctx.message.reply(file=discord.File("image.png"))

    '''embed = discord.Embed(
        title="🎉Giveaway", description=f"{prize}", color=ctx.author.color)
    end = datetime.datetime.utcnow() +\
        datetime.timedelta(seconds=float(mins*60))
    embed.add_field(name="Ends At:", value=f"{end} UTC")
    embed.set_footer(text=f"Ends in {mins} from now!")

    my_msg = await ctx.send(embed=embed)
    await my_msg.add_reaction("🎉")
    time = int(mins)
    await asyncio.sleep(time)

    new_msg = await ctx.channel.fetch_message(my_msg.id)
    user = []
    for users in new_msg.reactions:
        user.append(users)

    # users = await new_msg.reactions.users().flatten()
    for i in user:
        if i == client.user.name:
            user.pop(user.index(i))
    list = list(x for x in user)      
    winner = random.choice()
    await ctx.send(f"Congrats {winner.mention}!! You won {prize}")'''


@client.command()
async def botinfo(ctx):
    servers = len(client.guilds)
    lst = []
    for i in client.guilds:
        lst.append(i.member_count)
    users = sum(lst)
    commands = len(client.commands)
    embed = discord.Embed(
        title=f"```{client.user.name}'s info```", color=ctx.author.color)
    embed.add_field(name="Made By:", value=f"```Sathya#6960```", inline=False)
    embed.add_field(name="Servers:", value=f"```{servers}```", inline=False)
    embed.add_field(name="Users:", value=f"```{users}```", inline=False)
    embed.add_field(name="Total No. of Commands:",
                    value=f"```{commands}```", inline=False)
    embed.set_image(url=client.user.avatar_url)
    await ctx.message.reply(embed=embed)


# client.ipc.start()
Token = 'ODQ0ODEzMzE2NTA1MDc1NzEy.G7ieKV.y_aglJJ30PBmlvtm6tFrl4SraF5ExLuCQyF3TQ'
client.run(Token)
