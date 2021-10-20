from operator import attrgetter
import discord
from discord import client
from discord.errors import Forbidden
from discord.ext import commands
from pymongo import MongoClient
import random
from discord.utils import get
import aiohttp
import io
from PIL import Image, ImageDraw, ImageFont


'''bot_channel = 870541730410270814
talk_channel = [870541730410270814]'''
level = ["Level 1"]
levelnum = [2]


#Problem is here
cluster = MongoClient(
    "mongodb+srv://Hydra:CihVirus123@hydra.rvrbk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)


levelling = cluster["Hydra"]["Hydra"]


class levels(commands.Cog):
    def __init__(self, client):
        self.client = client

    @ commands.Cog.listener()
    async def on_message(self, message):
        try:
            user_id = str(message.author.id)
            guild_id = message.guild.id

            '''stats = levelling.find_one({"guild_id": guild_id,
                                        "users": {
                                            user_id: user_id

                                        }})'''
            stats = levelling.find_one({"guild_id": guild_id})

            if not message.author.bot:
                if stats is None:
                    new_guild = {"guild_id": guild_id,
                                 "users": {user_id: {"xp": 100}}}
                    levelling.insert_one(new_guild)

                elif user_id not in stats['users']:
                    stats['users'][user_id] = {'xp': 100}
                    levelling.update_one(
                        {"guild_id": guild_id}, {"$set": stats})

                else:

                    stats["users"][user_id]["xp"] += 5
                    xp = stats["users"][user_id]["xp"]

                    levelling.update_one(
                        {"guild_id": guild_id}, {"$set": stats})

                    lvl = 0
                    while True:
                        if xp < ((50 * (lvl**2)) + (50 * (lvl))):
                            break
                        lvl += 1

                    xp -= abs(((50 * (lvl - 1)**2)) + (50 * (lvl - 1)))

                    if xp == 0:
                        await message.channel.send(
                            f"Congratulations, {message.author.mention}! You just levelled up to **level {lvl}**!"
                        )
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(
                                    discord.utils.get(
                                        message.author.guild.roles,
                                        name=level[i]))
                                embed = discord.Embed(
                                    description=f"{message.author.mention} you have gotten the role **{level[i]}**!!"
                                )
                                embed.set_thumbnail(
                                    url=message.author.avatar_url)

                                await message.channel.send(embed=embed)
        except AttributeError or Forbidden:
            pass

    @ commands.command(aliases=["level", "lvl", "xp"])
    async def rank(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        user_id = str(member.id)
        guild_id = ctx.guild.id
        stats = levelling.find_one({"guild_id": guild_id})

        if str(member.id) not in stats['users']:
            await ctx.message.reply(f"**{member.display_name}#{member.discriminator}** hasn't sent any messages to Level up!")

        else:
            xp = stats["users"][user_id]["xp"]
            lvl = 0

            user_ids_sorted = list(stats["users"])
            user_ids_sorted.sort(
                key=lambda _user_id: stats["users"][_user_id]["xp"], reverse=True)

            rank = user_ids_sorted.index(user_id) + 1

            while True:
                if xp < abs((50 * (lvl**2)) + (50 * (lvl))):
                    break
                lvl += 1

            xp -= abs(((50 * (lvl - 1)**2)) + (50 * (lvl - 1)))

            boxes = int(xp/(5*lvl))
            guild_id = 824199403954896906
            # get(ctx.message.guild.emojis, name="filled_full_middle")
            #emoji = client.get_emoji(name="filled_full_middle")
            #emoji2 = get(ctx.message.guild.emojis, name="empty_begin")

            '''embed = discord.Embed(
                title="{}'s level stats".format(member.name))
            embed.add_field(
                name="**XP**", value=f"{xp}/{int(100*lvl)}", inline=False)
            embed.add_field(
                name="**Rank**", value=f"{rank}/{ctx.guild.member_count}", inline=False)
            embed.add_field(name="Progress Bar", value=boxes *
                            f"<:filled_full_middle:890589069757788200>"+(20-boxes)*"<:empty_middle:890589065408295042>", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.message.reply(embed=embed)'''
            final_xp = int(100*lvl)
            bytes = await self.make_rank_image(member, rank=rank, level=lvl, xp=xp, final_xp=final_xp)
            file = discord.File(bytes, 'rank.png')
            await ctx.message.reply(file=file)

    async def make_rank_image(self, member: discord.Member, rank, level, xp,  final_xp):
        user_avatar_image = str(member.avatar_url_as(format='png', size=4096))
        async with aiohttp.ClientSession() as Session:
            async with Session.get(user_avatar_image) as resp:
                avatar_bytes = io.BytesIO(await resp.read())
        img = Image.new('RGB', (1000, 240))
        logo = Image.open(avatar_bytes).resize((200, 200))

        # Stack overflow helps :)
        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)
        ##############################
        img.paste(logo, (20, 20), mask=logo)

        # Black Circle
        draw = ImageDraw.Draw(img, 'RGB')
        draw.ellipse((152, 152, 208, 208), fill='#000')

        # Placing offline or Online Status
        # Discord Colors (Online: '#43B581')
        # draw.ellipse((155, 155, 205, 205), fill='#43B581')
        if (member.status) is discord.Status.online:

            online = Image.open("Cogs/Pics/OnlineStatus.png")
            online = online.resize((50, 50))
            img.paste(online, (155, 155), mask=online)

        elif (member.status) is discord.Status.dnd:
            online = Image.open("Cogs/Pics/DNDStatus.png")
            online = online.resize((50, 50))
            img.paste(online, (155, 155), mask=online)
            # print("Hehehe")

            #print("here", img.size)

        elif (member.status) is discord.Status.idle:
            online = Image.open("Cogs/Pics/IdleStatus.png")
            online = online.resize((50, 50))
            img.paste(online, (155, 155), mask=online)

        elif (member.status) is discord.Status.offline:
            online = Image.open("Cogs/Pics/OfflineStatus.png")
            online = online.resize((50, 50))
            img.paste(online, (155, 155), mask=online)

        ##################################
        fill = random.choice(['#f21111', '#11f26f',
                             '#11ebf2', '#f211cc'])
        # Working with fonts
        big_font = ImageFont.FreeTypeFont('fonts/ABeeZee-Regular.ttf', 60)
        medium_font = ImageFont.FreeTypeFont('fonts/ABeeZee-Regular.ttf', 40)
        small_font = ImageFont.FreeTypeFont('fonts/ABeeZee-Regular.ttf', 30)

        # Placing Level text (right-upper part)
        text_size = draw.textsize(f"{level}", font=big_font)
        offset_x = 1000-15 - text_size[0]
        offset_y = 8
        draw.text((offset_x, offset_y),
                  f"{level}", font=big_font, fill="#11ebf2")
        text_size = draw.textsize('LEVEL', font=small_font)

        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "LEVEL",
                  font=small_font, fill="#11ebf2")

        # Placing Rank Text (right upper part)
        text_size = draw.textsize(f"#{rank}", font=big_font)
        offset_x -= 15 + text_size[0]
        offset_y = 8
        draw.text((offset_x, offset_y), f"#{rank}", font=big_font, fill="#fff")

        text_size = draw.textsize("RANK", font=small_font)
        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "RANK", font=small_font, fill="#fff")

        # Placing Progress Bar
        # Background Bar
        bar_offset_x = logo.size[0] + 20 + 100
        bar_offset_y = 160
        bar_offset_x_1 = 1000 - 50
        bar_offset_y_1 = 200
        circle_size = bar_offset_y_1 - bar_offset_y

        # Progress bar rect greyier one
        draw.rectangle((bar_offset_x, bar_offset_y,
                       bar_offset_x_1, bar_offset_y_1), fill="#727175")
        # Placing circle in progress bar

        # Left circle
        draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x +
                     circle_size//2, bar_offset_y + circle_size), fill="#727175")

        # Right Circle
        draw.ellipse((bar_offset_x_1 - circle_size//2, bar_offset_y,
                     bar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#727175")

        # Filling Progress Bar

        bar_length = bar_offset_x_1 - bar_offset_x
        # Calculating of length
        # Bar Percentage (final_xp - current_xp)/final_xp

        # Some variables
        # print(final_xp)
        progress = ((final_xp - xp) * 100)/final_xp
        progress = 100 - progress
        progress_bar_length = round(bar_length * progress/100)
        pbar_offset_x_1 = bar_offset_x + progress_bar_length

        # Drawing Rectangle
        draw.rectangle((bar_offset_x, bar_offset_y,
                       pbar_offset_x_1, bar_offset_y_1), fill=fill)
        # Left circle
        draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x +
                     circle_size//2, bar_offset_y + circle_size), fill=fill)
        # Right Circle
        draw.ellipse((pbar_offset_x_1 - circle_size//2, bar_offset_y,
                     pbar_offset_x_1 + circle_size//2, bar_offset_y_1), fill=fill)

        def convert_int(integer):
            integer = round(integer / 1000, 2)
            return f'{integer}K'

        # Drawing Xp Text
        text = f"/ {convert_int(final_xp)} XP"
        xp_text_size = draw.textsize(text, font=small_font)
        xp_offset_x = bar_offset_x_1 - xp_text_size[0]
        xp_offset_y = bar_offset_y - xp_text_size[1] - 10
        draw.text((xp_offset_x, xp_offset_y), text,
                  font=small_font, fill="#727175")

        text = f'{convert_int(xp)} '
        xp_text_size = draw.textsize(text, font=small_font)
        xp_offset_x -= xp_text_size[0]
        draw.text((xp_offset_x, xp_offset_y), text,
                  font=small_font, fill="#fff")

        # Placing User Name
        text = member.display_name
        text_size = draw.textsize(text, font=medium_font)
        text_offset_x = bar_offset_x - 10
        text_offset_y = bar_offset_y - text_size[1] - 10
        draw.text((text_offset_x, text_offset_y),
                  text, font=medium_font, fill="#fff")

        # Placing Discriminator
        text = f'#{member.discriminator}'
        text_offset_x += text_size[0] + 10
        text_size = draw.textsize(text, font=small_font)
        text_offset_y = bar_offset_y - text_size[1] - 20
        draw.text((text_offset_x, text_offset_y), text,
                  font=small_font, fill="#727175")

        bytes = io.BytesIO()
        img.save(bytes, 'png')
        bytes.seek(0)
        return bytes

    @ commands.command(aliases=["top"])
    async def leaderboard(self, ctx):
        user_id = str(ctx.author.id)
        guild_id = ctx.guild.id

        stats = levelling.find_one({"guild_id": guild_id})
        user_ids_sorted = list(stats["users"])
        user_ids_sorted.sort(
            key=lambda _user_id: stats["users"][_user_id]["xp"], reverse=True)

        rank = 1
        embed = discord.Embed(title="Leaderboard(XP):")

        for uid in user_ids_sorted:
            try:
                temp_user = ctx.guild.get_member(int(uid))
                embed.add_field(
                    name=f"{rank}: {temp_user.name}", value=f"Total XP: {stats['users'][uid]['xp']}", inline=False)
                embed.set_thumbnail(url=str(ctx.guild.icon_url))

                rank += 1
            except:
                rank -= 1

            if rank > 10:
                break

        if user_ids_sorted.index(user_id) > (10-1):
            embed.add_field(
                name=f"{user_ids_sorted.index(user_id) + 1}: {ctx.author.name}", value=f"Total XP: {stats['users'][user_id]['xp']}", inline=False)
            embed.set_thumbnail(url=str(ctx.guild.icon_url))
        await ctx.message.reply(embed=embed)


def setup(client):
    client.add_cog(levels(client))
