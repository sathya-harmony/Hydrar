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
    async def help(self, ctx):

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

        while True:
            try:
                interact = await self.client.wait_for("select_option", timeout=15.0)
                value = interact.component.value
                if value == 'fun':
                    await interact.edit_origin(embed=embed2)
            except asyncio.TimeoutError:
                break


def setup(client):
    client.add_cog(_help_(client))
