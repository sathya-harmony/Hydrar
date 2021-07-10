import discord
import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import asyncio
import random


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
            user = ctx.author
            embed = discord.Embed(
                title=f"{user}'s Avatar!", color=ctx.author.color, timestamp=ctx.message.created_at)
            embed.set_image(url=f"{user.avatar_url}")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title=f"{user}'s Avatar!", color=ctx.author.color, timestamp=ctx.message.created_at)
            embed.set_image(url=f"{user.avatar_url}")
            await ctx.send(embed=embed)

    @commands.command()
    async def pro(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        responses = ["Cogs/Pics/pro.jpg",
                     "Cogs/Pics/pro1.jpg", "Cogs/Pics/pro2.jpg", "Cogs/Pics/pro3.jpg", "Cogs/Pics/pro4.jpg", "Cogs/Pics/pro5.jpg", "Cogs/Pics/pro6.jpg"]

        img = Image.open(f'{random.choice(responses)}')
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

        font_size = 130
        cords = 445, 65
        font = ImageFont.truetype("fonts/Linotype.otf", font_size)
        text = user.display_name
        # 450,65
        # print(font.getsize(text)[0])
        while font.getsize(text)[0] >= 640:
            font_size -= 5
            cords = 410, 100
            if font_size <= 0:
                font_size = 10
                break

            font = ImageFont.truetype("fonts/Linotype.otf", font_size)

        draw_img.text((cords), text, (255, 255, 255), font=font)

        '''if (user.status) == discord.Status.online:

            online = Image.open("Cogs\Pics\OnlineStatus.png")
            online = online.resize((200, 200))
            img.paste(online, (500, 700))

        elif (user.status) == discord.Status.dnd:
            online = Image.open("Cogs\Pics\DNDStatus.png")
            online = online.resize((200, 200))
            img.paste(online, (500, 700))

        elif (user.status) == discord.Status.offline:
            online = Image.open("Cogs\Pics\DNDStatus.png")
            online = online.resize((200, 200))
            img.paste(online, (500, 700))

        with BytesIO() as buf:
            img.save(buf, format="jpeg")
            buf.seek(0)
            await ctx.send(file=discord.File(buf, f"Profile of {user.name}#{user.discriminator}.jpeg"))'''


def setup(client):
    client.add_cog(Wanted(client))
