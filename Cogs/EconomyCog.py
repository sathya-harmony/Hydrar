
from operator import index
from typing import Text
from discord import user
from discord.ext.commands import bot
from discord.ext.commands.cooldowns import BucketType
from discord_components.dpy_overrides import send
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
from io import BytesIO
import asyncio
import asyncpraw
import aiohttp


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

    job_list = {'discord mod': {"display": "<:tick:892291436232446002> Discord Mod", "salary": 10000, "hours_needed": 0,
                                'desc': 'Hours Required Per Day: `0` — Salary: `⏣ 10000 per hour`'},
                'babysitter': {"display": "<:tick:892291436232446002> Babysitter", "salary": 10500, "hours_needed": 1,
                               'desc': 'Hours Required Per Day: `1` — Salary: `⏣ 10500 per hour`'},
                'fast food cook': {"display": "<:tick:892291436232446002> Fast Food Cook", "salary": 11111, "hours_needed": 2,
                                   'desc': 'Hours Required Per Day: `2` — Salary: `⏣ 11111 per hour`'},
                'house wife': {"display": "<:tick:892291436232446002> House Wife", "salary": 12000, "hours_needed": 2,
                               'desc': 'Hours Required Per Day: `2` — Salary: `⏣ 12000 per hour`'},
                'twitch streamer': {"display": "<:tick:892291436232446002> Twitch Streamer", "salary": 15000, "hours_needed": 3,
                                    'desc': 'Hours Required Per Day: `3` — Salary: `⏣ 15000 per hour`'}}
    job_list_2 = {'youtuber': {"display": "<:tick:892291436232446002> YouTuber", "salary": 16000, "hours_needed": 3,
                               'desc': 'Hours Required Per Day: `3` — Salary: `⏣ 16000 per hour`'},
                  'professional hunter': {"display": "<:tick:892291436232446002> Professional Hunter", "salary": 17000, "hours_needed": 4,
                                          'desc': 'Hours Required Per Day: `4` — Salary: `⏣ 17000 per hour`'},
                  'professional fisherman': {"display": "<:tick:892291436232446002> Twitch Streamer", "salary": 18000, "hours_needed": 4,
                                             'desc': 'Hours Required Per Day: `4` — Salary: `⏣ 18000 per hour`'},
                  'bartender': {"display": "<:tick:892291436232446002> Bartender", "salary": 19000, "hours_needed": 4,
                                'desc': 'Hours Required Per Day: `4` — Salary: `⏣ 19000 per hour`'},
                  'robber': {"display": "<:tick:892291436232446002> Robber", "salary": 20000, "hours_needed": 4,
                             'desc': 'Hours Required Per Day: `4` — Salary: `⏣ 20000 per hour`'}}
    job_list_3 = {'police officer': {"display": "<:tick:892291436232446002> Police Officer", "salary": 21000, "hours_needed": 5,
                                     'desc': 'Hours Required Per Day: `5` — Salary: `⏣ 21000 per hour`'},
                  'teacher': {"display": "<:tick:892291436232446002> Teacher", "salary": 22000, "hours_needed": 5,
                              'desc': 'Hours Required Per Day: `5` — Salary: `⏣ 22000 per hour`'},
                  'musician': {"display": "<:tick:892291436232446002> Musician", "salary": 23000, "hours_needed": 5,
                               'desc': 'Hours Required Per Day: `5` — Salary: `⏣ 23000 per hour`'},
                  'hydrargyrum shopkeeper': {"display": "<:tick:892291436232446002> Hydrargyrum Shopkeeper", "salary": 24000, "hours_needed": 5,
                                             'desc': 'Hours Required Per Day: `5` — Salary: `⏣ 24000 per hour`'},
                  'pro gamer': {"display": "<:tick:892291436232446002> Pro Gamer", "salary": 25000, "hours_needed": 5,
                                'desc': 'Hours Required Per Day: `5` — Salary: `⏣ 25000 per hour`'}}
    job_list_4 = {'manager': {"display": "<:x_:892769246319357962> Manager", "salary": 26000, "hours_needed": 5,
                                     'desc': 'Hours Required Per Day: `5` — Salary: `⏣ 26000 per hour`'},
                  'developer': {"display": "<:x_:892769246319357962> Developer", "salary": 27000, "hours_needed": 6,
                              'desc': 'Hours Required Per Day: `6` — Salary: `⏣ 27000 per hour`'},
                  'day trader': {"display": "<:x_:892769246319357962> Day Trader", "salary": 28000, "hours_needed": 6,
                               'desc': 'Hours Required Per Day: `6` — Salary: `⏣ 28000 per hour`'},
                  'santa claus': {"display": "<:x_:892769246319357962> Santa Claus", "salary": 29000, "hours_needed": 6,
                                             'desc': 'Hours Required Per Day: `6` — Salary: `⏣ 29000 per hour`'},
                  'politician': {"display": "<:x_:892769246319357962> Politician", "salary": 30000, "hours_needed": 6,
                                'desc': 'Hours Required Per Day: `6` — Salary: `⏣ 30000 per hour`'}}
    job_list_5 = {'veterinarian': {"display": "<:x_:892769246319357962> Vetrinarian", "salary": 31000, "hours_needed": 6,
                              'desc': 'Hours Required Per Day: `6` — Salary: `⏣ 31000 per hour`'},
                  'mathematician': {"display": "<:x_:892769246319357962> Mathematician", "salary": 32000, "hours_needed": 6,
                                'desc': 'Hours Required Per Day: `6` — Salary: `⏣ 32000 per hour`'},
                  'lawyer': {"display": "<:x_:892769246319357962> Lawyer", "salary": 35000, "hours_needed": 7,
                                 'desc': 'Hours Required Per Day: `7` — Salary: `⏣ 35000 per hour`'},
                  'doctor': {"display": "<:x_:892769246319357962> Doctor", "salary": 40000, "hours_needed": 7,
                                             'desc': 'Hours Required Per Day: `7` — Salary: `⏣ 40000 per hour`'},
                  'scientist': {"display": "<:x_:892769246319357962> Scientist", "salary": 30000, "hours_needed": 7,
                                 'desc': 'Hours Required Per Day: `7` — Salary: `⏣ 30000 per hour`'}}

    def format_word_completion(self, word_completion):
        return "** \n" + '\u205F'.join(word_completion) + "**"

    def get_word(self):
        word = random.choice(title_choices.word_list)
        return word.upper()

    async def play(self, ctx, word):
        guild_id = str(ctx.guild.id)
        user_id = str(ctx.author.id)
        guild_data = self.get_bank_data(guild_id)
        job_name = guild_data['users'][user_id]['job']["job_name"]

        word_completion = ["\_"] * len(word)

        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        embed = discord.Embed(
            title="Let's play Hangman!", description=self.format_word_completion(word_completion))
        embed.set_thumbnail(url=f"{await self.display_hangman(tries)}")
        msg = await ctx.message.reply(embed=embed)
        try:
            while not guessed and tries > 0:
                def check(msg3):
                    return msg3.author.id == ctx.author.id and msg3.channel.id == ctx.channel.id

                msg2 = await self.client.wait_for('message', check=check, timeout=15.0)

                guess = msg2.content.upper()

                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters:
                        embed3 = discord.Embed(
                            title=f"You've already guessed that letter `{guess}`", description=self.format_word_completion(word_completion))
                        embed3.set_thumbnail(url=f"{await self.display_hangman(tries)}")
                        await msg.edit(embed=embed3)
                    elif guess not in word:

                        tries -= 1
                        guessed_letters.append(guess)
                        embed7 = discord.Embed(
                            title=f"`{guess}` is not in the word :angry:", description=self.format_word_completion(word_completion))
                        embed7.set_thumbnail(url=f"{await self.display_hangman(tries)}")
                        await msg.edit(embed=embed7)
                    else:

                        guessed_letters.append(guess)
                        # word_as_list = list(word_completion)
                        '''indices = [i for i, letter in enumerate(
                            word) if letter == guess]
                        for index in indices:
                            # word_as_list[index] = guess
                            word_completion[index] = guess'''

                        for index, letter in enumerate(word):
                            if letter == guess:
                                word_completion[index] = guess

                        # word_completion = "** **\n**" + '\u205F'.join(word_as_list)
                        '''if "** **\n**" + \
                                '\u205F'.join(["\_"]) or '\u205F'.join(["\_"]) not in word_completion:
                            guessed = True'''

                        if '\_' not in word_completion:
                            guessed = True

                        embed4 = discord.Embed(
                            title=f"Great! `{guess}` is in the word!", description=self.format_word_completion(word_completion))

                        embed4.set_thumbnail(url=await self.display_hangman(tries))
                        await msg.edit(embed=embed4)

                elif len(guess) == len(word) and guess.isalpha():
                    if guess in guessed_words:
                        embed5 = discord.Embed(
                            title=f"Bruh you've already guessed that word", description=self.format_word_completion(word_completion))
                        embed5.set_thumbnail(url=await self.display_hangman(tries))
                        await msg.edit(embed=embed5)
                    elif guess != word:

                        tries -= 1
                        guessed_words.append(guess)
                        embed6 = discord.Embed(
                            title=f"`{guess}` is not the word!", description=self.format_word_completion(word_completion))
                        embed6.set_thumbnail(url=f"{await self.display_hangman(tries)}")
                        await msg.edit(embed=embed6)
                    else:
                        guessed = True
                        word_completion = word

                else:
                    embed2 = discord.Embed(
                        title="Not a valid guess", description=self.format_word_completion(word_completion))
                    file = await self.display_hangman(tries)
                    embed2.set_thumbnail(url=f"{file}")
                    await msg.edit(embed=embed2)
            if guessed:
                await ctx.send(f"Congrats, you guessed the word **{word}**")

            else:
                await ctx.send(f"slow brains, you ran out of tries. The word was **{word}**")
        except asyncio.TimeoutError:
            if job_name in self.job_list:
                salary = int(self.job_list[job_name]['salary'])
                cut_off = random.choice([1.5, 1.75, 1.96, 1.99, 2.12, 2.25])
                amount = int(salary / cut_off)

            elif job_name in self.job_list_2:
                salary = int(self.job_list_2[job_name]['salary'])
                cut_off = random.choice([1.5, 1.75, 1.96, 1.99, 2.12, 2.25])
                amount = int(salary / cut_off)

            elif job_name in self.job_list_3:
                salary = int(self.job_list_3[job_name]['salary'])
                cut_off = random.choice([1.5, 1.75, 1.96, 1.99, 2.12, 2.25])
                amount = int(salary / cut_off)
            self.update_bank(ctx.author, amount, overwrite=True)

            embed = discord.Embed(title=f"Terrible Effort, {ctx.author}!",
                                  description=f'You lost the mini-game because you ran out of time.\nYou were given {amount} for a sub-par hour of work.')
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    async def display_hangman(self, tries):

        # discord.File("Cogs/Pics/1.png")
        none_1 = "https://media.discordapp.net/attachments/891700939176673321/891701020370042890/1.png"
        # discord.File("Cogs/Pics/2.png")
        head_2 = "https://media.discordapp.net/attachments/891700939176673321/891701022135824384/2.png"
        # discord.File("Cogs/Pics/3.png")
        head_body_3 = "https://media.discordapp.net/attachments/891700939176673321/891701022723022848/3.png"
        # discord.File("Cogs/Pics/4.png")
        head_body_hand_4 = "https://media.discordapp.net/attachments/891700939176673321/891701024874721320/4.png"
        # discord.File("Cogs/Pics/5.png")
        head_body_hand_5 = "https://media.discordapp.net/attachments/891700939176673321/891701026552430632/5.png"
        # discord.File("Cogs/Pics/6.png")
        head_body_hand_leg_6 = "https://media.discordapp.net/attachments/891700939176673321/891701027261280286/6.png"
        # discord.File("Cogs/Pics/7.png")
        head_body_hand_leg_7 = "https://media.discordapp.net/attachments/891700939176673321/891701029207441438/7.png"

        stages = [head_body_hand_leg_7, head_body_hand_leg_6, head_body_hand_5, head_body_hand_4, head_body_3, head_2, none_1

                  ]
        return stages[tries]

    async def main_hangman(self, ctx):
        word = self.get_word()
        await self.play(ctx=ctx, word=word)

    def get_sentence(self):
        sentence = random.choice(title_choices.sentence_list)
        return sentence

    async def retype(self, ctx, sentence):
        msg = await ctx.message.reply(f"Retype the following Phrase:-\n**{sentence}**")
        try:
            def check(msg3):
                    return msg3.author.id == ctx.author.id and msg3.channel.id == ctx.channel.id

            msg2 = await self.client.wait_for('message', check=check, timeout=10)

            sentence_upper = sentence.upper()
            guess = msg2.content.upper()
            if sentence_upper == guess:
                await ctx.send(f"{ctx.author.mention} Great work! You rewrote the sentence correctly.")

            else:
                await ctx.send(f"{ctx.author.mention} Terrible effort. Expected better work from you!")
        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention} Terrible effort. You were timed out.")

    async def main_retype(self, ctx):
        sentence = self.get_sentence()
        await self.retype(ctx=ctx, sentence=sentence)

    async def choose_emoji(self, ctx):
        guild_id = str(ctx.guild.id)
        user_id = str(ctx.author.id)
        guild_data = self.get_bank_data(guild_id)
        job_name = guild_data['users'][user_id]['job']["job_name"]
        emojies = ['😁', '😂', '🤣', '😃', '😅', '😆', '🥰', '😍', '😎', '🤗', '🤩',
            '🤔', '😛', '😴', '🤐', '🤑', '🤮', '😡', '🤬', '🤢', '👽', '🤖', '🙈', '☠']
        
        
        emoji_waste_list = (random.sample(emojies, 10))
        emoji_choice = random.choice(emoji_waste_list)

        '''emoji_choice = random.choice(emojies)
        emoji_waste_list = []
        f = 0
        for i in range(11):
            emoji_waste_list.append(emojies)
            index = random.randint(0, 11)
            
            if i == index:
                #emoji_waste_list.append(emoji_choice)
                emoji_waste_list.insert(index, emoji_choice)'''

        msg = await ctx.message.reply(f"**Work for {job_name}** - Emoji Match - Look at the emoji closely!\n{emoji_choice}")
        await asyncio.sleep(3)
        await msg.edit('What was the emoji?', components=[
                                                          [
                                                            (Button(style = ButtonStyle.grey,
                                                                label=emoji_waste_list[0],
                                                                
                                                                  )
                                                                  ),
                                                            (Button(style=ButtonStyle.grey,
                                                                    label=emoji_waste_list[1],
                                                                
                                                                )
                                                             
                                                             ),
                                                             (Button(style = ButtonStyle.grey,
                                                                label=emoji_waste_list[2],
                                                                
                                                                )
                                                             ),
                                                             (Button(style = ButtonStyle.grey,
                                                                label=emoji_waste_list[3],
                                                                
                                                                )
                                                             ),
                                                             (Button(style = ButtonStyle.grey,
                                                                     label=emoji_waste_list[4],
                                                                
                                                                )
                                                             )],[
                                                             (Button(style = ButtonStyle.grey,
                                                                label=emoji_waste_list[5],
                                                                
                                                                )
                                                             ),
                                                             (Button(style = ButtonStyle.grey,
                                                                label=emoji_waste_list[6],
                                                        
                                                                )
                                                             ),
                                                             (Button(style = ButtonStyle.grey,
                                                                     label=emoji_waste_list[7],
                                                                      
                                                                )
                                                             ),
                                                              (Button(style=ButtonStyle.grey,
                                                                      label=emoji_waste_list[8],
                                                                      
                                                              )
                                                               ),
                                                              (Button(style=ButtonStyle.grey,
                                                                      label=emoji_waste_list[9],
                                                                      ))
                                                              

                                                             ]
                                                        ])
        interaction = await self.client.wait_for("button_click", check = lambda i:i.component.label in emoji_waste_list,  timeout=15.0)
        if emoji_choice == interaction.component.label:
            row1 = []
            row2 = []
            for x in range(0, 5):
                if emoji_waste_list[x] == emojies:
                    row1.append(Button(label = emoji_waste_list[x], style = ButtonStyle.green, disabled = True))
                else:
                    row1.append(Button(label = emoji_waste_list[x], disabled = True))    
            for x in range(5, 10):
                  if emoji_waste_list[x] == emojies:
                    row2.append(Button(label = emoji_waste_list[x], style = ButtonStyle.green, disabled = True))
                  else: 
                      row2.append(Button(label = emoji_waste_list[x], disabled = True))
            await interaction.edit_origin(components = [row1, row2])
            #await interaction.respond(type=6)           

            
        '''buttons1 = []        
        buttons2 = []
        for i in range(5):
            buttons1.append(Button(style=ButtonStyle.grey,
                                   label=emoji_waste_list[i],
                                   ))'''

            
                       
              
                        
       
                
                
            
            
            
               
            


    def get_bank_data(self, guild_id):

        if type(guild_id) in [int, float]:
            guild_id=str(int(guild_id))

        guild_data=Economy_MongoDB.find_one(
            {"guild_id": guild_id})

        return guild_data

    def update_bank(self, user, change=0, mode="wallet", overwrite=False):

        guild_id=str(user.guild.id)
        user_id=str(user.id)
        if type(guild_id) in [int, float]:
            guild_id=str(int(guild_id))
        # UPDATE BANK
        guild_data=self.get_bank_data(guild_id)

        if overwrite:
            guild_data["users"][str(user_id)][mode]=change
        else:
            guild_data["users"][str(user_id)][mode] += change

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        return guild_data

    def open_account(self, user):
        # OPEN ACCOUNT VARIABLE
        guild_id=str(user.guild.id)
        user_id=str(user.id)

        guild_data=self.get_bank_data(guild_id)
        if type(guild_id) in [int, float]:
            guild_id=str(int(guild_id))

        if guild_data is None:
            guild_data={"guild_id": guild_id,
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
            guild_data['users'][user_id]={
                'wallet': 100, "bank": 0, "bank_space": 100, "padlock": False, "job": {"job_name": None,
                                                                                       "hours_worked": 0}, 'inv': {},  "daily": {"last_used": 0, "streak": 1}}
            Economy_MongoDB.update_one(
                {"guild_id": guild_id}, {"$set": guild_data})

        return guild_data

    @ commands.command(aliases=[])
    async def meme(self, ctx, subred='memes'):
        msg=await ctx.message.reply('Loading Meme https://tenor.com/view/hug-gif-22743155')
        '''async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                memes = str(r)
                embed = discord.Embed(color=discord.Color.purple())
                embed.set_image(
                    url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.set_footer(
                    text=f'Powered by r/Memes! | Meme requested by {ctx.author}')
                await ctx.send(embed=embed)'''

        reddit=asyncpraw.Reddit(client_id='uv7phVm3ez8QL_KF-aS0vg',
                                  client_secret='LyqQDeKxPGsxK2yrVR4pYIXXk3bXRQ',
                                  username='SathyaShrik',
                                  password='CihVirus123',
                                  user_agent='Hydra_meme')
        subreddit=await reddit.subreddit(subred)
        all_subs=[]
        top=subreddit.top(limit=300)
        async for submission in top:
            all_subs.append(submission)

        random_sub=random.choice(all_subs)
        name=random_sub.title
        url=random_sub.url
        embed=embeds.Embed(
            title=f'__{name}__', color=discord.Color.random(), timestamp=ctx.message.created_at, url=url)
        embed.set_image(url=url)
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        embed.set_footer(
            text=f'Powered by r/Memes! | Meme requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        # await ctx.send(embed=embed)await msg.edit(content=f'<https://reddit.com/r/{subreddit}/> :white_check_mark:')
        await msg.edit(embed=embed, content=f'<https://reddit.com/r/{subreddit}/> <:tick:892291436232446002>')
        return

    @ commands.command(aliases=[])
    @ commands.cooldown(1, 60*60*24, BucketType.user)
    async def daily(self, ctx):

        self.open_account(ctx.author)
        amount=25000
        users=ctx.author.name
        guild_id=str(ctx.guild.id)
        user_id=str(ctx.author.id)

        guild_data=self.get_bank_data(guild_id)
        current_time=time.time()

        user_daily=guild_data['users'][user_id]['daily']

        # You need it to be lesser than the given time for it to work. 2 days because 1 day cooldown, 1 day streak buffer.

        if current_time - 2*60*60*24 <= user_daily['last_used']:
            user_daily['streak'] += 1
        else:
            user_daily['streak']=1

        user_daily['last_used']=current_time

        streak=user_daily['streak']

        em=discord.Embed(
            title=f"Here are your daily coins, {users}!", description=f"**⏣ {amount+streak*250:,}** was placed in your wallet.", color=discord.Color.purple())
        em.set_thumbnail(url=ctx.author.avatar_url)
        em.set_footer(text=f"Streak: {streak} days(+⏣ {streak*250:,})")
        await ctx.message.reply(embed=em)
        self.update_bank(ctx.author, (amount + streak*250))

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        self.update_bank(ctx.author, amount + streak*250)

    @ daily.error
    async def error_daily(self, ctx, error):
        hour=int((error.retry_after/60)//(60))
        mins=int((error.retry_after-(hour*60*60))//(60))
        seconds=int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em=discord.Embed(
                title=f"You've already claimed your daily today, {ctx.author.name}!", description=f"Your next daily is ready in:\n**{hour} hours, {mins} minutes and {seconds} seconds**")
            em.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=em)

    @ commands.command(aliases=["with", "draw"])
    # WITHDRAW COMMAND
    async def withdraw(self, ctx, amount=None):
        try:
            self.open_account(ctx.author)

            if amount == None:
                await ctx.message.reply("How on Earth do you expect to withdraw absolutly nothing?")
                return

            users=self.get_bank_data(ctx.guild.id)
            bal=int(users["users"][str(ctx.author.id)]["bank"])
            if amount == 'all':
                amount=int(users["users"][str(ctx.author.id)]["bank"])

            amount=int(amount)
            if amount > bal:
                await ctx.message.reply("HA, you're broke.")
                return

            if amount < 0:
                await ctx.message.reply("Currency in negative value??")
                return

            self.update_bank(ctx.author, amount)
            self.update_bank(ctx.author, -1*amount, "bank")
            users2=self.get_bank_data(ctx.guild.id)
            amount_left=int(users2["users"][str(ctx.author.id)]["wallet"])
            await ctx.message.reply(f"**⏣ {amount:,}** withdrawn, current wallet balance is **⏣ {amount_left:,}**.")
        except ValueError:
            await ctx.message.reply("Please give proper input. Correct way to use this command is `-with <amount you want to withdraw from bank>`")

    @ commands.command(aliases=["dep", "depp"])
    # DEPOSIT COMMAND
    async def deposit(self, ctx, amount=None):
        try:
            self.open_account(ctx.author)

            if amount == None:
                await ctx.message.reply("How on Earth do you expect to deposit absolutly nothing?")
                return

            # bank_amt = await self.get_bank_data()[str(ctx.author.id)]["bank"]
            users=self.get_bank_data(ctx.guild.id)
            bal=int(users["users"][str(ctx.author.id)]["wallet"])
            bank_space=users["users"][str(ctx.author.id)]["bank_space"]

            if amount == 'all' and int(users["users"][str(ctx.author.id)]["wallet"]) >= int(bank_space) - int(users["users"][str(ctx.author.id)]["bank"]):
                # bal - int(bank_space)
                a=int(bank_space) -   \
                    int(users["users"][str(ctx.author.id)]["bank"])
                amount=a

            elif amount == 'all' and int(users["users"][str(ctx.author.id)]["wallet"]) <= int(bank_space) - int(users["users"][str(ctx.author.id)]["bank"]):
                amount=int(users["users"][str(ctx.author.id)]["wallet"])

            amount=int(amount)
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
            users2=self.get_bank_data(ctx.guild.id)
            amount_left=int(users2["users"][str(ctx.author.id)]["wallet"])
            await ctx.message.reply(f"**⏣ {amount:,}** deposited, current wallet balance is **⏣ {amount_left:,}**.")
        except ValueError:
            await ctx.message.reply("Please give proper input. Correct way to use this command is `-dep <amount to deposit into bank>`")

    @ commands.command(aliases=["give", "donate"])
    # SEND COMMAND
    async def send(self, ctx, member: discord.Member, amount=None):

        user=ctx.author
        self.open_account(user)
        self.open_account(member)

        if amount == None:
            await ctx.message.reply("How on Earth do you send someone absolutly nothing?")
            return
        users=self.get_bank_data(ctx.guild.id)

        bal=int(users["users"][str(ctx.author.id)]["wallet"])

        amount=int(amount)
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
    async def balance(self, ctx, member: discord.Member=None):
        if member == None:
            user=ctx.author
            self.open_account(user)

        else:
            user=member
            self.open_account(user)

        users=self.get_bank_data(ctx.guild.id)
        wallet_amt=users["users"][str(user.id)]["wallet"]
        bank_amt=users["users"][str(user.id)]["bank"]
        bank_space=users["users"][str(user.id)]["bank_space"]

        em=discord.Embed(
            title=f"{user.name}'s Balance", description=f"**Wallet**: ⏣ {wallet_amt:,}\n**Bank**: ⏣ {bank_amt:,} / {bank_space:,} `({(bank_amt/bank_space)*100}%)`", color=discord.Color.purple())

        em.set_thumbnail(url=user.avatar_url)
        await ctx.message.reply(embed=em)
    # BEG COMMAND

    @ commands.command()
    @ commands.cooldown(1, 30, BucketType.user)
    async def beg(self, ctx):
        self.open_account(ctx.author)

        users=self.get_bank_data(ctx.guild.id)
        user=ctx.author

        earnings=random.randrange(2500)
        a=[False, True]
        b=random.choice(a)
        if b is True:
            title_choice=random.choice(title_choices.names)
            description=random.choice([f"ok sure, have **⏣ {earnings:,}** coins",
                                         f"ur a bit stanky but here's **⏣ {earnings:,}** coins",
                                        f"Oh, you poor little beggar, take **⏣ {earnings:,}** coins",
                                         f"you get **⏣ {earnings:,}** COINS",
                                         f"**⏣ {earnings:,}** coins for you"])
            self.update_bank(user, earnings)

            em=discord.Embed(
                title=title_choice, set_thumbnail=ctx.author, description=description,  color=discord.Color.purple())
            em.set_thumbnail(url=str(user.avatar_url))
            em.set_footer(text="begging is everyone's right!")

            await ctx.message.reply(embed=em)
        elif b is False:
            title_choice=random.choice(title_choices.names)
            description=random.choice(title_choices.loss_message)

            em=discord.Embed(
                title=title_choice, description=description,  thumbnail=ctx.author,  color=discord.Color.purple())
            em.set_thumbnail(url=str(user.avatar_url))
            em.set_footer(text="begging is everyone's right!")

            await ctx.message.reply(embed=em)

    @ beg.error
    async def error_beg(self, ctx, error):
        hour=int((error.retry_after/60)//(60))
        mins=int((error.retry_after-(hour*60*60))//(60))
        seconds=int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em=discord.Embed(title="Too spicy, take a breather",
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
            user_id=str(ctx.author.id)

            guild_data=self.open_account(ctx.author)

            if amount == None:
                await ctx.message.reply("How on Earth do you expect to bet nothin'?")
                return

            amount=int(amount)
            if amount > guild_data['users'][user_id]['wallet']:
                await ctx.message.reply("HA, you're broke. ")
                return

            if amount < 0:
                await ctx.message.reply("Currency in negative value??")
                return

            embed=discord.Embed(title='Slot Machine')
            final=[]
            more=['🍒', '7️⃣', '🍫', '🍦', '💰', '🍔', '⚽', '💡', '💣', '💎', '✏️']
            emojis=random.sample(more, 3)
            embed=discord.Embed(
                title='Slot Machine', description=f"[{random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)}] Loading...")
            time.sleep(1)
            message=await ctx.message.reply(embed=embed)
            for _ in range(10):
                choice1=random.choice(emojis)
                choice2=random.choice(emojis)
                choice3=random.choice(emojis)

                new_embed=discord.Embed(
                    title='Slot Machine', description=f"[{choice1} | {choice2} | {choice3}] Spinning Reels...")
                await message.edit(embed=new_embed)
            newer_embed=discord.Embed(
                title="Slot Machine", description=f"[{choice1} | {choice2} | {choice3}] Reels Spun...")
            await message.edit(embed=newer_embed)
            final.append(choice1)
            final.append(choice2)
            final.append(choice3)
            time.sleep(0.3)

            '''for i in range(4):
                if i == 1:
                    a = random.choice(
                        ["🍉", "🍓", "🍔", "🍗", "🍵"])
                    # for _ in range(4): p = random.choice(["🍉", "🍓", "🍔", "🍗", "🍵"])
                    final.append(a)
                    embed.add_field(
                        name=f'[{final[0]}', value='\u205F')
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.set_footer(
                        text="Tip: When all 3 slots are equal,\n you can earn upto 2 times\n the amount you bet!")

                    message = await ctx.message.reply(embed=embed)
                if i == 2:
                    a = random.choice(
                        ["🍉", "🍓", "🍔", "🍗", "🍵", "🥘"])
                    final.append(a)
                    embed.add_field(
                        name=f'|{final[1]}', value='\u205F')

                    await message.edit(embed=embed)

                if i == 3:
                    a = random.choice(
                        ["🍉", "🍓", "🍔", "🍗", "🍵", "🥘"])
                    final.append(a)
                    embed.add_field(
                        name=f'|{final[2]}]  Reels Spun...', value='\u205F')
                    await message.edit(embed=embed)'''

            if final[0] == final[1] and final[2] == final[1] and final[0] == final[2]:

                b=random.choice([3, 3.5, 4])
                bamount=math.trunc(int(b*amount))
                self.update_bank(ctx.author, bamount)
                await message.edit(f'You won a lottery of **⏣{bamount:,}**')

            elif final[0] == final[1] or final[2] == final[1] or final[0] == final[2]:

                d=random.choice([1, 1.75, 2])
                damount=math.trunc(int(d*amount))
                self.update_bank(ctx.author, damount)
                await message.edit(f'God gave you **⏣{damount:,}**')

            elif final[0] != final[1] or final[2] != final[1] or final[0] != final[2]:

                c=random.choice(
                    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
                camount=math.trunc(int(c*amount))
                users=self.get_bank_data(ctx.guild.id)
                wallet=int(users["users"][str(ctx.author.id)]["wallet"])

                if wallet - camount < 0:
                    camount=wallet

                self.update_bank(ctx.author, -camount)

                await message.edit(f'Get REKT! YOU LOST **⏣{camount:,}**')
        except ValueError:
            await ctx.send("Please give proper input. Correct way to use this command is `-stock <put your amount here>`")

    @ slots.error
    async def error_slots(self, ctx, error):
        hour=int((error.retry_after/60)//(60))
        mins=int((error.retry_after-(hour*60*60))//(60))
        seconds=int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em=discord.Embed(title="Too spicy, take a breather",
                               description=f"If I let you bet whenever you wanted, you'd be a lot more poor. Wait {seconds} seconds")
            em.set_footer(text="The default cooldown is 15 seconds")

            await ctx.message.reply(embed=em)

    @ commands.command(aliases=["steal"])
    # ROB  COMMAND
    @ commands.cooldown(1, 30, BucketType.user)
    async def rob(self, ctx, member: discord.Member):
        # try:

        guild_id=str(member.guild.id)
        users=self.get_bank_data(guild_id)
        self.open_account(ctx.author)
        self.open_account(member)

        bal=int(users["users"][str(member.id)]["wallet"])
        bal_author=int(users["users"][str(ctx.author.id)]["wallet"])

        if bal < 1000:
            await ctx.message.reply("Hey...the person you're trying to rob has less than ⏣ 1,000. It's not worth it duh.")
            return

        if bal_author <= 500:
            await ctx.message.reply("dude earn some money then rob. u need to learn to work lol(hint: you need atleast ⏣ 500 to rob someone)")

        earnings=random.randint(1, bal)
        author_earnings=random.randint(
            1, int(((40/100) * bal_author)))

        if bool(users["users"][str(member.id)]["padlock"]) == True:

            users["users"][str(ctx.author.id)]["wallet"] -= author_earnings
            users["users"][str(member.id)]["wallet"] += author_earnings

            await ctx.message.reply(f"You tried to rob this person, but it automatically failed for he had padlock and you didn't have bolt cutters. You paid {member.mention} **⏣ {author_earnings:,}**")
            users["users"][str(member.id)]["padlock"]=False

            Economy_MongoDB.update_one(
                {"guild_id": guild_id}, {"$set": users})

        elif bool(users["users"][str(member.id)]["padlock"]) == False:

            choice=random.choice([True, False])
            author_earnings2=random.randint(
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
                await ctx.message.reply(f"YOU WERE CAUGHT **HAHAHA**. YOU PAID **⏣ {author_earnings2:,}** TO THE COPS")
        # except ValueError:
        # await ctx.send("Please give proper input. Correct way to use this command is `-rob <the person you want to rob>`")

    @ rob.error
    async def error_rob(self, ctx, error):
        hour=int((error.retry_after/60)//(60))
        mins=int((error.retry_after-(hour*60*60))//(60))
        seconds=int(error.retry_after-(hour*60*60)-(mins*60))

        if isinstance(error, commands.CommandOnCooldown):
            em=discord.Embed(title="Too spicy, take a breather",
                               description=f'This person has already been robbed in the last 30 seconds.\nYou can rob again in {seconds} seconds')
            em.set_footer(text="The default cooldown is 30 seconds")

            await ctx.message.reply(embed=em)

    @ commands.command(aliases=["worklist", "joblist", "job_list"])
    async def work_list(self, ctx):
        em=discord.Embed(title="Available Jobs",
                           description="Choose a job if you haven't already! ")

        for jobs in self.job_list.values():
            name=jobs["display"]
            salary=jobs["salary"]
            desc=jobs["desc"]

            em.add_field(name=name, value=f"{desc}\n\u205F", inline=False)
            em.set_footer(text="Page 1 of 5")

        em2=discord.Embed(title="Available Jobs",
                            description="Choose a job if you haven't already!")
        for jobs_2 in self.job_list_2.values():
            name2=jobs_2["display"]
            salary2=jobs_2["salary"]
            desc2=jobs_2["desc"]

            em2.add_field(name=name2, value=f"{desc2}\n\u205F", inline=False)
            em2.set_footer(text="Page 2 of 5")
        em3=discord.Embed(title="Available Jobs",
                            description="Choose a job if you haven't already!")
        for jobs_3 in self.job_list_3.values():
            name3=jobs_3["display"]
            salary3=jobs_3["salary"]
            desc3=jobs_3["desc"]

            em3.add_field(name=name3, value=f"{desc3}\n\u205F", inline=False)
            em3.set_footer(text="Page 3 of 5")
        em4=discord.Embed(title="Available Jobs",
                            description="Choose a job if you haven't already!")
        for jobs_4 in self.job_list_4.values():
            name4=jobs_4["display"]
            salary4=jobs_4["salary"]
            desc4=jobs_4["desc"]

            em4.add_field(name=name4, value=f"{desc4}\n\u205F", inline=False)
            em4.set_footer(text="Page 4 of 5")
        em5=discord.Embed(title="Available Jobs",
                            description="Choose a job if you haven't already!")
        for jobs_5 in self.job_list_5.values():
            name5=jobs_5["display"]
            salary5=jobs_5["salary"]
            desc5=jobs_5["desc"]

            em5.add_field(name=name5, value=f"{desc5}\n\u205F", inline=False)
            em5.set_footer(text="Page 5 of 5")


        emoji_id=892299845824544768
        emoji_id2=892299845572919297
        emoji_id3=892299845489029121
        emoji_id4=892299845975547944
        message=await ctx.message.reply(embed=em, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])

        while True:
            try:
                interaction=await self.client.wait_for("button_click", timeout=15.0)

                if ctx.author.id != interaction.author.id:
                    await interaction.respond(content=f"{interaction.author.mention} This message is not for you lmao")
                else:
                    if interaction.component.custom_id == "next":
                        await interaction.edit_origin(embed=em2, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page2", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page2", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])
                    elif interaction.component.custom_id == "back_page2":
                        await interaction.edit_origin(embed=em, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])
                    elif interaction.component.custom_id == "next_page2":
                        await interaction.edit_origin(embed=em3, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page3", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page3", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])
                    elif interaction.component.custom_id == "back_page3":
                        await interaction.edit_origin(embed=em2, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page2", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page2", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])

                    elif interaction.component.custom_id == "next_page3":
                        await interaction.edit_origin(embed=em4, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page4", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page4", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])

                    elif interaction.component.custom_id == "back_page4":
                        await interaction.edit_origin(embed=em3, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page3", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page3", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])
                    elif interaction.component.custom_id == "next_page4":
                        await interaction.edit_origin(embed=em5, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page5", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page5", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1, disabled=True))]])
                    elif interaction.component.custom_id == "back_page5":
                        await interaction.edit_origin(embed=em4, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page4", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page4", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])

                    elif interaction.component.custom_id == "doubleback":
                        await interaction.edit_origin(embed=em, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next", style=1)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1))]])

                    elif interaction.component.custom_id == "doublenext":
                        await interaction.edit_origin(embed=em5, components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=1)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page5", style=1)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page5", style=1, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=1, disabled=True))]])
            except asyncio.TimeoutError:
                await message.edit(components=[[(Button(emoji=self.client.get_emoji(emoji_id4), custom_id="doubleback", style=ButtonStyle.gray, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id), custom_id="back_page5", style=ButtonStyle.gray, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id2), custom_id="next_page5", style=ButtonStyle.gray, disabled=True)), (Button(emoji=self.client.get_emoji(emoji_id3), custom_id="doublenext", style=ButtonStyle.gray, disabled=True))]])

                break



            '''interaction2 = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "back")
            await interaction2.edit_origin(embed=em, components=[
                                                                  [
                                                                    (Button(emoji=self.client.get_emoji(emoji_id),
                                                                        custom_id="back",
                                                                            style=1)),
                                                                      (Button(emoji=self.client.get_emoji(emoji_id2),
                                                                          custom_id="next",
                                                                            style=1))]] )

            interaction = await self.client.wait_for("button_click", check = lambda i : i.custom_id == "next_page2")
            await interaction.edit_origin(embed = em3)

            interaction2 = await self.client.wait_for("button_click", check=lambda i: i.custom_id == "back_page2")
            await interaction2.edit_origin(embed=em2)'''


        '''interaction =  await self.client.wait_for("button_click", check=lambda i: i.component.label.startswith('Next'))
        await interaction.message.edit(embed=em2)

        interaction2 = await self.client.wait_for("button_click", check=lambda i: i.component.label.startswith('Back'))
        await interaction2.respond.edit_message(embed=em)'''
        \




    @ commands.command()
    async def work(self, ctx, *, job_name=None):

        guild_id=str(ctx.guild.id)
        user_id=str(ctx.author.id)
        self.open_account(ctx.author)
        if job_name != None:
            job_name=job_name.lower()

        guild_data=self.get_bank_data(guild_id)

        if job_name == "resign":
            await ctx.message.reply(f"{ctx.author.mention} You resigned from your position as **{(guild_data['users'][user_id]['job']['job_name']).title()}**. You need to wait 3 hours before you can apply for another job.")
            guild_data['users'][user_id]['job']['job_name']=None
        elif job_name is None:
            if guild_data['users'][user_id]['job']['job_name'] == None:
                await ctx.message.reply(f"LMAO you're unemployed. Get a job idiot (Tip: Use `-work_list` to see available jobs :P)")
                return
            elif guild_data['users'][user_id]['job']['job_name'] is not None:
                channel=ctx.message.channel
                '''gamechoice=random.choice(['hangman', 'retype'])
                if gamechoice == 'hangman':
                    await self.main_hangman(ctx)
                elif gamechoice == 'retype':
                    await self.main_retype(ctx)
'''
                await self.choose_emoji(ctx)

                # await self.main_hangman(ctx)

        elif job_name is not None:
            if guild_data['users'][user_id]['job']['job_name'] is not None:
                if job_name in self.job_list:
                    await ctx.message.reply(f"lol your already working as a `{guild_data['users'][user_id]['job']['job_name']}` just type `-work` to start working or type `-work resign` to resign your post")
                    return
                elif job_name in self.job_list_2:
                    await ctx.message.reply(f"lol your already working as a `{guild_data['users'][user_id]['job']['job_name']}` just type `-work` to start working or type `-work resign` to resign your post")
                    return
                elif job_name in self.job_list_3:
                    await ctx.message.reply(f"lol your already working as a `{guild_data['users'][user_id]['job']['job_name']}` just type `-work` to start working or type `-work resign` to resign your post")
                    return
                elif job_name in self.job_list_4:
                    await ctx.message.reply(f"{ctx.author.mention} This job is currently under development. Please try some other job")
                elif job_name in self.job_list_5:
                    await ctx.message.reply(f"{ctx.author.mention} This job is currently under development. Please try some other job")
                elif job_name not in self.job_list and job_name not in self.job_list_2 and job_name not in self.job_list_3:
                    await ctx.message.reply(f"lol this job does not exist, try getting another job hehe")
                    return


            elif guild_data['users'][user_id]['job']['job_name'] is None:
                    if job_name in self.job_list:
                        guild_data['users'][user_id]['job']['job_name']=job_name
                        guild_data['users'][user_id]['job']['hours_worked']=0
                        hours_needed=self.job_list[job_name]["hours_needed"]
                        salary=self.job_list[job_name]["salary"]
                        await ctx.message.reply(f"{ctx.author.mention} Congratulations, you are now working as a **{(guild_data['users'][user_id]['job']['job_name']).title()} **!\nYou're required to work at least **{hours_needed} times** a day via `-work`, or you'll be fired.\nYou start now, and your salary(the amount of coins you get per hour of work) is ⏣ {salary:,} per hour.")

                    elif job_name in self.job_list_2:
                        guild_data['users'][user_id]['job']['job_name']=job_name
                        guild_data['users'][user_id]['job']['hours_worked']=0
                        hours_needed=self.job_list_2[job_name]["hours_needed"]
                        salary=self.job_list_2[job_name]["salary"]
                        await ctx.message.reply(f"{ctx.author.mention} Congratulations, you are now working as a **{(guild_data['users'][user_id]['job']['job_name']).title()} **!\nYou're required to work at least **{hours_needed} times** a day via `-work`, or you'll be fired.\nYou start now, and your salary(the amount of coins you get per hour of work) is ⏣ {salary:,} per hour.")

                    elif job_name in self.job_list_3:
                        guild_data['users'][user_id]['job']['job_name']=job_name
                        guild_data['users'][user_id]['job']['hours_worked']=0
                        hours_needed=self.job_list_3[job_name]["hours_needed"]
                        salary=self.job_list_3[job_name]["salary"]
                        await ctx.message.reply(f"{ctx.author.mention} Congratulations, you are now working as a **{(guild_data['users'][user_id]['job']['job_name']).title()} **!\nYou're required to work at least **{hours_needed} times** a day via `-work`, or you'll be fired.\nYou start now, and your salary(the amount of coins you get per hour of work) is ⏣ {salary:,} per hour.")

        '''if job_name is None and guild_data['users'][user_id]['job']['job_name'] == "discord mod":'''

        # , "Retype", "Color Match", "Reverse", "Scramble", "Soccer"]

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})



        # SHOP COMMAND

    @ commands.command()
    async def shop(self, ctx):
        em=discord.Embed(title='Shop')

        for item in self.mainshop.values():
            name=item["display"]
            price=item["price"]
            desc=item["desc"]
            em.add_field(name=name,
                         value=f"⏣ {price:,} | {desc}", inline=False)

        await ctx.send(embed=em)

    @ commands.command()
    async def buy(self, ctx, amount: int, item):

        self.open_account(ctx.author)

        await ctx.message.reply(await self.buy_item(ctx.author, item, amount))

    @ commands.command(aliases=['inv', 'inventory'])
    async def bag(self, ctx, user: discord.Member=None):

        user=user or ctx.author
        self.open_account(user)

        guild_data=self.open_account(user)

        inv=guild_data["users"][str(user.id)]["inv"]

        em=discord.Embed(title="Items in your Bag💰")

        for key, value in inv.items():
            em.add_field(
                name=self.mainshop[key]['display'].title(), value=value, inline=False)

        await ctx.message.reply(embed=em)

    async def buy_item(self, user, item, amount=1):
        guild_id=str(user.guild.id)
        user_id=str(user.id)
        item=item.lower()

        if item not in self.mainshop:
            return "What are you trying to buy idiot? tbh that item isn't there in the shop"

        if amount <= 0:
            return "Amount on steroids! You need a doc's consultation."

        cost=amount * self.mainshop[item]['price']

        guild_data=self.get_bank_data(guild_id)

        if guild_data['users'][user_id]['wallet'] < cost:
            return f"You don't have enough money in your wallet to buy **{amount:,} {self.mainshop[item]['display']}**"

        if item in guild_data['users'][user_id]['inv']:
            guild_data['users'][user_id]['inv'][item] += amount
        else:
            guild_data['users'][user_id]['inv'][item]=amount

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        self.update_bank(user, -cost, "wallet")

        return f"You just bought **{amount} {self.mainshop[item]['display']}** for **⏣ {cost:,}**"

    @ commands.command()
    async def use(self, ctx, amount: int, item):

        user=ctx.author
        self.open_account(user)
        guild_id=str(user.guild.id)
        guild_data=self.get_bank_data(guild_id)
        user_id=str(user.id)
        bank_space=random.randint(15000, 25000)
        item=item.lower()

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
                guild_data['users'][user_id]["padlock"]=True
                await ctx.message.reply("Your wallet now has a padlock on it. Anyone who tries to steal from you will automatically fail if they don't have bolt cutters, however this is only a one-time use.")

        if guild_data['users'][user_id]['inv'][item] == 0:
            del guild_data['users'][user_id]['inv'][item]

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})


    @ commands.command()
    async def sell(self, ctx, amount: int, item):
        self.open_account(ctx.author)

        await ctx.message.reply(await self.sell_item(ctx.author, item, amount))

    async def sell_item(self, user, item, amount=1):

        guild_id=str(user.guild.id)
        user_id=str(user.id)
        item=item.lower()
        guild_data=self.get_bank_data(guild_id)

        if item not in guild_data["users"][user_id]["inv"]:
            return "What are you trying to sell idiot? tbh you don't own that item"

        if amount <= 0:
            return "Amount on steroids! You need a doc's consultation."

        if amount > guild_data["users"][user_id]["inv"][item]:
            return "bruh you're tryin to sell more than what you own"

        item_price=int(self.mainshop[item]['price'])
        cost=int((60/100)*(amount * item_price))

        if item in guild_data['users'][user_id]['inv']:
            guild_data['users'][user_id]['inv'][item] -= amount
        else:
            guild_data['users'][user_id]['inv'][item]=amount

        Economy_MongoDB.update_one(
            {"guild_id": guild_id}, {"$set": guild_data})

        self.update_bank(user, int(cost), "wallet")

        return f"You just Sold **{amount} {self.mainshop[item]['display']}** for **⏣ {cost:,}**"

    @ commands.command(aliases=["rich"])
    async def wealthy(self, ctx):
        self.open_account(ctx.author)
        user_id=str(ctx.author.id)
        guild_id=ctx.guild.id
        guild_data=self.get_bank_data(guild_id)
        users_data=guild_data["users"]

        user_ids_sorted=sorted(
            users_data, key=lambda _user_id: users_data[_user_id]["wallet"] + users_data[_user_id]["bank"], reverse=True)
        lb=[]
        sep="\n"

        rank=1


        award={1: ':first_place:', 2: ':second_place:', 3: ':third_place:'}
        for uid in user_ids_sorted:
            try:
                temp_user=ctx.guild.get_member(int(uid))
                lb.append(
                    f"{award[rank] if rank in award else ':small_blue_diamond:'} **{guild_data['users'][uid]['wallet'] + guild_data['users'][uid]['bank']:,}** - {temp_user.mention}")

                rank += 1
            except:
                rank -= 1

            if rank >= 10:
                break
        em=discord.Embed(title=f"Richest users in {ctx.guild.name}", description=f'{sep.join(lb)}',
                           color=discord.Color(0xfa43ee))
        em.set_thumbnail(url=str(ctx.guild.icon_url)
                         )

        em.set_footer(text="This is the net-worth")

        await ctx.message.reply(embed=em)


def setup(client):
    client.add_cog(Economy(client))
