from operator import attrgetter
import discord
from discord import client
from discord.ext import commands
from pymongo import MongoClient
import random
from discord.utils import get


'''bot_channel = 870541730410270814
talk_channel = [870541730410270814]'''
level = ["Level 1"]
levelnum = [2]

cluster = MongoClient(
    "mongodb+srv://Hydra:jpszYWQcPolIDvCm@hydra.jea2k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
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
        except AttributeError:
            pass

    @ commands.command(aliases=["level", "lvl", "xp"])
    async def rank(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        user_id = str(member.id)
        guild_id = ctx.guild.id
        stats = levelling.find_one({"guild_id": guild_id})

        if stats is None:
            await ctx.message.reply("You haven't sent any messaged to Level up!")

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

            embed = discord.Embed(
                title="{}'s level stats".format(member.name))
            embed.add_field(
                name="**XP**", value=f"{xp}/{int(100*lvl)}", inline=False)
            embed.add_field(
                name="**Rank**", value=f"{rank}/{ctx.guild.member_count}", inline=False)
            embed.add_field(name="Progress Bar", value=boxes *
                            f"<:filled_full_middle:890589069757788200>"+(20-boxes)*"<:empty_middle:890589065408295042>", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.message.reply(embed=embed)

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
