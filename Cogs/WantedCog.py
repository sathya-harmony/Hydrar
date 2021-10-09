import discord
import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import asyncio
import random
from discord.utils import get
from discord_components.dpy_overrides import fetch_message
from pymongo import MongoClient


from discord.ext import commands
cluster = MongoClient(
    "mongodb+srv://Hydra:CihVirus123@economy.2xn9e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


Extras_MongoDB = cluster["Extras"]["Extras"]
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


def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk


@commands.Cog.listener()
async def on_message(self, message):
    user_data = self.get_extra_data(message.author.id)
    if message.author.id in user_data.keys():
        user_data.pop(message.author.id)
        try:
            await message.author.edit(nick=remove(message.author.display_name))

        except:
            pass
        await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK!")
    for id, reason in user_data.items():
        member = get(member.guild.members, id=id)
        if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
            await message.reply(f"{member.name} is AFK. AFK Note: {reason}")


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
        await ctx.message.reply(file=discord.File("ReturnPICS/profile.jpg"))

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
        await ctx.message.reply(file=discord.File("ReturnPICS/rip.jpg"))

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
            embed = discord.Embed(
                title=f"{user}'s Avatar!", color=ctx.author.color, timestamp=ctx.message.created_at)
            embed.set_image(url=f"{user.avatar_url}")
            await ctx.message.reply(embed=embed)

        else:
            embed = discord.Embed(
                title=f"{user}'s Avatar!", color=ctx.author.color, timestamp=ctx.message.created_at)
            embed.set_image(url=f"{user.avatar_url}")
            await ctx.message.reply(embed=embed)

    @commands.command()
    async def pro(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        responses = ["Cogs/Pics/pro.jpg",
                     "Cogs/Pics/pro1.jpg", "Cogs/Pics/pro2.jpg", "Cogs/Pics/pro3.jpg", "Cogs/Pics/pro4.jpg", "Cogs/Pics/pro5.jpg", "Cogs/Pics/pro6.jpg"]

        img = Image.open(random.choice(responses))
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

        if (user.status) is discord.Status.online:

            online = Image.open("Cogs/Pics/OnlineStatus.png")
            online = online.resize((75, 75))
            img.paste(online, (300, 340), mask=online)

        elif (user.status) is discord.Status.dnd:
            online = Image.open("Cogs/Pics/DNDStatus.png")
            online = online.resize((75, 75))
            img.paste(online, (300, 340), mask=online)

            #print("here", img.size)

        elif (user.status) is discord.Status.idle:
            online = Image.open("Cogs/Pics/IdleStatus.png")
            online = online.resize((75, 75))
            img.paste(online, (300, 340), mask=online)

        elif (user.status) is discord.Status.offline:
            online = Image.open("Cogs/Pics/OfflineStatus.png")
            online = online.resize((75, 75))
            img.paste(online, (300, 340), mask=online)

        with BytesIO() as buf:
            img.save(buf, format="png")
            buf.seek(0)
            await ctx.message.reply(file=discord.File(buf, f"Profile of {user.name}#{user.discriminator}.png"))

    def get_extra_data(self, user_id):

        if type(user_id) in [int, float]:
            user_id = str(int(user_id))

        guild_data = Extras_MongoDB.find_one(
            {"users": user_id})

        return guild_data

    @commands.command()
    async def afk(self, ctx, *, reason="No reason provided"):
        user_data = self.get_extra_data(ctx.author.id)
        member = ctx.author
        if user_data is None:
            user_data = {}
        if member.id in user_data.keys():
            user_data.pop(member.id)

        else:
            try:
                user_data[member.id] = reason
                member.edit(nick=f"[AFK] {member.display_name}")
            except:
                pass

        embed = discord.embed(
            title=":zzz: Member AFK", description=f"{member.mention} has gone **AFK**", color=member.color)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(name=self.client.user.name,
                         icon_url=self.client.user.avatar_url)
        embed.add_field(name='AFK Note:', value=reason)
        await ctx.message.reply(embed=embed)


def setup(client):
    client.add_cog(Wanted(client))
