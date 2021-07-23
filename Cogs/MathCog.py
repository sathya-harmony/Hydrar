import os
import discord
from discord.ext import commands
import wolframalpha
from fractions import*
import asyncio
import wikipedia
from random import randint
import json
import requests
import ast
#import google_currency


@commands.Cog.listener()
async def on_command_error(ctx, error):
    if isinstance(error, commands.UserInputError):
        await ctx.send('Please give proper input.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "You don't have the permissions to execute this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please give proper input.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command.")


class Math(commands.Cog):
    def __init__(self,  client):
        self.client = client

    @commands.command(aliases=['fractionize', 'fraction'])
    async def convert(self, ctx, *, amount: float):
        await ctx.send(Fraction(amount))

    @commands.command(aliases=['ask'])
    async def solve(self, ctx, *, thing):
        async with ctx.channel.typing():
            await asyncio.sleep(0.5)
            app_id = 'KPH8T8-L58AQ4EQT8'
            client = wolframalpha.Client(app_id)
            res = client.query(thing)
            for result in res.result:
                answer = next(result)
                answer2 = next(result)
            try:
                await ctx.send('**Question:** {}\n**Answer:** {}\n**.**{}'.format(thing, answer, answer2))
            except Exception:
                await ctx.send("Sorry, I don't know the answer to that.:frown:")

    @commands.command()
    async def search(self, ctx, *, query):
        async with ctx.channel.typing():
            await asyncio.sleep(0.3)
            page = wikipedia.page(''.join(query))
            summary = wikipedia.summary(''.join(query), sentences=10)
            title = page.title
            url = page.url
            await ctx.send(f"**Title:**{title}\n\n**Summary:**{summary}\n\nRead More Here: {url}")

    '''@commands.command()
    async def currencyConvert(self, ctx, ffrom: str, to: str, amount: float):
        currency = google_currency.convert(ffrom, to, amount)
        # await ctx.send(currency)
        response = requests.get(currency)
        wl = response.text
        quod = ast.literal_eval(wl)
        curren = quod["curren"]
        await ctx.send(curren)'''

    '''async with ctx.channel.typing():
            await asyncio.sleep(0.5)
            def viki_sum(arg):
                definition = wikipedia.summary(arg,sentences=3,chars=1000)
                return definition
            #embed = discord.Embed(title="***Wikipedia***",description=viki_sum(word))
            await ctx.send(viki_sum(word))'''


def setup(client):
    client.add_cog(Math(client))
