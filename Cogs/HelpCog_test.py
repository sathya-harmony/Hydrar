import discord
from discord.ext import commands
from discord import embeds
from discord.ext.commands.errors import ArgumentParsingError, InvalidEndOfQuotedStringError
from discord_components import *
import ssl
import asyncio


class _help_(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='help',
                      aliases=["helpme", "command", "commands", "cmd", "cmds"])
    async def help(self, ctx, arg=''):

        embed1 = discord.Embed(
            title="Hydrargyrum - Command Categories",
            description="*Use `-help` `command` for extended\ninformation on that command.*",
            color=ctx.author.color)
        embed1.set_thumbnail(
            url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
        )
        embed1.add_field(
            name="**😄Fun**",
            value="`Use the filter below!`\n[Hover for Info](https://rb.gy/o2krdf)",
            inline=False)
        embed1.add_field(
            name="**👮‍♂️Moderation**",
            value="`Use the filter below!`\n[Hover for Info](https://rb.gy/o2krdf)",
            inline=False)

        embed1.add_field(
            name="**🛠Utility**",
            value="`Use the filter below!`\n[Hover for Info](https://rb.gy/o2krdf)",
            inline=False)

        embed1.add_field(
            name="**💰Currency**",
            value="`Use the filter below!`\n[Hover for Info](https://rb.gy/o2krdf)",
            inline=False)

        embed1.add_field(
            name="**📊Levels**",
            value="`Use the filter below!`\n[Hover for Info](https://rb.gy/o2krdf)",
            inline=False)

        embed1.add_field(
            name="**✉️Invite**",
            value="`Use the filter below!`\n[Hover for Info](https://rb.gy/o2krdf)",
            inline=False)

        '''embed1.add_field(
            name="**🏓Games**",
            value="`Use the filter below!`\n[Hover for Info](https://rb.gy/o2krdf)",
            inline=False)'''
        # await ctx.message.reply(embed = embed1)

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

        embed3 = discord.Embed(
            title=":cop: Moderation Commands",
            description="**Description:**\nShows the Moderation Commands Category.\nYou and I both need to have specific permissions to use these\ncommands :cop:",
            color=ctx.author.color)
        embed3.set_thumbnail(
            url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
        )
        embed3.add_field(name="**Commands:**",
                         value="`Kick`, `Ban`,`Unban`, `Clear`, `Mute`, `Unmute`",
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

        embed4 = discord.Embed(
            title=":tools: Utility Commands",
            description="**Description:**\nShows the Utility Commands Category.\nUseful commands- Yes, you read it right, I am a useful bot. :rofl:",
            color=ctx.author.color)
        embed4.set_thumbnail(
            url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
        )
        embed4.add_field(
            name="**Commands:**",
            value="`Help`, `Server`, `Userinfo`,`Ask`, `Changeprefix`",
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

        embed5 = discord.Embed(
            title=":tools: Currency Commands",
            description="**Description:**\nShows the Currency Commands Category.\nEarn Hydroids! :money_with_wings:\nHydroids: Hydrargyrum Currency :coin:",
            color=ctx.author.color)
        embed5.set_thumbnail(
            url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
        )
        embed5.add_field(name="**Commands:**",
                         value="`daily`, `withdraw`, `deposit`, `donate`, `balance`, `beg`, `bet`, `steal`, `shop`, `buy`, `inventory`, `use`, `sell`, `rich`, `worklist`, `work`",
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

        embed6 = discord.Embed(
            title="📊 levelling Commands",
            description="**Description:**\nShows the Levelling Commands category.\nOur bot has a levelling system! You can view your levelling stats too and the person with the most xp!📉",
            color=ctx.author.color)
        embed6.set_thumbnail(
            url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
        )
        embed6.add_field(name="**Commands:**",
                         value="`rank`, `top`, `setlevelchannel`",
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

        embedinvite = discord.Embed(
            title="✉️ Invite the bot!", description="Loving the bot? Support us by inviting the bot to any server right now! Click the button below to invite the bot ♥")

        components = [Select(placeholder="Filter",
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

                                 ),
                                 SelectOption(
                                     label="✉️ Invite",
                                     value="invite",
                                     description="Invite the bot to other servers!!")

                             ]
                             )
                      ]

        if arg == '':

            message = await ctx.message.reply(embed=embed1, components=components)

            while True:
                try:
                    interaction = await self.client.wait_for("select_option", timeout=20.0)
                    if ctx.author.id != interaction.author.id:
                        await interaction.respond(content="This message ain't for you LOL")
                    value = interaction.values[0]
                    if value == 'fun':
                        await interaction.edit_origin(embed=embed2, components=[Select(placeholder="😄 Fun Commands",
                                                                                       options=[
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

                                                                                           ),
                                                                                           SelectOption(
                                                                                               label="✉️ Invite",
                                                                                               value="invite",
                                                                                               description="Invite the bot to other servers!!"),
                                                                                           SelectOption(
                                                                                               label="🏡 Home",
                                                                                               value="home",
                                                                                               description="Return to the main help page!")


                                                                                       ]
                                                                                       )])

                    elif value == 'moderation':
                        await interaction.edit_origin(embed=embed3, components=[Select(placeholder="👮‍♂️ Moderation",
                                                                                       options=[
                                                                                           SelectOption(
                                                                                               label="😄 Fun",
                                                                                               value="fun",
                                                                                               description="Shows the Fun Commands Category!"

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

                                                                                           ),
                                                                                           SelectOption(
                                                                                               label="✉️ Invite",
                                                                                               value="invite",
                                                                                               description="Invite the bot to other servers!!"),
                                                                                           SelectOption(
                                                                                               label="🏡 Home",
                                                                                               value="home",
                                                                                               description="Return to the main help page!")


                                                                                       ]
                                                                                       )])

                    elif value == 'utility':
                        await interaction.edit_origin(embed=embed4, components=[Select(placeholder="🛠 Utility",
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
                                                                                               label="💰 Economy",
                                                                                               value="economy",
                                                                                               description="Shows the Economy Commands Category!"
                                                                                           ),
                                                                                           SelectOption(
                                                                                               label="📊 Levels",
                                                                                               value="levels",
                                                                                               description="Shows the Levels Commands Catergory!"

                                                                                           ),
                                                                                           SelectOption(
                                                                                               label="✉️ Invite",
                                                                                               value="invite",
                                                                                               description="Invite the bot to other servers!!"),
                                                                                           SelectOption(
                                                                                               label="🏡 Home",
                                                                                               value="home",
                                                                                               description="Return to the main help page!")


                                                                                       ]
                                                                                       )])
                    elif value == 'economy':
                        await interaction.edit_origin(embed=embed5, components=[Select(placeholder="💰 Economy",
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
                                                                                               label="📊 Levels",
                                                                                               value="levels",
                                                                                               description="Shows the Levels Commands Catergory!"

                                                                                           ),
                                                                                           SelectOption(
                                                                                               label="✉️ Invite",
                                                                                               value="invite",
                                                                                               description="Invite the bot to other servers!!"),
                                                                                           SelectOption(
                                                                                               label="🏡 Home",
                                                                                               value="home",
                                                                                               description="Return to the main help page!")


                                                                                       ]
                                                                                       )])
                    elif value == 'levels':
                        await interaction.edit_origin(embed=embed6, components=[Select(placeholder="📊 Levels",
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
                                                                                               label="✉️ Invite",
                                                                                               value="invite",
                                                                                               description="Invite the bot to other servers!!"),
                                                                                           SelectOption(
                                                                                               label="🏡 Home",
                                                                                               value="home",
                                                                                               description="Return to the main help page!")


                                                                                       ]
                                                                                       )])
                    elif value == 'home':
                        await interaction.edit_origin(embed=embed1, components=[Select(placeholder="🏡 Home",
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

                                                                                           ),
                                                                                           SelectOption(
                                                                                               label="✉️ Invite",
                                                                                               value="invite",
                                                                                               description="Invite the bot to other servers!!")


                                                                                       ]
                                                                                       )])
                    elif value == 'invite':
                        await interaction.edit_origin(embed=embedinvite, components=[(Button(style=ButtonStyle.URL, label="🔗 Invite the bot!", url="https://discord.com/api/oauth2/authorize?client_id=844813316505075712&permissions=8&scope=bot"))])

                except asyncio.TimeoutError:
                    await message.edit(components=[Select(placeholder="Timed Out", options=[
                        SelectOption(
                            label="😄 Fun",
                            value="fun",
                            description="Shows the Fun Commands Category!"

                        )], disabled=True)])

                    break
        arg = arg.lower()

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

        if arg == 'ban':
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

        if arg == 'kick':
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

        if arg == 'unban':
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
        if arg == 'mute':
            try:
                embed16 = discord.Embed(
                    title="Mute Info",
                    description="**Description:**\nPrevent a person from chatting or entering a voice channel!(You need admin perms to use this command.)",
                    color=ctx.author.color)
                embed16.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed16.add_field(name="**Usage:**",
                                  value="**.** `-mute <member>`",
                                  inline=False)
                embed16.add_field(name="**Aliases:**",
                                  value="mute",
                                  inline=False)
                embed16.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed16)
                return
            except:
                pass
        if arg == 'unmute':
            try:
                embed17 = discord.Embed(
                    title="Unmute Info",
                    description="**Description:**\nAllow a person who has already been muted, to talk and enter in voice channels!(You need admin perms to use this command.)",
                    color=ctx.author.color)
                embed17.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed17.add_field(name="**Usage:**",
                                  value="`-unmute <member>`",
                                  inline=False)
                embed17.add_field(name="**Aliases:**",
                                  value="unmute",
                                  inline=False)
                embed17.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed17)
                return
            except:
                pass

        if arg == 'userinfo':
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
                await ctx.message.reply(embed=embed14)
                return
            except:
                pass
        if arg == 'changeprefix':
            try:
                embed18 = discord.Embed(
                    title="Change Prefix Info",
                    description="**Description:**\nChange the prefix of the bot!\n Does this bot's prefix default prefix `-` the same as another bot's? No worries, you can add custom prefixes!",
                    color=ctx.author.color)
                embed18.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed18.add_field(name="**Usage:**",
                                  value="`-changeprefix <prefix>`",
                                  inline=False)
                embed18.add_field(name="**Aliases:**",
                                  value="changeprefix",
                                  inline=False)
                embed18.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed18)
                return
            except:
                pass

        if arg == 'daily':
            try:
                embed15 = discord.Embed(
                    title="Daily Info",
                    description="**Description:**\nCollect your daily coins. You earn more if your streak is higher!(Economy Command)",
                    color=ctx.author.color)
                embed15.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed15.add_field(name="**Usage:**",
                                  value="`-daily`",
                                  inline=False)
                embed15.add_field(name="**Aliases:**",
                                  value="daily",
                                  inline=False)
                embed15.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed15)
                return
            except:
                pass
        if arg == 'withdraw':
            try:
                embed19 = discord.Embed(
                    title="Withdraw Info",
                    description="**Description:**\nWithdraw any amount from your bank to your wallet! Hint: The money present in your wallet can be easily robbed! (Economy Command)",
                    color=ctx.author.color)
                embed19.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed19.add_field(name="**Usage:**",
                                  value="**.** `-with <amount>`\n**.** `-with all`",
                                  inline=False)
                embed19.add_field(name="**Aliases:**",
                                  value="withdraw, with",
                                  inline=False)
                embed19.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed19)
                return
            except:
                pass

        if arg == 'deposit':
            try:
                embed20 = discord.Embed(
                    title="Deposit Info",
                    description="**Description:**\nDeposit an amount less than or equal to the bank space from your wallet to your bank! Hint: The money present in your bank cannot be touched by robbers! (Economy Command)",
                    color=ctx.author.color)
                embed20.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed20.add_field(name="**Usage:**",
                                  value="**.** `-dep <amount>`\n**.** `-dep all`",
                                  inline=False)
                embed20.add_field(name="**Aliases:**",
                                  value="deposit, dep",
                                  inline=False)
                embed20.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed20)
                return
            except:
                pass

        if arg == 'balance':
            try:
                embed22 = discord.Embed(
                    title="Balance Info",
                    description="**Description:**\nCheck your balance! Shows wallet balance, bank balance, and bank space! (Economy Command)",
                    color=ctx.author.color)
                embed22.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed22.add_field(name="**Usage:**",
                                  value="`-bal`",
                                  inline=False)
                embed22.add_field(name="**Aliases:**",
                                  value="bal, balance",
                                  inline=False)
                embed22.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed22)
                return
            except:
                pass

        if arg == 'beg':
            try:
                embed23 = discord.Embed(
                    title="Beg Info",
                    description="**Description:**\nBeg some money from random people!(Economy Command)",
                    color=ctx.author.color)
                embed23.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed23.add_field(name="**Usage:**",
                                  value="`-beg`",
                                  inline=False)
                embed23.add_field(name="**Aliases:**",
                                  value="beg",
                                  inline=False)
                embed23.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed23)
                return
            except:
                pass

        if arg == 'slots':
            try:
                embed24 = discord.Embed(
                    title="Slots Info",
                    description="**Description:**\nSpin a slot machine after investing some money! You may win or lose money according to your luck!(Economy Command)",
                    color=ctx.author.color)
                embed24.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed24.add_field(name="**Usage:**",
                                  value="`-slots <amount>`",
                                  inline=False)
                embed24.add_field(name="**Aliases:**",
                                  value="slots",
                                  inline=False)
                embed24.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed24)
                return
            except:
                pass

        if arg == 'steal' or arg == 'rob':
            try:
                embed25 = discord.Embed(
                    title="Steal Info",
                    description="**Description:**\nLike robbing people? Then this command is for you. Rob anyone you like. You getting caught by cops or successfully robbing the money is based on luck(Economy Command)",
                    color=ctx.author.color)
                embed25.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed25.add_field(name="**Usage:**",
                                  value="`-rob <member>`",
                                  inline=False)
                embed25.add_field(name="**Aliases:**",
                                  value="rob, steal",
                                  inline=False)
                embed25.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed25)
                return
            except:
                pass

        if arg == 'shop':
            try:
                embed26 = discord.Embed(
                    title="Shop Info",
                    description="**Description:**\nSee the items that can be bought! Buy anything from the shop obio if you have money(Economy Command)",
                    color=ctx.author.color)
                embed26.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed26.add_field(name="**Usage:**",
                                  value="`-shop`",
                                  inline=False)
                embed26.add_field(name="**Aliases:**",
                                  value="shop",
                                  inline=False)
                embed26.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed26)
                return
            except:
                pass

        if arg == 'buy':
            try:
                embed27 = discord.Embed(
                    title="Buy Info",
                    description="**Description:**\nBuy any item from the shop!(Economy Command)",
                    color=ctx.author.color)
                embed27.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed27.add_field(name="**Usage:**",
                                  value="`-buy <quantity> <item>`",
                                  inline=False)
                embed27.add_field(name="**Aliases:**",
                                  value="buy",
                                  inline=False)
                embed27.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed27)
                return
            except:
                pass

        if arg == 'inventory' or arg == 'inv':
            try:
                embed28 = discord.Embed(
                    title="Inventory Info",
                    description="**Description:**\nSee the items that you have bought!(Economy Command)",
                    color=ctx.author.color)
                embed28.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed28.add_field(name="**Usage:**",
                                  value="`-inv`",
                                  inline=False)
                embed28.add_field(name="**Aliases:**",
                                  value="inventory, bag, inv",
                                  inline=False)
                embed28.set_footer(
                    text=f"`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed28)
                return
            except:
                pass

        if arg == 'use':
            try:
                embed29 = discord.Embed(
                    title="Use Info",
                    description="**Description:**\nStart using an item and remove it from your inventory. This will add it your active items list. (Only for items which h've been bought)(Economy Command)",
                    color=ctx.author.color)
                embed29.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed29.add_field(name="**Usage:**",
                                  value="`-use [quantity] <item>`",
                                  inline=False)
                embed29.add_field(name="**Aliases:**",
                                  value="use",
                                  inline=False)
                embed29.set_footer(
                    text=f"`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed29)
                return
            except:
                pass

        if arg == 'sell':
            try:
                embed30 = discord.Embed(
                    title="Sell Info",
                    description="**Description:**\nSell an item from you inventory! Sell anytime! Obio the money you get for selling the item is lesser than for what it was bought.(Only for items which h've been bought)(Economy Command)",
                    color=ctx.author.color)
                embed30.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed30.add_field(name="**Usage:**",
                                  value="`-sell [quantity] <item>`",
                                  inline=False)
                embed30.add_field(name="**Aliases:**",
                                  value="sell",
                                  inline=False)
                embed30.set_footer(
                    text=f"`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed30)
                return
            except:
                pass

        if arg == 'rich' or arg == 'wealthy':
            try:
                embed30 = discord.Embed(
                    title="Rich Info",
                    description="**Description:**\nSee the richest people in the server where the command is invoked!(Shows the net-worth that is the total of wallet and bank money!)(Economy Command)",
                    color=ctx.author.color)
                embed30.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed30.add_field(name="**Usage:**",
                                  value="`-rich`",
                                  inline=False)
                embed30.add_field(name="**Aliases:**",
                                  value="rich, wealthy",
                                  inline=False)
                embed30.set_footer(
                    text=f"`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed30)
                return
            except:
                pass

        if arg == 'worklist' or arg == 'work list':
            try:
                embed30 = discord.Embed(
                    title="Work List Info",
                    description="**Description:**\nSee the list of jobs which you can be employed for!(Economy Command)",
                    color=ctx.author.color)
                embed30.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed30.add_field(name="**Usage:**",
                                  value="`-worklist`",
                                  inline=False)
                embed30.add_field(name="**Aliases:**",
                                  value="worklist",
                                  inline=False)
                embed30.set_footer(
                    text=f"`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed30)
                return
            except:
                pass

        if arg == 'work':
            try:
                embed30 = discord.Embed(
                    title="Work Info",
                    description="**Description:**\nWork and get rewarded some Hydroids! `-work resign` to resign from your current job, `-work <job>` to apply to a job and `-work` to work for your current job(Economy Command)",
                    color=ctx.author.color)
                embed30.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed30.add_field(name="**Usage:**",
                                  value="**.** `-work`\n**.** `-work resign`\n**.** `-work <job>`\n",
                                  inline=False)
                embed30.add_field(name="**Aliases:**",
                                  value="work",
                                  inline=False)
                embed30.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed30)
                return
            except:
                pass

        if arg == 'rank' or arg == 'lvl' or arg == 'level':
            try:
                embed30 = discord.Embed(
                    title="Rank Info",
                    description="**Description:**\nEverytime you send a message, you gain some XP. Wanna see this XP beautifully compiled into a card? This command is for you then!(Levelling Command)",
                    color=ctx.author.color)
                embed30.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed30.add_field(name="**Usage:**",
                                  value="`-lvl`",
                                  inline=False)
                embed30.add_field(name="**Aliases:**",
                                  value="lvl, rank, level",
                                  inline=False)
                embed30.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed30)
                return
            except:
                pass

        if arg == 'top' or arg == "lb" or arg == 'leaderboard':
            try:
                embed30 = discord.Embed(
                    title="Leaderboard(XP) Info",
                    description="**Description:**\nEverytime you send a message, you gain some XP. Wanna see the people with most XP in YOUR server? This command is for you!(Levelling Command)",
                    color=ctx.author.color)
                embed30.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed30.add_field(name="**Usage:**",
                                  value="`-top`",
                                  inline=False)
                embed30.add_field(name="**Aliases:**",
                                  value="top, lb, leaderboard",
                                  inline=False)
                embed30.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed30)
                return
            except:
                pass

        if arg == 'setlevelchannel':
            try:
                embed30 = discord.Embed(
                    title="Set Level Channel Info",
                    description="**Description:**\nEverytime you send a message, you gain some XP. Everytime you hit a mark, the bot will send a congratulating message! If you wanna send this message in custom channels, use this command!(Levelling Command)",
                    color=ctx.author.color)
                embed30.set_thumbnail(
                    url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
                )

                embed30.add_field(name="**Usage:**",
                                  value="`-setlevelchannel <channel_id>`",
                                  inline=False)
                embed30.add_field(name="**Aliases:**",
                                  value="setlevelchannel",
                                  inline=False)
                embed30.set_footer(
                    text="`<>` is compuslory. `[]` is optional. Don't forget to use the prefix `-` before each command!",
                    icon_url=embeds.EmptyEmbed)
                await ctx.message.reply(embed=embed30)
                return
            except:
                pass


def setup(client):
    client.add_cog(_help_(client))
