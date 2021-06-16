import discord
import os
from PIL import Image, ImageDraw
from io import BytesIO
import asyncio


from discord.ext import commands
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


class Wanted(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open("Cogs/Pics/Wanted.jpg")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((328, 321))
        wanted.paste(pfp, (122, 251))
        wanted.save("ReturnPICS/profile.jpg")
        await ctx.send(file=discord.File("ReturnPICS/profile.jpg"))

    @commands.command()
    async def rip(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        rip = Image.open("Cogs/Pics/RIP.jpg")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((142, 125))
        rip.paste(pfp, (81, 145))
        rip.save("ReturnPICS/rip.jpg")
        await ctx.send(file=discord.File("ReturnPICS/rip.jpg"))

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send("Mention somebody to get their Avatar.")

        else:
            embed = discord.Embed(
                title=f"{user}'s Avatar!", color=ctx.author.color, timestamp=ctx.message.created_at)
            embed.set_image(url=f"{user.avatar_url}")
            await ctx.send(embed=embed)

    @commands.command()
    async def pro(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        '''im = Image.open("Cogs/Pics/pro.jpg")
        d = ImageDraw.Draw(im)

        west_north = (150, 50)
        east_south = (250, 150)

        outline_color = (255, 255, 255)

        d.ellipse([west_north, east_south], outline=outline_color, width=50)

        im.save("ReturnPICS/drawn_grid.png")

        pro = Image.open("Cogs/Pics/pro.jpg")
        asset = user.avatar_url_as(size=1024)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((300, 300))
        #pro.paste(pfp, (81, 145))
        # ReturnPICS/pro.jpg
        pro.save("ReturnPICS/pro.jpg")
        await ctx.send(file=discord.File("ReturnPICS/pro.jpg"))'''

        img = Image.open('Cogs/Pics/pro.jpg')
        draw_img = ImageDraw.Draw(img)

        # Left, Top, Right, Bottom
        # start_x, start_y, end_x, end_y
        pfp_coords = (81, 145, 81+300, 145+300)

        pfp_lum_img = Image.new(size=(
            pfp_coords[2]-pfp_coords[0], pfp_coords[3]-pfp_coords[1]), mode="L", color="black")
        draw_pfp_lum_img = ImageDraw.Draw(pfp_lum_img)
        draw_pfp_lum_img.ellipse((0, 0) + pfp_lum_img.size, fill="white")

        asset = user.avatar_url_as(size=1024)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize(pfp_lum_img.size)
        img.paste(pfp, pfp_coords[:2], mask=pfp_lum_img)
        draw_img.ellipse(pfp_coords, outline="white", width=8)

        with BytesIO() as buf:
            img.save(buf, format="jpeg")
            buf.seek(0)
            await ctx.send(file=discord.File(buf, f"Profile of {user.name}#{user.discriminator}.jpeg"))


def setup(client):
    client.add_cog(Wanted(client))
