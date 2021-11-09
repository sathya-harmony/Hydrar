import discord

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO
import io

import random
#from discord.utils import get
#from discord_components.dpy_overrides import fetch_message
#from pymongo import MongoClient

from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions

from modules.common import *
import aiohttp
from petpetgif import petpet as petpetgif
import requests
import urllib

#from discord_slash import cog_ext
# cluster = MongoClient(
#     "mongodb+srv://Hydra:CihVirus123@economy.2xn9e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


Extras_MongoDB = cluster["Extras"]["Extras"]


class Wanted(commands.Cog):

    afk_users_cache = dict()  # {123456789: 'reason'}
    newly_added_afk_users = []

    def __init__(self, client):
        self.client = client

        for item in Extras_MongoDB.find():
            self.afk_users_cache[item['user_id']] = item['reason']

    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open("Cogs/Pics/Wanted.jpg").convert("RGB")
        user_avatar_image = str(user.avatar_url_as(format='jpg', size=4096))
        async with aiohttp.ClientSession() as Session:
            async with Session.get(user_avatar_image) as resp:
                avatar_bytes = io.BytesIO(await resp.read())
        ava = Image.open(avatar_bytes)
        ava = ava.resize((330, 321))
        wanted.paste(ava, (120, 254))
        wanted.save("wanted.jpg")
        await ctx.message.reply(file=discord.File("wanted.jpg"))

    @commands.command()
    async def deleted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        delete = Image.open("Cogs/Pics/Delete.png")
        user_avatar_image = str(user.avatar_url_as(format='png', size=4096))
        async with aiohttp.ClientSession() as Session:
            async with Session.get(user_avatar_image) as resp:
                avatar_bytes = io.BytesIO(await resp.read())

        ava = Image.open(avatar_bytes)
        ava = ava.resize((200, 195))
        delete.paste(ava, (120, 135))
        delete.save("delete.png")
        await ctx.message.reply(file=discord.File("delete.png"))

    @commands.command()
    async def rip(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        rip = Image.open("Cogs/Pics/RIP.jpg").convert('RGB')
        user_avatar_image = str(user.avatar_url_as(format='jpg', size=4096))
        async with aiohttp.ClientSession() as Session:
            async with Session.get(user_avatar_image) as resp:
                avatar_bytes = io.BytesIO(await resp.read())
        ava = Image.open(avatar_bytes)
        ava = ava.resize((142, 125))
        rip.paste(ava, (80, 150))
        rip.save("image.jpg")
        await ctx.message.reply(file=discord.File("image.jpg"))

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
    async def pet(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        user_avatar_image = str(user.avatar_url_as(format='png', size=4096))
        async with aiohttp.ClientSession() as Session:
            async with Session.get(user_avatar_image) as resp:
                img1 = io.BytesIO(await resp.read())

        source = img1  # file-like container to hold the emoji in memory
        dest = BytesIO()  # container to store the petpet gif in memory
        petpetgif.make(source, dest)
        # set the file pointer back to the beginning so it doesn't upload a blank file.
        dest.seek(0)

        await ctx.send(file=discord.File(dest, filename=f"petpet.gif"))

    @commands.command(aliases=["russian", "communism"])
    async def communist(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        #user_avatar_image = user.avatar_url_as(format='png', size=4096)

        response = requests.get(user.avatar_url)

        avatar = Image.open(BytesIO(response.content))
        img1 = avatar.convert('RGBA').resize((300, 300))
        img2 = Image.open('Cogs/Pics/communism.gif')
        img1.putalpha(96)

        out = []
        for i in range(0, img2.n_frames):
            img2.seek(i)
            f = img2.copy().convert('RGBA').resize((300, 300))
            f.paste(img1, (0, 0), img1)
            out.append(f.resize((256, 256)))

        out[0].save("lmao.gif", format='gif', save_all=True, append_images=out[1:],
                    loop=0, disposal=2, optimize=True, duration=40)
        img2.close()
        # b.seek(0)
        await ctx.message.reply(file=discord.File("lmao.gif"))

    @commands.command()
    async def airpods(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        #user_avatar_image = user.avatar_url_as(format='png', size=4096)
        async with ctx.typing():
            blank = Image.new('RGBA', (400, 128), (255, 255, 255, 0))
            response = requests.get(user.avatar_url)

            avatar = Image.open(BytesIO(response.content))
            avatar = avatar.convert('RGBA').resize((128, 128))
            urllib.request.urlretrieve(
                f"https://github.com/DankMemer/imgen/blob/master/assets/airpods/left.gif?raw=true", "leftairpods.png")
            urllib.request.urlretrieve(
                f"https://github.com/DankMemer/imgen/blob/master/assets/airpods/right.gif?raw=true", "rightairpods.png")
            right = Image.open("rightairpods.png")
            left = Image.open("leftairpods.png")
            out = []
            for i in range(0, left.n_frames):
                left.seek(i)
                right.seek(i)
                f = blank.copy().convert('RGBA')
                l = left.copy().convert('RGBA')
                r = right.copy().convert('RGBA')
                f.paste(l, (0, 0), l)
                f.paste(avatar, (136, 0), avatar)
                f.paste(r, (272, 0), r)
                out.append(f.resize((400, 128), Image.LANCZOS).convert('RGBA'))

            out[0].save("airpods.gif", format='gif', save_all=True, append_images=out[1:], loop=0, disposal=2, optimize=True,
                        duration=30, transparency=0)
            await ctx.message.reply(file=discord.File("airpods.gif"))

    @commands.command()
    async def deepfry(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        #user_avatar_image = user.avatar_url_as(format='png', size=4096)
        async with ctx.typing():
            response = requests.get(user.avatar_url)
            avatar = Image.open(BytesIO(response.content))
            avatar = avatar.convert('RGBA').resize((400, 400))
            hundred = urllib.request.urlretrieve(
                f"https://github.com/DankMemer/imgen/blob/master/assets/deepfry/100.bmp", "100.bmp")
            fire = urllib.request.urlretrieve(
                f"https://github.com/DankMemer/imgen/blob/master/assets/deepfry/fire.bmp", "fire.bmp")
            joy = urllib.request.urlretrieve(
                f"https://github.com/DankMemer/imgen/blob/master/assets/deepfry/joy.bmp", "joy.bmp")
            hand = urllib.request.urlretrieve(
                f"https://github.com/DankMemer/imgen/blob/master/assets/deepfry/ok-hand.bmp", "ok-hand.bmp")
            '''response1 = requests.get(
                url='https://github.com/DankMemer/imgen/blob/master/assets/deepfry/joy.bmp')
            joy = Image.open((response1.content))
            response2 = requests.get(
                url='https://github.com/DankMemer/imgen/blob/master/assets/deepfry/ok-hand.bmp')
            hand = Image.open((response2.content))
            response3 = requests.get(
                url='https://github.com/DankMemer/imgen/blob/master/assets/deepfry/100.bmp')
            hundred = Image.open((response3.content))
            response4 = requests.get(
                url='https://github.com/DankMemer/imgen/blob/master/assets/deepfry/fire.bmp')
            fire = Image.open((response4.content))'''
            joy, hand, hundred, fire = [
                Image.open(BytesIO(f"{asset}.bmp"))
                .resize((100, 100))
                .rotate(random.randint(-30, 30))
                .convert('RGBA')
                for asset in ['100', 'fire', 'joy', 'ok-hand']
            ]

            avatar.paste(joy, (random.randint(20, 75),
                               random.randintrandint(20, 45)), joy)
            avatar.paste(hand, (random.randint(20, 75),
                                random.randint(150, 300)), hand)
            avatar.paste(hundred, (random.randint(150, 300),
                                   random.randint(20, 45)), hundred)
            avatar.paste(fire, (random.randint(150, 300),
                                random.randint(150, 300)), fire)

            noise = avatar.convert('RGB')
            #noise = noisegen.add_noise(noise, 25)
            noise = ImageEnhance.Contrast(
                noise).enhance(random.randint(5, 20))
            noise = ImageEnhance.Sharpness(noise).enhance(17.5)
            noise = ImageEnhance.Color(noise).enhance(
                random.randint(-15, 15))
            noise.save("deepfry.png", format='png')
            await ctx.message.reply(file=discord.File(noise))

    '''@commands.command()
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
            await ctx.message.reply(file=discord.File(buf, f"Profile of {user.name}#{user.discriminator}.png"))'''

    def get_extra_data(self, user_id):

        if type(user_id) in [int, float]:
            user_id = str(int(user_id))

        guild_data = Extras_MongoDB.find_one(
            {"user_id": user_id})

        return guild_data

    @commands.command()
    async def afk(self, ctx, *, reason="No reason provided"):
        user_data = self.get_extra_data(ctx.author.id)
        member = ctx.author

        self.afk_users_cache[member.id] = reason
        self.newly_added_afk_users.append(member.id)

        if user_data is None:

            user_data = {"user_id": member.id,
                         'reason': reason}
            Extras_MongoDB.insert_one(user_data)

        else:
            try:
                user_data['reason'] = reason
                Extras_MongoDB.update_one(
                    {"user_id": member.id}, {"$set": user_data})
            except:
                pass
        try:
            await member.edit(nick=f"[AFK] {member.display_name}")
        except discord.Forbidden:
            pass

        embed = discord.Embed(
            title=":zzz: Member AFK", description=f"{member.mention} has gone **AFK**", color=member.color)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=self.client.user.name,
                         icon_url=self.client.user.avatar_url)
        embed.add_field(name='**AFK Note:**', value=reason)
        await ctx.channel.send(embed=embed)

    '''@commands.Cog.listener()'''

    def remove_afk_prefix(self, display_name):
        '''if "[AFK]" in afk.split():
            return " ".join(afk.split()[1:])
        else:
            return afk'''

        if display_name.lower().startswith('[afk]'):
            display_name[6:].strip()

        return display_name

    @commands.Cog.listener()
    async def on_message(self, message):
        #stats = Extras_MongoDB.find_one({"user_id": {str(message.author.id)}})

        #user_data = self.get_extra_data(message.author.id)
        # if str(message.author.id) in user_data["user_id"].keys():
        if message.author.id in self.afk_users_cache:
            # user_data["user_id"].pop(str(message.author.id))

            if message.author.id in self.newly_added_afk_users:
                self.newly_added_afk_users.remove(message.author.id)
            else:
                self.afk_users_cache.pop(message.author.id)
                Extras_MongoDB.delete_one({'user_id': message.author.id})

                try:
                    '''new_nickname = str(self.remove_afk_prefix(
                        message.author.display_name))'''
                    if message.author.display_name.startswith('[AFK]'):
                        name = str(
                            message.author.display_name.replace('[AFK]', ''))

                        await message.author.edit(nick=name)
                except MissingPermissions:
                    pass

                await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK!")
        else:
            '''for id, reason in user_data["user_id"].items():
                member = get(member.guild.members, id=id)
                # if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                if member in message.mentions:
                    await message.reply(f"{member.name} is AFK. AFK Note: {reason}")
        # for reason in user_data["user_id"][str(member)]:'''

            for mention in message.mentions:
                if mention.id in self.afk_users_cache:

                    await message.reply(f"**{mention}** is AFK.\n**AFK Note:** `{self.afk_users_cache[mention.id]}`")

    async def on_command_error(ctx, error1):
        if isinstance(error1, commands.UserInputError):
            await ctx.message.reply('Please give proper input.')
        elif isinstance(error1, commands.MissingPermissions):
            await ctx.message.reply(
                "You don't have the permissions to execute this command.")
        elif isinstance(error1, commands.MissingRequiredArgument):
            await ctx.message.reply('Please give proper input.')
        elif isinstance(error1, commands.CommandNotFound):
            await ctx.message.reply("Invalid command.")

        #Extras_MongoDB.update_one({"user_id": {str(message.author.id)}}, {"$set": user_data})


def setup(client):
    client.add_cog(Wanted(client))
