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

    mainshop = [{"Name": "Watch""⌚", "Price": 800, "Description": "Time"},
                {"Name": "Laptop""💻", "Price": 10000, "Description": "Work"},
                {"Name": "Gaming PC""🎮", "Price": 200000, "Description": "Gaming"}]

    async def update_bank(self, user, change=0, mode="wallet"):  # UPDATE BANK
        users = await self.get_bank_data()
        users[str(user.id)][mode] += change

        with open("Supporting/mainbank.json", "w") as f:
            json.dump(users, f)
        bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
        return bal

    async def open_account(self, user):  # OPEN ACCOUNT VARIABLE
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

    async def get_bank_data(self):  # GET BANK DATA
        with open("Supporting/mainbank.json", "r") as f:
            users = json.load(f)

        return users

    @commands.command(aliases=["with", "draw"])
    # WITHDRAW COMMAND
    async def withdraw(self, ctx, amount=None):
        await self.open_account(ctx.author)

        if amount == None:
            await ctx.send("How on Earth do you expect to withdraw absolutly nothing?")
            return
        bal = await self.update_bank(ctx.author)
        users = await self.get_bank_data()
        if amount == 'all':
            amount = int(users[str(ctx.author.id)]["bank"])

        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("HA, you're broke. ")
            return

        if amount < 0:
            await ctx.send("Currency in negative value??")
            return

        await self.update_bank(ctx.author, amount)
        await self.update_bank(ctx.author, -1*amount, "bank")
        users2 = await self.get_bank_data()
        amount_left = int(users2[str(ctx.author.id)]["bank"])
        await ctx.send(f"You just placed **⏣{amount}** in your wallet! Current balance in your bank is **⏣{amount_left}**")

    @commands.command(aliases=["dep", "depp"])
    # DEPOSIT COMMAND
    async def deposit(self, ctx, amount=None):
        await self.open_account(ctx.author)

        if amount == None:
            await ctx.send("How on Earth do you expect to deposit absolutly nothing?")
            return
        bal = await self.update_bank(ctx.author)
        # bank_amt = await self.get_bank_data()[str(ctx.author.id)]["bank"]
        users = await self.get_bank_data()
        if amount == 'all':
            amount = int(users[str(ctx.author.id)]["wallet"])

        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("HA, you're broke.")
            return

        if amount < 0:
            await ctx.send("Currency in negative value??")
            return

        await self.update_bank(ctx.author, -1*amount)
        await self.update_bank(ctx.author, amount, "bank")
        users2 = await self.get_bank_data()
        amount_left = int(users2[str(ctx.author.id)]["wallet"])
        await ctx.send(f"You deposited **⏣{amount}** to the bank!\nCurrent balance in wallet is **⏣{amount_left}**")

    @commands.command(aliases=["give", "donate"])
    # SEND COMMAND
    async def send(self, ctx, member: discord.Member, amount=None):
        await self.open_account(ctx.author)
        await self.open_account(member)

        if amount == None:
            await ctx.send("How on Earth do you send someone absolutly nothing?")
            return
        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("HA, you're broke. ")
            return

        if amount < 0:
            await ctx.send("Currency in negative value??")
            return

        await self.update_bank(ctx.author, -1*amount, "bank")
        await self.update_bank(member, amount, "bank")
        await ctx.send(f"You sent **⏣{amount}** to {member.mention}'s the bank!")

    @commands.command(aliases=["bal"])
    # BALANCE COMMAND
    async def balance(self, ctx, member: discord.Member = None):
        if member == None:
            user = ctx.author
            await self.open_account(ctx.author)

        else:
            user = member
            await self.open_account(member)

        users = await self.get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(
            title=f"{user.name}'s Balance", color=discord.Color.purple())
        em.add_field(name="Wallet Balance",
                     value=f'**⏣{wallet_amt}**', inline=False)
        em.add_field(name="Bank Balance",
                     value=f'**⏣{bank_amt}**', inline=False)
        await ctx.send(embed=em)
    # BEG COMMAND

    @commands.command()
    async def beg(self, ctx):
        await self.open_account(ctx.author)

        users = await self.get_bank_data()
        user = ctx.author

        earnings = random.randrange(101)

        await ctx.send(f"Oh you poor little beggar, take **⏣{earnings}**!")
        users[str(user.id)]["wallet"] += earnings
        with open("Supporting/mainbank.json", "w") as f:
            json.dump(users, f)

    # STOCK/BET COMMAND

    @commands.command()
    async def stock(self, ctx, amount=None):
        await self.open_account(ctx.author)

        if amount == None:
            await ctx.send("How on Earth do you expect to bet so less?")
            return
        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("HA, you're broke. ")
            return

        if amount < 0:
            await ctx.send("Currency in negative value??")
            return
        final = []
        for i in range(3):
            a = random.choice(["X", "O", "A"])

            final.append(a)

        await ctx.send(str(final))

        if len(set(final)) < 3:

            b = random.choice([1, 10, 50, 100])
            bamount = b*amount
            await self.update_bank(ctx.author, bamount)
            await ctx.send(f'What good day must it be for you! God just showered you with **⏣{bamount}**')

        else:
            c = random.choice([-1, -2, -3])
            camount = c*amount
            await self.update_bank(ctx.author, camount)

            await ctx.send(f'Get REKT! YOU LOST **⏣{abs(camount)}**')

    @commands.command()
    # ROB  COMMAND
    async def rob(self, ctx, member: discord.Member):
        await self.open_account(ctx.author)
        await self.open_account(member)

        bal = await self.update_bank(member)

        if bal[0] < 1000:
            await ctx.send("Hey...the person you're trying to rob has less than ⏣1,000. It's not worth it duh.")
            return

        earnings = random.randrange(0, bal[0])

        await self.update_bank(ctx.author, earnings)
        await self.update_bank(member, -1*earnings)
        if earnings <= (20/100)*bal[0]:
            await ctx.send(f"You stole a small portion!💷\nYour payout was **⏣{earnings}**")
        elif earnings <= (50/100)*bal[0] and earnings >= (20/100)*bal[0]:
            await ctx.send(f"You stole a large portion!!💰\nYour payout was **⏣{earnings}**")
        elif earnings <= (85/100)*bal[0] and earnings >= (50/100)*bal[0]:
            await ctx.send(f"You stole a SHIT TON OF MONEY!!🤑\nYour payout was **⏣{earnings}**")
        elif earnings <= (100/100)*bal[0] and earnings >= (85/100)*bal[0]:
            await ctx.send(f"You stole almost everything!! YOU ARE A GREAT THIEF!!🤑\nYour payout was **⏣{earnings}**")

    # SHOP COMMAND

    @commands.command()
    async def shop(self, ctx):
        em = discord.Embed(title='Shop')

        for item in self.mainshop:
            name = item["Name"]
            price = item["Price"]
            desc = item["Description"]
            em.add_field(name=name, value=f"⏣{price} | {desc}", inline=False)

        await ctx.send(embed=em)

    @commands.command()
    async def buy(self, ctx, item, amount=1):
        await self.open_account(ctx.author)

        res = await self.buy_this(ctx.author, item, amount)

        if not res[0]:
            if res[1] == 1:
                await ctx.send("What are you trying to buy idiot? tbh that item isn't there in the shop")
                return
            if res[1] == 2:
                await ctx.send(f"You don't have enough money in your wallet to buy **{amount} {item}**")
                return

        await ctx.send(f"You just bought **{amount} {item}**")

    @commands.command()
    async def bag(self, ctx):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []

        em = discord.Embed(title="Items in your Bag💰")
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            em.add_field(name=name, value=amount, inline=False)

        await ctx.send(embed=em)

    async def buy_this(self, user, item_name, amount):
        item_name = item_name.lower()
        name_ = None
        for item in self.mainshop:
            name = item["Name"].lower()[:-1]
            if name == item_name:
                name_ = name
                price = item["Price"]
                break

        if name_ == None:
            return [False, 1]

        cost = price*amount

        users = await self.get_bank_data()

        bal = await self.update_bank(user)

        if bal[0] < cost:
            return [False, 2]

        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt + amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index += 1
            if t == None:
                obj = {"item": item_name, "amount": amount}
                users[str(user.id)]["bag"].append(obj)
        except:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"] = [obj]

        with open("Supporting/mainbank.json", "w") as f:
            json.dump(users, f)

        await self.update_bank(user, cost*-1, "wallet")

        return [True, "Worked"]

    @commands.command()
    async def sell(self, ctx, item, amount=1):
        await self.open_account(ctx.author)

        res = await self.sell_this(ctx.author, item, amount)

        if not res[0]:
            if res[1] == 1:
                await ctx.send("What are you trying to sell idiot? tbh that item isn't there in the shop")
                return
            if res[1] == 2:
                await ctx.send(f"You don't have {amount} {item} in your bag.")
                return
            if res[1] == 3:
                await ctx.send(f"You don't have {item} in your bag.")
                return

        await ctx.send(f"You just sold {amount} {item}.")

    async def sell_this(self, user, item_name, amount, price=None):
        item_name = item_name.lower()
        name_ = None
        for item in self.mainshop:
            name = item["Name"].lower()[:-1]
            if name == item_name:
                name_ = name
                if price == None:
                    price = 50/100 * item["Price"]
                break

        if name_ == None:
            return [False, 1]

        cost = price*amount

        users = await self.get_bank_data()

        bal = await self.update_bank(user)

        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt - amount
                    if new_amt < 0:
                        return [False, 2]
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index += 1
            if t == None:
                return [False, 3]
        except:
            return [False, 3]

        with open("Supporting/mainbank.json", "w") as f:
            json.dump(users, f)

        await self.update_bank(user, cost, "wallet")

        return [True, "Worked"]

    @commands.command(aliases=["lb", "rich"])
    async def wealthy(self, ctx, x=10):
        users = await self.get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total, reverse=True)

        em = discord.Embed(title=f"Top {x} Richest People",
                           description="This is WALLETs, not net worth or bank balance", color=discord.Color(0xfa43ee))
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = ctx.bot.get_user(id_)
            name = member.name
            em.add_field(name=f"{index}. {name}",
                         value=f"{amt}",  inline=False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed=em)
# client.run('ODQ0ODEzMzE2NTA1MDc1NzEy.YKX3tg.0eYGwHfkQMKEbF71c8dVDmGVlBI')


def setup(client):
    client.add_cog(Economy(client))
