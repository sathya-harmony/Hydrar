import os
import random
import discord
from discord import client
from discord import embeds
from discord.ext import commands
import json

# os.chdir(
# r"Hydrargyruum\Supporting")


class Economy(commands.Cog):
    def __init__(self,  client):
        self.client = client

    async def open_account(self, user):
        users = await self.get_bank_data()

        if str(user.id) in users:
            return False

        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 100
            users[str(user.id)]["bank"] = 0

        with open("Supporting/mainbank.json", "w") as f:
            json.dump(users, f)

        return True

    async def get_bank_data(self):
        with open("Supporting/mainbank.json", "r") as f:
            users = json.load(f)

        return users

    @commands.command()
    async def balance(self, ctx):

        await self.open_account(ctx.author)
        user = ctx.author

        users = await self.get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(
            title=f"{ctx.author.name}'s Balance", color=discord.Color.purple())
        em.add_field(name="Wallet Balance", value=wallet_amt)
        em.add_field(name="Bank Balance", value=bank_amt)
        await ctx.send(embed=em)

    '''async def open_account(user):
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        if str(user.id) in users:
            return False

        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 100
            users[str(user.id)]["bank"] = 0

        with open("mainbank.json", "w") as f:
            json.dumb(users, f)

        return True

    async def get_bank_data():
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        return users'''

    @commands.command()
    async def beg(self, ctx):
        await self.open_account(ctx.author)

        users = await self.get_bank_data()
        user = ctx.author

        earnings = random.randrange(101)

        await ctx.send(f"Oh you poor little beggar, take ⏣{earnings}!")
        users[str(user.id)]["wallet"] += earnings
        with open("Supporting/mainbank.json", "w") as f:
            json.dump(users, f)

# client.run('ODQ0ODEzMzE2NTA1MDc1NzEy.YKX3tg.0eYGwHfkQMKEbF71c8dVDmGVlBI')


def setup(client):
    client.add_cog(Economy(client))
