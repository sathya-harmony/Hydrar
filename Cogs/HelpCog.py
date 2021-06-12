import discord
from discord.ext import commands
from discord import embeds
from discord.ext.commands.errors import ArgumentParsingError, InvalidEndOfQuotedStringError

prefix = '-'
client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      intents=discord.Intents.all())


@commands.Cog.listener()
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
                    name="**🏓Games**",
                    value="`-help Games`\n[Hover for Info](https://rb.gy/o2krdf)",
                    inline=False)
                await ctx.send(embed=embed1)
                return
            except:
                pass

        if arg == 'fun':
            embed2 = discord.Embed(
                title="😄Fun Commands",
                description="**Desciption:**\nShows the Fun Commands Category. \nHave fun using these commands! :smile:",
                color=ctx.author.color)
            embed2.set_thumbnail(
                url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
            )
            embed2.add_field(name="**Commands:**",
                             value="`8ball`, `ping`, `wanted`, `RIP`, `Chat`, `joke` ",
                             inline=False)

            embed2.add_field(name="**Aliases:**", value="fun", inline=False)

            embed2.add_field(name="**Usage:**",
                             value="`-help fun`",
                             inline=False)

            embed2.set_footer(
                text="Don't forget to use the prefix '-' before each command!",
                icon_url=embeds.EmptyEmbed)

            await ctx.send(embed=embed2)
            return

        if arg == 'moderation':
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

            await ctx.send(embed=embed3)
            return
        if arg == 'utility':
            embed4 = discord.Embed(
                title=":tools: Utility Commands",
                description="**Description:**\nShows the Utility Commands Category.\nUseful commands- Yes, you read it right, I am a useful bot. :rofl:",
                color=ctx.author.color)
            embed4.set_thumbnail(
                url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
            )
            embed4.add_field(
                name="**Commands:**",
                value="`Help`, `Server`, `Userinfo`, `Solve`, `Ask`, `Music`, `Search`, `Quote`",
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
            await ctx.send(embed=embed4)
            return

        if arg == 'currency':
            embed5 = discord.Embed(
                title=":tools: Currency Commands",
                description="**Description:**\nShows the Currency Commands Category.\nEarn Hydroids! :money_with_wings:\nHydroids: Hydrargyrum Currency :coin:",
                color=ctx.author.color)
            embed5.set_thumbnail(
                url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
            )
            embed5.add_field(name="**Commands:**",
                             value="(Launching Soon)",
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
            await ctx.send(embed=embed5)
            return
        if arg == 'games':
            embed6 = discord.Embed(
                title=":game_die: Game Commands",
                description="**Description:**\nShows the Game Commands Category.\nPlay some minigames solo, or with your friends :bowling:",
                color=ctx.author.color)
            embed6.set_thumbnail(
                url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
            )
            embed6.add_field(name="**Commands:**",
                             value="(Launching Soon)",
                             inline=False)
            embed6.add_field(name="**Aliases:**", value="games", inline=False)
            embed6.add_field(name="**Usage:**",
                             value="`-help games`",
                             inline=False)
            embed6.set_footer(
                text="Don't forget to use the prefix '-' before each command!",
                icon_url=embeds.EmptyEmbed)
            await ctx.send(embed=embed6)
            return
        # inside main function
        if arg == '8ball':
            embed7 = discord.Embed(
                title="8ball Info",
                description="**Description:**\nAsk the magic (and kinda rude) 8ball about your future!",
                color=ctx.author.color)
            embed7.set_thumbnail(
                url='https://media.giphy.com/media/pfquvHUjzmNbGBXHgA/giphy.gif'
            )

            embed7.add_field(name="**Usage:**",
                             value="`-help games`",
                             inline=False)
            embed7.add_field(name="**Aliases:**",
                             value="8ball, 8b",
                             inline=False)
            embed7.set_footer(
                text="Don't forget to use the prefix '-' before each command!",
                icon_url=embeds.EmptyEmbed)
            await ctx.send(embed=embed7)
            return


def setup(client):
    client.add_cog(_help(client))
