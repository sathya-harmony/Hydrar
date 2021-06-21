import discord
from discord.ext import commands
from pymongo import MongoClient


bot_channel = 846986346245128193
talk_channel = [846986346245128193]
level = ["Level 1"]
levelnum = [2]

cluster = MongoClient(
    "mongodb+srv://Hydra:CihVirus123@hydra.jea2k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

levelling = cluster["Hydra"]["Hydra"]


class levels(commands.Cog):
    def __init__(self, client):
        self.client = client

    @ commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channel:
            stats = levelling.find_one({"id": message.author.id})

            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id, "xp": 100}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id": message.author.id},
                                         {"$set": {
                                             "xp": xp
                                         }})
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

    @ commands.command(aliases=["level", "lvl", "xp"])
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id": ctx.author.id})
            if stats is None:
                await ctx.channel.send("You haven't sent any messaged to Level up!")

            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < abs((50 * (lvl**2)) + (50 * (lvl))):
                        break
                    lvl += 1

                xp -= abs(((50 * (lvl - 1)**2)) + (50 * (lvl - 1)))

                # boxes = int((xp/(200*((1/2) * lvl)))*20)
                boxes = int(xp/(5*lvl))
                ranking = levelling.find().sort("xp", -1)
                for x in ranking:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(
                    title="{}'s level stats".format(ctx.author.name))
                embed.add_field(
                    name="**XP**", value=f"{xp}/{int(100*lvl)}", inline=False)
                embed.add_field(
                    name="**Rank**", value=f"{rank}/{ctx.guild.member_count}", inline=False)
                embed.add_field(name="Progress Bar", value=boxes *
                                "🟩"+(20-boxes)*"⬜", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)

    @ commands.command(aliases=["top"])
    async def leaderboard(self, ctx):
        if (ctx.channel.id == bot_channel):
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(title="LeaderBoard:")
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(
                        name=f" {i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
                    i += 1

                except:
                    pass

                if i >= 11:
                    break

            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(levels(client))
