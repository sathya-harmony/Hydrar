import os
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandError, CommandInvokeError
from requests.models import HTTPError
from wikipedia.exceptions import PageError
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
        await ctx.message.reply('Please give proper input.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.message.reply(
            "You don't have the permissions to execute this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.reply('Please give proper input.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.reply("Invalid command.")


class Math(commands.Cog):
    def __init__(self,  client):
        self.client = client

    @commands.command(aliases=['fractionize', 'fraction'])
    async def convert(self, ctx, *, amount: float):
        await ctx.message.reply(Fraction(amount))

    '''@commands.command(aliases=['ask'])
    async def solve(self, ctx, *, thing):
        async with ctx.channel.typing():

            app_id = 'KPH8T8-L58AQ4EQT8'
            try:
                client = wolframalpha.Client(app_id)
                res = client.query(thing)
                answer = next(res.results).text

                await ctx.message.reply('**This is what I got:** {}'.format(answer))
            except StopIteration or RuntimeError:
                await ctx.message.reply("Sorry, I don't know the answer to that. :frowning:")'''

    @commands.command(aliases=["search", "query", "doubt"])
    async def ask(self, ctx, *, question):

        async with ctx.channel.typing():
            await asyncio.sleep(0.001)
            app_id = 'KPH8T8-L58AQ4EQT8'
            client = wolframalpha.Client(app_id)

            try:
                res = client.query(question)
            except HTTPError:
                await ctx.send("Sorry, **unable to send answer** due to it exceeding **2000 characters**.")
                return

            answer = ""
            i = 0
            try:
                for result in res.results:
                    try:
                        answer = str(
                            result.text) if i == 0 else f"{answer}\n• {result.text}"
                        i += 1
                    except StopIteration:
                        pass
            except AttributeError:
                try:
                    for pod in res.pods:
                        try:
                            answer = str(
                                pod) if i == 0 else f"{answer}\n• {pod}"
                            i += 1
                        except StopIteration:
                            pass
                except AttributeError:
                    pass

            if i > 1:
                answer = f"\n• {answer}"
            elif "\n" in answer:
                answer = f"\n{answer}"
            elif answer == "" or answer.isspace():
                answer = "I don't know the answers to that yet. :("

            try:
                if answer == "I don't know the answers to that yet. :(":
                    if len(question) <= 300:
                        page = wikipedia.page(question)
                        title = page.title
                        result = wikipedia.summary(
                            question, sentences=6).replace("\n", "\n\n")
                        url = page.url
                        answer = f"\n\n**Title: ** {title}\n\n**According to wikipedia**, {result}\n\n**For more information, refer {url}**"
                    else:
                        answer = f"Please limit your input to not more than 300 characters.\n(Your current input is of {len(question)} characters)"
            except wikipedia.exceptions.DisambiguationError as e:
                answer = f"\n**Next time, choose one of these (if any one of these are your search target):** \n{e}"
            except wikipedia.exceptions.PageError:
                pass

            if len(answer) > 2000-30:
                await ctx.message.reply("Sorry, **unable to send answer** due to it exceeding **2000 characters**.")
                print(answer, len(answer))
                return

            if answer == "My name is Wolfram|Alpha.":
                await ctx.message.reply("**This is what I got:** I am <@!844813316505075712>.")
                return

            if "Stephen Wolfram" in answer:
                await ctx.message.reply("**This is what I got:** **Sathya#6960** made me.")
                return

            await ctx.message.reply(f"**This is what I got:** {answer}")

    '''@commands.command()
    async def search(self, ctx, *, query):
        async with ctx.channel.typing():
            try:
                page = wikipedia.page(''.join(query))
                summary = wikipedia.summary(''.join(query), sentences=10)
                title = page.title
                url = page.url
                await ctx.message.reply(f"**Title:**{title}\n\n**Summary:**{summary}\n\nRead More Here: {url}")
            except Exception or PageError or CommandInvokeError or IndexError or CommandError:
                await ctx.message.reply("Sorry, I couldn't find any matching data regarding that :frowning:")'''

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
