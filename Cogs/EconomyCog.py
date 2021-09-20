
from typing import Text
from discord import user
from discord.ext.commands import bot
from discord.ext.commands.cooldowns import BucketType
import pymongo
import modules.title_choices_beg_economy as title_choices
import random
import discord
from discord import client
from discord import embeds
from discord.ext import commands
import os
from pymongo import MongoClient
import time
import math
from math import *
from discord_components import *


cluster = MongoClient(
    "mongodb+srv://Hydra:CihVirus123@economy.2xn9e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

Economy_MongoDB = cluster["Economy"]["Economy"]


class Economy(commands.Cog):
    def __init__(self,  client):
        self.client = client

    mainshop = {'watch': {"display": "Watch""⌚", "price": 800, "desc": "Time"},
                'laptop': {"display": "Laptop""💻", "price": 5000, "desc": "Work"},
                'banknote': {"display": "Banknote💸", "price":  25000, "desc": "Increases bank storage capacity"},
                'padlock': {"display": "Padlock🔒", "price":  4000, "desc": "Protection from robbers"}}

    job_list = {'discord mod': {"display": "✅ Discord Mod", "salary": 10000, "hours_needed": 0,
                                'desc': 'Hours Required Per Day: `0` — Salary: `⏣ 10000 per hour`'},
                'babysitter': {"display": "✅ Babysitter", "salary": 10500, "hours_needed": 1,
                               'desc': 'Hours Required Per Day: `1` — Salary: `⏣ 10500 per hour`'},
                'fast food cook': {"display": "✅ Fast Food Cook", "salary": 11111, "hours_needed": 2,
                                   'desc': 'Hours Required Per Day: `2` — Salary: `⏣ 11111 per hour`'},
                'house wife': {"display": "✅ House Wife", "salary": 12000, "hours_needed": 2,
                               'desc': 'Hours Required Per Day: `2` — Salary: `⏣ 12000 per hour`'},
                'twitch streamer': {"display": "✅ Twitch Streamer", "salary": 15000, "hours_needed": 3,
                                    'desc': 'Hours Required Per Day: `3` — Salary: `⏣ 15000 per hour`'}}
    job_list_2 = {'youtuber': {"display": "✅ YouTuber", "salary": 16000, "hours_needed": 3,
                               'desc': 'Hours Required Per Day: `3` — Salary: `⏣ 16000 per hour`'},
                  'professional hunter': {"display": "✅ Professional Hunter", "salary": 17000, "hours_needed": 4,
                                          'desc': 'Hours Required Per Day: `4` — Salary: `⏣ 17000 per hour`'},
                  'professional fisherman': {"display": "✅ Twitch Streamer", "salary": 18000, "hours_needed": 4,
                                             'desc': 'Hours Required Per Day: `4` — Salary: `⏣ 18000 per hour`'},
                  'bartender': {"display": "✅ Bartender", "salary": 19000, "hours_needed": 4,
                                'desc': 'Hours Required Per Day: `4` — Salary: `⏣ 19000 per hour`'}}

    def get_bank_data(self, guild_id):

        if type(guild_id) in [int, float]:
            guild_id = str(int(guild_id))

        guild_data = Economy_MongoDB.find_one(
            {"guild_id": guild_id})  # GET BANK DATA'''

        return guild_data

    def update_bank(self, user, change=0, mode="wallet", overwrite=False):

        guild_id = str(user.guild.id)
        user_id = str(user.id)
        if type(guild_id) in [int, float]:
            guild_id = str(int(guild_id))
        # UPDATE BANK
        guild_data = self.get_bank_data(guild_id)

        if overwrite:
            guild_data["users"][str(user_id)][mode] = change
        else:
            guild_data["users"][str(user_id)][mode] += change

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        return guild_data

    def open_account(self, user):
        # OPEN ACCOUNT VARIABLE
        guild_id = str(user.guild.id)
        user_id = str(user.id)

        guild_data = self.get_bank_data(guild_id)
        if type(guild_id) in [int, float]:
            guild_id = str(int(guild_id))

        if guild_data is None:
            guild_data = {"guild_id": guild_id,
                          "users": {user_id: {"wallet": 100,
                                              "bank": 0,
                                              "bank_space": 100,
                                              "padlock": False,
                                              "job": {"job_name": None,
                                                      "hours_worked": 0},
                                              "inv": {},
                                              "daily": {"last_used": 0, "streak": 1}
                                              }
                                    }
                          }

            Economy_MongoDB.insert_one(guild_data)

        elif user_id not in guild_data['users']:
            guild_data['users'][user_id] = {
                'wallet': 100, "bank": 0, "bank_space": 100, "padlock": False, "job": {"job_name": None,
                                                                                       "hours_worked": 0}, 'inv': {},  "daily": {"last_used": 0, "streak": 1}}
            Economy_MongoDB.update_one(
                {"guild_id": guild_id}, {"$set": guild_data})

        return guild_data

    '''@commands.command(aliases=[])
    async def meme(self, ctx):
        # msg = await ctx.message.reply('Loading meme... <a:Loading:84528574434795580>')
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json")as r:
                memes = await r.join()
                embed = discord.Embed(color=discord.Color.purple())
                embed.set_image(
                    url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.set_footer(
                    text=f'Powered by r/Memes! | Meme requested by {ctx.author}')
                await ctx.send(embed=embed)'''

    '''reddit = asyncpraw.Reddit(client_id='8i3fEtFOnr_XjpkrpatKOA',
                                  client_secret='qBg4vg8yT8tBywSIz8pKSDPQc8dG-A',
                                  username='Hydrargyrum',
                                  password='CihVirus123',
                                  user_agent='Hydra_meme')
        subreddit = await reddit.subreddit(subred)
        all_subs = []
        top = subreddit.top(limit=50)
        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        embed = embeds.Embed(
            title=f'__{name}__', color=discord.Color.random())
        embed.add_image(url=url)
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        # await msg.edit(content=f'<https://reddit.com/r/{subreddit}/> :white_check_mark:')
        return'''

    @commands.command(aliases=[])
    @commands.cooldown(1, 60*60*24, BucketType.user)
    async def daily(self, ctx):

        self.open_account(ctx.author)
        amount = 25000
        users = ctx.author.name
        guild_id = str(ctx.guild.id)
        user_id = str(ctx.author.id)

        guild_data = self.get_bank_data(guild_id)
        current_time = time.time()

        user_daily = guild_data['users'][user_id]['daily']

        # You need it to be lesser than the given time for it to work. 2 days because 1 day cooldown, 1 day streak buffer.

        if current_time - 2*60*60*24 <= user_daily['last_used']:
            user_daily['streak'] += 1
        else:
            user_daily['streak'] = 1

        user_daily['last_used'] = current_time

        streak = user_daily['streak']

        em = discord.Embed(
            title=f"Here are your daily coins, {users}!", description=f"**⏣ {amount+streak*250:,}** was placed in your wallet.", color=discord.Color.purple())
        em.set_thumbnail(url=ctx.author.avatar_url)
        em.set_footer(text=f"Streak: {streak} days(+⏣ {streak*250:,})")
        await ctx.message.reply(embed=em)
        self.update_bank(ctx.author, (amount + streak*250))

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        self.update_bank(ctx.author, amount + streak*250)

    @daily.error
    async def error_daily(self, ctx, error):
        hour = int((error.retry_after/60)//(60))
        mins = int((error.retry_after-(hour*60*60))//(60))
        seconds = int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(
                title=f"You've already claimed your daily today, {ctx.author.name}!", description=f"Your next daily is ready in:\n**{hour} hours, {mins} minutes and {seconds} seconds**")
            em.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=em)

    @commands.command(aliases=["with", "draw"])
    # WITHDRAW COMMAND
    async def withdraw(self, ctx, amount=None):
        try:
            self.open_account(ctx.author)

            if amount == None:
                await ctx.message.reply("How on Earth do you expect to withdraw absolutly nothing?")
                return

            users = self.get_bank_data(ctx.guild.id)
            bal = int(users["users"][str(ctx.author.id)]["bank"])
            if amount == 'all':
                amount = int(users["users"][str(ctx.author.id)]["bank"])

            amount = int(amount)
            if amount > bal:
                await ctx.message.reply("HA, you're broke.")
                return

            if amount < 0:
                await ctx.message.reply("Currency in negative value??")
                return

            self.update_bank(ctx.author, amount)
            self.update_bank(ctx.author, -1*amount, "bank")
            users2 = self.get_bank_data(ctx.guild.id)
            amount_left = int(users2["users"][str(ctx.author.id)]["wallet"])
            await ctx.message.reply(f"**⏣ {amount:,}** withdrawn, current wallet balance is **⏣ {amount_left:,}**.")
        except ValueError:
            await ctx.message.reply("Please give proper input. Correct way to use this command is `-with <amount you want to withdraw from bank>`")

    @commands.command(aliases=["dep", "depp"])
    # DEPOSIT COMMAND
    async def deposit(self, ctx, amount=None):
        try:
            self.open_account(ctx.author)

            if amount == None:
                await ctx.message.reply("How on Earth do you expect to deposit absolutly nothing?")
                return

            # bank_amt = await self.get_bank_data()[str(ctx.author.id)]["bank"]
            users = self.get_bank_data(ctx.guild.id)
            bal = int(users["users"][str(ctx.author.id)]["wallet"])
            bank_space = users["users"][str(ctx.author.id)]["bank_space"]

            if amount == 'all' and int(users["users"][str(ctx.author.id)]["wallet"]) >= int(bank_space) - int(users["users"][str(ctx.author.id)]["bank"]):
                # bal - int(bank_space)
                a = int(bank_space) -   \
                    int(users["users"][str(ctx.author.id)]["bank"])
                amount = a

            elif amount == 'all' and int(users["users"][str(ctx.author.id)]["wallet"]) <= int(bank_space) - int(users["users"][str(ctx.author.id)]["bank"]):
                amount = int(users["users"][str(ctx.author.id)]["wallet"])

            amount = int(amount)
            if amount > bal:
                await ctx.message.reply("HA, you're broke.")
                return

            elif amount > int(bank_space) or amount > (int(bank_space) - int(users["users"][str(ctx.author.id)]["bank"])):
                await ctx.message.reply("doode you don't have enough space in your bank to deposit that much")
                return
            elif amount < 0:
                await ctx.message.reply("Currency in negative value??")
                return

            self.update_bank(ctx.author, -1*amount)
            self.update_bank(ctx.author, amount, "bank")
            users2 = self.get_bank_data(ctx.guild.id)
            amount_left = int(users2["users"][str(ctx.author.id)]["wallet"])
            await ctx.message.reply(f"**⏣ {amount:,}** deposited, current wallet balance is **⏣ {amount_left:,}**.")
        except ValueError:
            await ctx.message.reply("Please give proper input. Correct way to use this command is `-dep <amount to deposit into bank>`")

    @ commands.command(aliases=["give", "donate"])
    # SEND COMMAND
    async def send(self, ctx, member: discord.Member, amount=None):

        user = ctx.author
        self.open_account(user)
        self.open_account(member)

        if amount == None:
            await ctx.message.reply("How on Earth do you send someone absolutly nothing?")
            return
        users = self.get_bank_data(ctx.guild.id)

        bal = int(users["users"][str(ctx.author.id)]["wallet"])

        amount = int(amount)
        if amount > bal:
            await ctx.message.reply("HA, you're broke. ")
            return

        if amount < 0:
            await ctx.message.reply("Currency in negative value??")
            return

        self.update_bank(user, -1*amount, "wallet")
        self.update_bank(member, amount, "wallet")
        await ctx.message.reply(f"You sent **⏣ {amount:,}** to {member.mention}'s the bank!")
        '''except ValueError:
            await ctx.message.reply("Please give proper input. Correct way to use this command is `-send <the person you want to send money to> <amount>`")'''

    @ commands.command(aliases=["bal"])
    # BALANCE COMMAND
    async def balance(self, ctx, member: discord.Member = None):
        if member == None:
            user = ctx.author
            self.open_account(user)

        else:
            user = member
            self.open_account(user)

        users = self.get_bank_data(ctx.guild.id)
        wallet_amt = users["users"][str(user.id)]["wallet"]
        bank_amt = users["users"][str(user.id)]["bank"]
        bank_space = users["users"][str(user.id)]["bank_space"]

        em = discord.Embed(
            title=f"{user.name}'s Balance", description=f"**Wallet**: ⏣ {wallet_amt:,}\n**Bank**: ⏣ {bank_amt:,} / {bank_space:,} `({(bank_amt/bank_space)*100}%)`", color=discord.Color.purple())

        em.set_thumbnail(url=user.avatar_url)
        await ctx.message.reply(embed=em)
    # BEG COMMAND

    @ commands.command()
    @ commands.cooldown(1, 30, BucketType.user)
    async def beg(self, ctx):
        self.open_account(ctx.author)

        users = self.get_bank_data(ctx.guild.id)
        user = ctx.author

        earnings = random.randrange(2500)
        a = [False, True]
        b = random.choice(a)
        if b is True:
            title_choice = random.choice(title_choices.names)
            description = random.choice([f"ok sure, have **⏣ {earnings:,}** coins",
                                         f"ur a bit stanky but here's **⏣ {earnings:,}** coins",
                                        f"Oh, you poor little beggar, take **⏣ {earnings:,}** coins",
                                         f"you get **⏣ {earnings:,}** COINS",
                                         f"**⏣ {earnings:,}** coins for you"])
            self.update_bank(user, earnings)

            em = discord.Embed(
                title=title_choice, set_thumbnail=ctx.author, description=description,  color=discord.Color.purple())
            em.set_thumbnail(url=str(user.avatar_url))
            em.set_footer(text="begging is everyone's right!")

            await ctx.message.reply(embed=em)
        elif b is False:
            title_choice = random.choice(title_choices.names)
            description = random.choice(title_choices.loss_message)

            em = discord.Embed(
                title=title_choice, description=description,  thumbnail=ctx.author,  color=discord.Color.purple())
            em.set_thumbnail(url=str(user.avatar_url))
            em.set_footer(text="begging is everyone's right!")

            await ctx.message.reply(embed=em)

    @ beg.error
    async def error_beg(self, ctx, error):
        hour = int((error.retry_after/60)//(60))
        mins = int((error.retry_after-(hour*60*60))//(60))
        seconds = int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Too spicy, take a breather",
                               description=f'Stop begging so much, it makes you look like a poor person.\nYou can beg more in {seconds} seconds')
            em.set_footer(text="The default cooldown is 30 seconds")

            await ctx.message.reply(embed=em)

    # STOCK/BET COMMAND
    '''@commands.command(aliases=["bet", "gamble"])
    async def stock(self, ctx, amount=None):

        user_id = str(ctx.author.id)
        guild_data = self.open_account(ctx.author)
        bal = int(guild_data['users'][user_id]['wallet'])

        if amount == None:
            await ctx.message.reply("How on Earth do you expect to bet nothin'?")
            return

        amount = int(amount)
        if amount > bal:
            await ctx.message.reply(f"{ctx.author.mention} You only have **⏣ {bal}, don't try and lie to me hoe")
            return

        if amount < 0:
            await ctx.message.reply(f"{ctx.author.mention} You have to bet actual coins, dont try to break me.")
            return
        if amount < 50:
            await ctx.message.reply(f"{ctx.author.mention} You can't bet less than **⏣ 50**")
            return

        final_bot = []
        for i in range(20):
            iteration_bot = random.randint(1, 100)
            final_bot.append(iteration_bot)
        # final_user = []
        kumar = (random.randint(1, 100))
        if kumar not in final_bot:
            def absolute_difference_function(
                list_value): return abs(list_value - kumar)
            closest_value = min(final_bot, key=absolute_difference_function)
            if closest_value > kumar:
                loss = int(
                    (int(int(closest_value)-int(kumar))/closest_value)*100)
                await ctx.send(f"GET REKT! YOU LOST {loss}%")
                return
            elif closest_value < kumar:
                loss = int((int(int(kumar)-int(closest_value))/kumar)*100)
            await ctx.send(f"GET REKT! YOU LOST {loss}%")
            return
        else:
            await ctx.send("you won")'''

    '''for i in final_user:
            if i in final_bot:
                a = "Holy smokes you won a lottery!"

            else:
                pass
        await ctx.send(a)
        print(f"{i}, {final_bot}")
        for i in range(final_user[1]):
            if i in final_bot:
                b = await ctx.send("nice")

            else:
                pass

        await ctx.send(b)
        print(f"{i}, {final_bot}")'''

    @ commands.command(aliases=["stock"])
    @ commands.cooldown(1, 15, BucketType.user)
    async def slots(self, ctx, amount=None):
        # channel = bot.get_channel(ctx.channel.id)

        # message = str(await channel.fetch_message(bot.message.id))
        try:
            user_id = str(ctx.author.id)

            guild_data = self.open_account(ctx.author)

            if amount == None:
                await ctx.message.reply("How on Earth do you expect to bet nothin'?")
                return

            amount = int(amount)
            if amount > guild_data['users'][user_id]['wallet']:
                await ctx.message.reply("HA, you're broke. ")
                return

            if amount < 0:
                await ctx.message.reply("Currency in negative value??")
                return

            embed = discord.Embed(title='Slot Machine')
            final = []
            for i in range(4):
                if i == 1:
                    a = random.choice(
                        ["🍉", "🍓", "🍔", "🍗", "🍵"])
                    final.append(a)
                    embed.add_field(
                        name=f'[{final[0]}', value='\u200b')
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.set_footer(
                        text="Tip: When all 3 slots are equal,\n you can earn upto 2 times\n the amount you bet!")

                    message = await ctx.message.reply(embed=embed)
                if i == 2:
                    a = random.choice(
                        ["🍉", "🍓", "🍔", "🍗", "🍵", "🥘"])
                    final.append(a)
                    embed.add_field(
                        name=f'|{final[1]}', value='\u200b')

                    await message.edit(embed=embed)

                if i == 3:
                    a = random.choice(
                        ["🍉", "🍓", "🍔", "🍗", "🍵", "🥘"])
                    final.append(a)
                    embed.add_field(
                        name=f'|{final[2]}]  Reels Spun...', value='\u200b')
                    await message.edit(embed=embed)

            if final[0] == final[1] and final[2] == final[1] and final[0] == final[2]:

                b = random.choice([3, 3.5, 4])
                bamount = math.trunc(int(b*amount))
                self.update_bank(ctx.author, bamount)
                await message.edit(f'You won a lottery of **⏣{bamount:,}**')

            elif final[0] == final[1] or final[2] == final[1] or final[0] == final[2]:

                d = random.choice([1, 1.75, 2])
                damount = math.trunc(int(d*amount))
                self.update_bank(ctx.author, damount)
                await message.edit(f'God gave you **⏣{damount:,}**')

            elif final[0] != final[1] or final[2] != final[1] or final[0] != final[2]:

                c = random.choice(
                    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
                camount = math.trunc(int(c*amount))
                users = self.get_bank_data(ctx.guild.id)
                wallet = int(users["users"][str(ctx.author.id)]["wallet"])

                if wallet - camount < 0:
                    camount = wallet

                self.update_bank(ctx.author, -camount)

                await message.edit(f'Get REKT! YOU LOST **⏣{camount:,}**')
        except ValueError:
            await ctx.send("Please give proper input. Correct way to use this command is `-stock <put your amount here>`")

    @ slots.error
    async def error_slots(self, ctx, error):
        hour = int((error.retry_after/60)//(60))
        mins = int((error.retry_after-(hour*60*60))//(60))
        seconds = int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Too spicy, take a breather",
                               description=f"If I let you bet whenever you wanted, you'd be a lot more poor. Wait {seconds} seconds")
            em.set_footer(text="The default cooldown is 15 seconds")

            await ctx.message.reply(embed=em)

    @ commands.command(aliases=["steal"])
    # ROB  COMMAND
    @ commands.cooldown(1, 30, BucketType.user)
    async def rob(self, ctx, member: discord.Member):
        # try:

        guild_id = str(member.guild.id)
        users = self.get_bank_data(guild_id)
        self.open_account(ctx.author)
        self.open_account(member)

        bal = int(users["users"][str(member.id)]["wallet"])
        bal_author = int(users["users"][str(ctx.author.id)]["wallet"])

        if bal < 1000:
            await ctx.message.reply("Hey...the person you're trying to rob has less than ⏣ 1,000. It's not worth it duh.")
            return

        if bal_author <= 500:
            await ctx.message.reply("dude earn some money then rob. u need to learn to work lol(hint: you need atleast ⏣ 500 to rob someone)")

        earnings = random.randint(1, bal)
        author_earnings = random.randint(
            1, int(((40/100) * bal_author)))

        if bool(users["users"][str(member.id)]["padlock"]) == True:

            users["users"][str(ctx.author.id)]["wallet"] -= author_earnings

            await ctx.message.reply(f"You tried to rob this person, but it automatically failed for he had padlock and you didn't have bolt cutters. You paid the police **⏣ {author_earnings:,}**")
            users["users"][str(member.id)]["padlock"] = False

            Economy_MongoDB.update_one(
                {"guild_id": guild_id}, {"$set": users})

        elif bool(users["users"][str(member.id)]["padlock"]) == False:

            choice = random.choice([True, False])
            author_earnings2 = random.randint(
                1, int(((20/100) * bal_author)))

            if choice == True:
                self.update_bank(ctx.author, earnings)
                self.update_bank(member, -1*earnings)
                if earnings <= (20/100)*bal:
                    await ctx.message.reply(f"You stole a small portion!💷\nYour payout was **⏣{earnings:,}**")

                elif earnings <= (50/100)*bal and earnings >= (20/100)*bal:
                    await ctx.message.reply(f"You stole a large portion!!💰\nYour payout was **⏣{earnings:,}**")

                elif earnings <= (85/100)*bal and earnings >= (50/100)*bal:
                    await ctx.message.reply(f"You stole a SHIT TON OF MONEY!!🤑\nYour payout was **⏣{earnings:,}**")

                elif earnings <= (100/100)*bal and earnings >= (85/100)*bal:
                    await ctx.message.reply(f"You stole almost everything!! YOU ARE A GREAT THIEF!!🤑\nYour payout was **⏣{earnings:,}**")

            elif choice == False:
                self.update_bank(ctx.author, -1*author_earnings2)
                await ctx.message.reply(f"You were caught stealing. You paid to cops **⏣ {author_earnings2:,}**")
        # except ValueError:
        # await ctx.send("Please give proper input. Correct way to use this command is `-rob <the person you want to rob>`")

    @ rob.error
    async def error_rob(self, ctx, error):
        hour = int((error.retry_after/60)//(60))
        mins = int((error.retry_after-(hour*60*60))//(60))
        seconds = int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Too spicy, take a breather",
                               description=f'This person has already been robbed in the last 30 seconds.\nYou can rob again in {seconds} seconds')
            em.set_footer(text="The default cooldown is 30 seconds")

            await ctx.message.reply(embed=em)

    @commands.command(aliases=["work list"])
    async def work_list(self, ctx):
        em = discord.Embed(title="Available Jobs",
                           description="Choose a job if you haven't already!")

        for jobs in self.job_list.values():
            name = jobs["display"]
            salary = jobs["salary"]
            desc = jobs["desc"]

            em.add_field(name=name, value=f"{desc}\n\uFEFF", inline=False)
            em.set_footer(text="Page 1 of 2")

        em2 = discord.Embed(title="Available Jobs",
                            description="Choose a job if you haven't already!")
        for jobs_2 in self.job_list_2.values():
            name2 = jobs_2["display"]
            salary2 = jobs_2["salary"]
            desc2 = jobs_2["desc"]

            em2.add_field(name=name2, value=f"{desc2}\n\uFEFF", inline=False)
            em2.set_footer(text="Page 2 of 2")

        await ctx.message.reply(embed=em, components=[[Button(label="Next ⏩"), Button(label="Back 🔙")]])
        if lambda i: i.component.label.startswith('Next'):
            interaction = await self.client.wait_for("button_click", check=lambda i: i.component.label.startswith('Next'))
            await interaction.message.edit(embed=em2)
        if lambda i: i.component.label.startswith('Back'):
            interaction2 = await self.client.wait_for("button_click", check=lambda i: i.component.label.startswith('Back'))
            await interaction2.message.edit(embed=em)

        # await interaction.respond(embed=em2)

    @commands.command()
    async def work(self, ctx, *, job_name=None):

        guild_id = str(ctx.guild.id)
        user_id = str(ctx.author.id)
        self.open_account(ctx.author)
        if job_name != None:
            job_name = job_name.lower()

        guild_data = self.get_bank_data(guild_id)

        if job_name == None and guild_data['users'][user_id]['job']['job_name'] == None:
            await ctx.message.reply(f"LMAO you're unemployed. Get a job idiot (Tip: Use `-work_list` to see available jobs :P)")
            return
        elif job_name != None and job_name not in self.job_list and self.job_list_2:
            await ctx.message.reply(f"lol this job does not exist, try getting another job hehe")
            return

        elif job_name != guild_data['users'][user_id]['job']['job_name']:
            guild_data['users'][user_id]['job']['job_name'] = job_name
            guild_data['users'][user_id]['job']['hours_worked'] = 0

        if job_name != None and job_name in self.job_list:
            hours_needed = self.job_list[job_name]["hours_needed"]
            salary = self.job_list[job_name]["salary"]
            await ctx.message.reply(f"{ctx.author.mention} Congratulations, you are now working as a **{(guild_data['users'][user_id]['job']['job_name']).title()} **!\nYou're required to work at least **{hours_needed} times** a day via `-work`, or you'll be fired.\nYou start now, and your salary(the amount of coins you get per hour of work) is ⏣ {salary:,} per hour.")
            return
        elif job_name != None and job_name in self.job_list_2:
            hours_needed = self.job_list_2[job_name]["hours_needed"]
            salary = self.job_list_2[job_name]["salary"]
            await ctx.message.reply(f"{ctx.author.mention} Congratulations, you are now working as a **{(guild_data['users'][user_id]['job']['job_name']).title()} **!\nYou're required to work at least **{hours_needed} times** a day via `-work`, or you'll be fired.\nYou start now, and your salary(the amount of coins you get per hour of work) is ⏣ {salary:,} per hour.")
            return

        if job_name == guild_data['users'][user_id]['job']['job_name'] and guild_data['users'][user_id]['job']['job_name'] != None:
            await ctx.message.reply(f"lol your already working as a `{guild_data['users'][user_id]['job']['job_name']}` just type `-work` to start working or type `-work resign` to resign your post")
            return
        if job_name == None and guild_data['users'][user_id]['job']['job_name'] == "discord mod":

            # , "Retype", "Color Match", "Reverse", "Scramble", "Soccer"]
            game_choice = random.choice["Hangman"]
            if game_choice == "Hangman":
                def get_word():
                    word = random.choice(title_choices.word_list)
                    return word.upper()

                async def play(word):

                    word_completion = "_" * len(word)
                    guessed = False
                    guessed_letters = []
                    guessed_words = []
                    tries = 6
                    embed = discord.Embed(
                        title="Let's play Hangman!", description=f"{display_hangman}\n{word_completion}")
                    message = await ctx.message.reply(embed=embed)
                    while not guessed and tries > 0:
                        guess = ctx.author.message.upper()
                        if len(guess) == 1 and guess.isalpha():
                            if guess in guessed_letters:
                                await ctx.message.reply(f"You already guessed that letter! `{guess}`")
                            elif guess not in word:
                                await ctx.message.reply(f"`{guess}` is not in the word.")
                                tries -= 1
                                guessed_letters.append(guess)
                            else:
                                await ctx.message.reply(f"Good job mate, `{guess}` is in the word!")
                                guessed_letters.append(guess)
                                word_as_list = list(word_completion)
                                indices = [i for i, letter in enumerate(
                                    word) if letter == guess]
                                for index in indices:
                                    word_as_list[index] = guess
                                word_completion = "".join(word_as_list)
                                if "_" not in word_completion:
                                    guessed = True

                        elif len(guess) == len(word) and guess.isalpha():
                            if guess in guessed_words:
                                await ctx.message.reply(f"bruh you already guessed that word `{guess}`")
                            elif guess != word:
                                await ctx.message.reply(f"`{guess}` is not the word")
                                tries -= 1
                                guessed_words.append(guess)
                            else:
                                guessed = True
                                word_completion = word

                        else:
                            embed2 = discord.Embed(
                                title="Not a valid guess", description=f"{display_hangman(tries)}\n{word_completion}")
                            await message.edit(embed2)
                    if guessed:
                        await ctx.message.reply("Congrats, you guessed the word")

                    else:
                        await ctx.message.reply(f"slow brains, you ran out of tries. The word was {word}")

                def display_hangman(tries):
                    stages = [  # final state: head, torso, both arms, and both legs
                        """
                                            --------
                                            |      |
                                            |      O
                                            |     \\|/
                                            |      |
                                            |     / \\
                                            -
                                        """,
                        # head, torso, both arms, and one leg
                        """
                                            --------
                                            |      |
                                            |      O
                                            |     \\|/
                                            |      |
                                            |     /
                                            -
                                        """,
                        # head, torso, and both arms
                        """
                                            --------
                                            |      |
                                            |      O
                                            |     \\|/
                                            |      |
                                            |
                                            -
                                        """,
                        # head, torso, and one arm
                        """
                                            --------
                                            |      |
                                            |      O
                                            |     \\|
                                            |      |
                                            |
                                            -
                                        """,
                        # head and torso
                        """
                                            --------
                                            |      |
                                            |      O
                                            |      |
                                            |      |
                                            |
                                            -
                                        """,
                        # head
                        """
                                            --------
                                            |      |
                                            |      O
                                            |
                                            |
                                            |
                                            -
                                        """,
                        # initial empty state
                        """
                                            --------
                                            |      |
                                            |
                                            |
                                            |
                                            |
                                            -
                                        """
                    ]
                    return stages[tries]

                def main_hangman():
                    word = get_word()
                    play(word)
                if __name__ == "__main__":
                    main_hangman()

        # or job_name in self.job_list or self.job_list_2 and self.job_list and self.job_list_2 in guild_data['users'][user_id]['job']['job_name']:

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})
        # SHOP COMMAND

    @ commands.command()
    async def shop(self, ctx):
        em = discord.Embed(title='Shop')

        for item in self.mainshop.values():
            name = item["display"]
            price = item["price"]
            desc = item["desc"]
            em.add_field(name=name,
                         value=f"⏣ {price:,} | {desc}", inline=False)

        await ctx.send(embed=em)

    @commands.command()
    async def buy(self, ctx, amount: int, item):

        self.open_account(ctx.author)

        await ctx.message.reply(await self.buy_item(ctx.author, item, amount))

    @commands.command(aliases=['inv', 'inventory'])
    async def bag(self, ctx, user: discord.Member = None):

        user = user or ctx.author
        self.open_account(user)

        guild_data = self.open_account(user)

        inv = guild_data["users"][str(user.id)]["inv"]

        em = discord.Embed(title="Items in your Bag💰")

        for key, value in inv.items():
            em.add_field(
                name=self.mainshop[key]['display'].title(), value=value, inline=False)

        await ctx.message.reply(embed=em)

    async def buy_item(self, user, item, amount=1):
        guild_id = str(user.guild.id)
        user_id = str(user.id)
        item = item.lower()

        if item not in self.mainshop:
            return "What are you trying to buy idiot? tbh that item isn't there in the shop"

        if amount <= 0:
            return "Amount on steroids! You need a doc's consultation."

        cost = amount * self.mainshop[item]['price']

        guild_data = self.get_bank_data(guild_id)

        if guild_data['users'][user_id]['wallet'] < cost:
            return f"You don't have enough money in your wallet to buy **{amount:,} {self.mainshop[item]['display']}**"

        if item in guild_data['users'][user_id]['inv']:
            guild_data['users'][user_id]['inv'][item] += amount
        else:
            guild_data['users'][user_id]['inv'][item] = amount

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        self.update_bank(user, -cost, "wallet")

        return f"You just bought **{amount} {self.mainshop[item]['display']}** for **⏣ {cost:,}**"

    @commands.command()
    async def use(self, ctx, amount: int, item):

        user = ctx.author
        self.open_account(user)
        guild_id = str(user.guild.id)
        guild_data = self.get_bank_data(guild_id)
        user_id = str(user.id)
        bank_space = random.randint(15000, 25000)
        item = item.lower()

        if amount <= 0:
            await ctx.message.reply(f"bruh...when ur in a shop do you buy **{amount}** chocolates? Go study elementary mathematics once more")
            return
        elif item in guild_data['users'][user_id]['inv'] and guild_data['users'][user_id]['inv'][item] >= amount:
            guild_data['users'][user_id]['inv'][item] -= amount

        else:
            await ctx.message.reply("What are you trying to use idiot? tbh that item isn't there in your inventory")
            return

        if item == "banknote":

            guild_data['users'][user_id]["bank_space"] += (amount*bank_space)
            await ctx.message.reply(f"The bank officials inreased your bankspace by **⏣ {amount*bank_space:,}**")

        if item == "padlock":
            if guild_data['users'][user_id]["padlock"]:
                await ctx.message.reply("You can't use this item, you've already used it and it's active right now!")
                guild_data['users'][user_id]['inv'][item] += amount
            else:
                guild_data['users'][user_id]["padlock"] = True
                await ctx.message.reply("Your wallet now has a padlock on it. Anyone who tries to steal from you will automatically fail if they don't have bolt cutters, however this is only a one-time use.")

        if guild_data['users'][user_id]['inv'][item] == 0:
            del guild_data['users'][user_id]['inv'][item]

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        '''if guild_data['users'][user_id]['inv'][item] == 0:
            Economy_MongoDB.remove({"guild_id": guild_id}, {
                                   "$unset": item})'''

    @commands.command()
    async def sell(self, ctx, amount: int, item):
        self.open_account(ctx.author)

        await ctx.message.reply(await self.sell_item(ctx.author, item, amount))

    async def sell_item(self, user, item, amount=1):

        guild_id = str(user.guild.id)
        user_id = str(user.id)
        item = item.lower()
        guild_data = self.get_bank_data(guild_id)

        if item not in guild_data["users"][user_id]["inv"]:
            return "What are you trying to sell idiot? tbh you don't own that item"

        if amount <= 0:
            return "Amount on steroids! You need a doc's consultation."

        if amount > guild_data["users"][user_id]["inv"][item]:
            return "bruh you're tryin to sell more than what you own"

        item_price = int(self.mainshop[item]['price'])
        cost = int((60/100)*(amount * item_price))

        if item in guild_data['users'][user_id]['inv']:
            guild_data['users'][user_id]['inv'][item] -= amount
        else:
            guild_data['users'][user_id]['inv'][item] = amount

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        self.update_bank(user, int(cost), "wallet")

        return f"You just Sold **{amount} {self.mainshop[item]['display']}** for **⏣ {cost:,}**"

    @commands.command(aliases=["rich"])
    async def wealthy(self, ctx):
        self.open_account(ctx.author)
        user_id = str(ctx.author.id)
        guild_id = ctx.guild.id
        guild_data = self.get_bank_data(guild_id)
        users_data = guild_data["users"]

        user_ids_sorted = sorted(
            users_data, key=lambda _user_id: users_data[_user_id]["wallet"] + users_data[_user_id]["bank"], reverse=True)
        lb = []
        sep = "\n"

        rank = 1
        # embed = discord.Embed(title="Leaderboard(XP):")

        award = {1: ':first_place:', 2: ':second_place:', 3: ':third_place:'}
        for uid in user_ids_sorted:
            try:
                temp_user = ctx.guild.get_member(int(uid))
                lb.append(
                    f"{award[rank] if rank in award else ':small_blue_diamond:'} **{guild_data['users'][uid]['wallet'] + guild_data['users'][uid]['bank']:,}** - {temp_user.mention}")
                # embed.add_field(
                # name=f"{rank}: {temp_user.name}", value=f"Total XP: {stats['users'][uid]['xp']}", inline=False)
                # embed.set_thumbnail(url=str(ctx.guild.icon_url))

                rank += 1
            except:
                rank -= 1

            if rank >= 10:
                break
        em = discord.Embed(title=f"Richest users in {ctx.guild.name}", description=f'{sep.join(lb)}',
                           color=discord.Color(0xfa43ee))
        em.set_thumbnail(url=str(ctx.guild.icon_url)
                         )

        em.set_footer(text="This is the net-worth")

        await ctx.message.reply(embed=em)


def setup(client):
    client.add_cog(Economy(client))
