import os
import random
import discord
from discord import client
from discord import embeds
from discord.ext import commands
import json

os.chdir(
    r"C:\Users\cogent\Downloads\Hydrargyruum\Supporting")

prefix = '-'
#api_key = "RRcoNdt3Qs8k"
#rs = RandomStuff(async_mode = True, api_key = api_key)


client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      intents=discord.Intents.all())


@client.command()
async def balance(ctx):

    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"] = 100
    bank_amt = users[str(user.id)]["bank"] = 0

    em = discord.Embed(
        title=f"{ctx.author.name}'s Balance", color=discord.Color.purple())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name="Bank Balance", value=bank_amt)
    await ctx.send(embed=em)


async def open_account(user):
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

    return users


@client.command()
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author

    earnings = random.randrange(101)

    await ctx.send(f"Oh you poor little beggar, take ⏣ {earnings}!")
    users[str(user.id)]["wallet"] + - earnings
    with open("mainbank.json", "r") as f:
        users = json.load(f)

# client.run('ODQ0ODEzMzE2NTA1MDc1NzEy.YKX3tg.0eYGwHfkQMKEbF71c8dVDmGVlBI')
