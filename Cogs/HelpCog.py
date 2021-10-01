import discord
from discord.ext import commands
from discord import embeds
from discord.ext.commands.errors import ArgumentParsingError, InvalidEndOfQuotedStringError
from discord_components import *
import ssl
import asyncio

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


class _help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='help',
                      aliases=["helpme", "command", "commands", "cmd", "cmds"])
    async def help(self, ctx, arg=''):
        arg = arg.lower()
        if arg == '':
            try:
                embed1 = discord.Embed(
                    title="Hydrargyrum - Command Categories",
                    description="*Use `-help` `command` for extended\ninformation on that command.*",
                    color=ctx.author.color)
                embed1.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )
                embed1.add_field(
                    name="**😄Fun**",
                    value="`-help Fun`\n[Hover for Info](https://rb.gy/o2krdf)",
                    inline=False)
                embed1.add_field(
                    name="**👮‍♂️Moderation**",
                    value="`-help Moderation`\n[Hover for Info](https://rb.gy/o2krdf)",
                    inline=False)

                embed1.add_field(
                    name="**🛠Utility**",
                    value="`-help Utility`\n[Hover for Info](https://rb.gy/o2krdf)",
                    inline=False)

                embed1.add_field(
                    name="**💰Currency**",
                    value="`-help Currency`\n[Hover for Info](https://rb.gy/o2krdf)",
                    inline=False)

                embed1.add_field(
                    name="**📊Levels**",
                    value="`-help Levels`\n[Hover for Info](https://rb.gy/o2krdf)",
                    inline=False)

                embed1.add_field(
                    name="**🏓Games**",
                    value="`-help Games`\n[Hover for Info](https://rb.gy/o2krdf)",
                    inline=False)
                # await ctx.message.reply(embed = embed1)
                await ctx.message.reply(embed=embed1, components=[Select(placeholder="Filter",
                                                                         options=[
                                                                             SelectOption(
                                                                                 label="😄 Fun",
                                                                                 value="fun",
                                                                                 description="Shows the Fun Commands Category!"

                                                                             ),
                                                                             SelectOption(
                                                                                 label="👮‍♂️ Moderation",
                                                                                 value="moderation",
                                                                                 description="Shows the Moderation Commands Category!"
                                                                             ),
                                                                             SelectOption(
                                                                                 label="🛠 Utility",
                                                                                 value="utility",
                                                                                 description="Shows the Utility Commands Category!"
                                                                             ),
                                                                             SelectOption(
                                                                                 label="💰 Economy",
                                                                                 value="economy",
                                                                                 description="Shows the Economy Commands Category!"
                                                                             ),
                                                                             SelectOption(
                                                                                 label="📊 Levels",
                                                                                 value="levels",
                                                                                 description="Shows the Levels Commands Catergory!"

                                                                             )

                                                                         ]
                                                                         )
                                                                  ]
                                        )
                interaction = await self.client.wait_for("button_click",
                                                         check=lambda i: i.component.label.startswith(
                                                             'Continue')
                                                         )
                await interaction.respond(content="LOL")
                return
            except:
                pass

        elif arg == 'fun':
            try:
                embed2 = discord.Embed(
                    title="😄Fun Commands",
                    description="**Desciption:**\nShows the Fun Commands Category. \nHave fun using these commands! :smile:",
                    color=ctx.author.color)
                embed2.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )
                embed2.add_field(name="**Commands:**",
                                 value="`8ball`, `ping`, `wanted`, `RIP`, `chat`, `joke`,`quote`, `fact`",
                                 inline=False)

                embed2.add_field(name="**Aliases:**",
                                 value="fun", inline=False)

                embed2.add_field(name="**Usage:**",
                                 value="`-help fun`",
                                 inline=False)

                embed2.set_footer(
                    text="Don't forget to use the prefix '-' before each command!",
                    icon_url=embeds.EmptyEmbed)

                await ctx.message.reply(embed=embed2)
                return
            except:
                pass

        elif arg == 'moderation':
            try:
                embed3 = discord.Embed(
                    title=":cop: Moderation Commands",
                    description="**Description:**\nShows the Moderation Commands Category.\nYou and I both need to have specific permissions to use these\ncommands :cop:",
                    color=ctx.author.color)
                embed3.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )
                embed3.add_field(name="**Commands:**",
                                 value="`Kick`, `Ban`,`Unban`, `Clear`",
                                 inline=False)

                embed3.add_field(name="**Aliases:**",
                                 value="Moderation",
                                 inline=False)

                embed3.add_field(name="**Usage:**",
                                 value="`-help moderation`",
                                 inline=False)

                embed3.set_footer(
                    text="Don't forget to use the prefix '-' before each command!",
                    icon_url=embeds.EmptyEmbed)

                await ctx.message.reply(embed=embed3)
                return
            except:
                pass
        elif arg == 'utility':
            try:
                embed4 = discord.Embed(
                    title=":tools: Utility Commands",
                    description="**Description:**\nShows the Utility Commands Category.\nUseful commands- Yes, you read it right, I am a useful bot. :rofl:",
                    color=ctx.author.color)
                embed4.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )
                embed4.add_field(
                    name="**Commands:**",
                    value="`Help`, `Server`, `Userinfo`, `Solve`, `Ask`",
                    inline=False)
                embed4.add_field(name="**Aliases:**",
                                 value="utility",
                                 inline=False)
                embed4.add_field(name="**Usage:**",
                                 value="`-help utility`",
                                 inline=False)
                embed4.set_footer(
                    text="Don't forget to use the prefix '-' before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed4)
                return
            except:
                pass

        elif arg == 'currency':
            try:
                embed5 = discord.Embed(
                    title=":tools: Currency Commands",
                    description="**Description:**\nShows the Currency Commands Category.\nEarn Hydroids! :money_with_wings:\nHydroids: Hydrargyrum Currency :coin:",
                    color=ctx.author.color)
                embed5.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )
                embed5.add_field(name="**Commands:**",
                                 value="`daily`, `withdraw`, `deposit`, `donate`, `balance`, `beg`, `bet`, `steal`, `shop`, `buy`, `inventory`, `use`, `sell`, `rich`",
                                 inline=False)
                embed5.add_field(name="**Aliases:**",
                                 value="currency",
                                 inline=False)
                embed5.add_field(name="**Usage:**",
                                 value="`-help currency`",
                                 inline=False)
                embed5.set_footer(
                    text="Don't forget to use the prefix '-' before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed5)

                return
            except:
                pass

        elif arg == 'level':
            try:
                embed6 = discord.Embed(
                    title="📊 levelling Commands",
                    description="**Description:**\nShows the Levelling Commands category.\nOur bot has a levelling system! You can view your levelling stats too and the person with the most xp!📉",
                    color=ctx.author.color)
                embed6.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )
                embed6.add_field(name="**Commands:**",
                                 value="`rank`, `top`",
                                 inline=False)
                embed6.add_field(name="**Aliases:**",
                                 value="level, levels, lvls, lvl",
                                 inline=False)
                embed6.add_field(name="**Usage:**",
                                 value="`-help levels`",
                                 inline=False)
                embed6.set_footer(
                    text="Don't forget to use the prefix '-' before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed6)
                return
            except:
                pass
        elif arg == 'games':
            try:
                embed7 = discord.Embed(
                    title=":game_die: Game Commands",
                    description="**Description:**\nShows the Game Commands Category.\nPlay some minigames solo, or with your friends :bowling:",
                    color=ctx.author.color)
                embed7.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )
                embed7.add_field(name="**Commands:**",
                                 value="(Launching Soon)",
                                 inline=False)
                embed7.add_field(name="**Aliases:**",
                                 value="games", inline=False)
                embed7.add_field(name="**Usage:**",
                                 value="`-help games",
                                 inline=False)
                embed7.set_footer(
                    text="Don't forget to use the prefix '-' before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed7)
                return
            except:
                pass
        while True:
            try:
                interact = await self.client.wait_for("select_option", timeout=15.0)
                value = interact.component.label
                if value == 'fun':
                    await interact.edit_origin(embed=embed2)

                '''if ctx.author.id != interact.author.id:
                    await interact.respond(content=f"{interaction.author.mention} This message is not for you lmao")'''
            except asyncio.TimeoutError:
                break
        # inside main function
        if arg == '8ball':
            try:
                embed8 = discord.Embed(
                    title="8ball Info",
                    description="**Description:**\nAsk the magic (and kinda rude) 8ball about your future!",
                    color=ctx.author.color)
                embed8.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed8.add_field(name="**Usage:**",
                                 value="`-8ball <question>`",
                                 inline=False)
                embed8.add_field(name="**Aliases:**",
                                 value="8ball, 8b",
                                 inline=False)
                embed8.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed8)
                return
            except:
                pass

        if arg == 'wanted':
            try:
                embed9 = discord.Embed(
                    title="Wanted Info",
                    description="**Description:**\nGet a person chased down by the cops! (by applying some posters lol)",
                    color=ctx.author.color)
                embed9.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed9.add_field(name="**Usage:**",
                                 value="`-wanted [member]`",
                                 inline=False)
                embed9.add_field(name="**Aliases:**",
                                 value="wanted",
                                 inline=False)
                embed9.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed9)
                return
            except:
                pass

        if arg == 'rip':
            try:
                embed10 = discord.Embed(
                    title="RIP Info",
                    description="**Description:**\nKill a person instantly! (this person will be remembered lol)",
                    color=ctx.author.color)
                embed10.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed10.add_field(name="**Usage:**",
                                  value="`-rip [member]`",
                                  inline=False)
                embed10.add_field(name="**Aliases:**",
                                  value="rip, Rip, RIP",
                                  inline=False)
                embed10.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed10)
                return
            except:
                pass

        if arg == 'chat':
            try:
                embed11 = discord.Embed(
                    title="Chat Info",
                    description="**Description:**\nChat with the smartest bot!(im srs lol, this bot is very smart)",
                    color=ctx.author.color)
                embed11.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed11.add_field(name="**Usage:**",
                                  value="`-chat <input>`",
                                  inline=False)
                embed11.add_field(name="**Aliases:**",
                                  value="Chat, chat",
                                  inline=False)
                embed11.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed11)
                return
            except:
                pass

        if arg == 'Ban':
            try:
                embed12 = discord.Embed(
                    title="Ban Info",
                    description="**Description:**\nBan someone from the server! (Only works if you have `Manage Members` permission. The person cannot join back the server until he is unbanned.)",
                    color=ctx.author.color)
                embed12.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed12.add_field(name="**Usage:**",
                                  value="`-ban <member> [reason]`",
                                  inline=False)
                embed12.add_field(name="**Aliases:**",
                                  value="ban",
                                  inline=False)
                embed12.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed12)
                return
            except:
                pass

        if arg == 'Kick':
            try:
                embed13 = discord.Embed(
                    title="Kick Info",
                    description="**Description:**\nkick someone from the server! (Only works if you have `Manage Members` permission. The person can join back the server with another invite link.)",
                    color=ctx.author.color)
                embed13.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed13.add_field(name="**Usage:**",
                                  value="`-kick <member> [reason]`",
                                  inline=False)
                embed13.add_field(name="**Aliases:**",
                                  value="kick",
                                  inline=False)
                embed13.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed13)
                return
            except:
                pass

        if arg == 'Unban':
            try:
                embed11 = discord.Embed(
                    title="Clear Info",
                    description="**Description:**\nUnban someone! (Only works if you have `Manage Members` permission. Only works when the member has already been banned and is in the ban list of the server.)",
                    color=ctx.author.color)
                embed11.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed11.add_field(name="**Usage:**",
                                  value="`-unban <member> [reason]`",
                                  inline=False)
                embed11.add_field(name="**Aliases:**",
                                  value="unban",
                                  inline=False)
                embed11.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed11)
                return
            except:
                pass

        if arg == 'clear':
            try:
                embed12 = discord.Embed(
                    title="Clear Info",
                    description="**Description:**\nClear any number of messages in the channel you're using the command in!(You need admin perms to use this command.)",
                    color=ctx.author.color)
                embed12.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed12.add_field(name="**Usage:**",
                                  value="**.** `-clear <amount>`\n**.** `-clear all`",
                                  inline=False)
                embed12.add_field(name="**Aliases:**",
                                  value="kick",
                                  inline=False)
                embed12.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed12)
                return
            except:
                pass

        if arg == 'Userinfo':
            try:
                embed13 = discord.Embed(
                    title="User Info",
                    description="**Description:**\nShows information on a mentioned user of the server.",
                    color=ctx.author.color)
                embed13.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed13.add_field(name="**Usage:**",
                                  value="`-about [member]`",
                                  inline=False)
                embed13.add_field(name="**Aliases:**",
                                  value="userinfo, about",
                                  inline=False)
                embed13.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed13)
                return
            except:
                pass

        if arg == 'ask':
            try:
                embed14 = discord.Embed(
                    title="User Info",
                    description="**Description:**\nThis bot can solve any question. May it be math, science ANYTHING(Just use ask command lol)",
                    color=ctx.author.color)
                embed14.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed14.add_field(name="**Usage:**",
                                  value="`-ask <question>`",
                                  inline=False)
                embed14.add_field(name="**Aliases:**",
                                  value="ask, solve",
                                  inline=False)
                embed14.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed12)
                return
            except:
                pass

        if arg == 'daily':
            try:
                embed14 = discord.Embed(
                    title="Daily Info",
                    description="**Description:**\nCollect your daily coins. You earn more if your streak is higher!",
                    color=ctx.author.color)
                embed14.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed14.add_field(name="**Usage:**",
                                  value="`-ask <question>`",
                                  inline=False)
                embed14.add_field(name="**Aliases:**",
                                  value="ask, solve",
                                  inline=False)
                embed14.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed12)
                return
            except:
                pass


def setup(client):
    client.add_cog(_help(client))
