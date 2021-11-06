from logging import exception
import os
import random
import discord
from discord.ext import commands
import asyncio

from discord.ext.commands.errors import CommandInvokeError
#from discord_slash import cog_ext


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


class pingpong(commands.Cog):
    def __init__(self,  client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):

        await ctx.message.reply(f"Pong! {int(self.client.latency*1000)}ms")

    '''@cog_ext.cog_slash(name='Ping', description="Shows how fast the connection is between the bot and Discord!")
    async def ping(self, ctx):

        await ctx.send(f"Pong! {int(self.client.latency*1000)}ms")'''

    def convert(self, time):
        pos = ["s", "m", "h", "d"]
        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

        unit = time[-1]
        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    async def giveaway(self, ctx):
        await ctx.message.reply("Let's get you set-up with your giveaway! Answer these questions **Carefully**(Times out in 20 seconds!)")

        questions = ["Which channel should your giveaway be hosted in?",
                     "What should be the duration of the giveaway? (accepted format: `s|m|h|d`)",
                     "What is the prize of the giveaway?"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(i)
            try:
                msg = await self.client.wait_for('message', timeout=20.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("You didn\'t answer in time, so I have stopped this giveaway request! `P.S be quicker next time if you were trying to host the giveaway`")
                return
            else:
                answers.append(msg.content)

        try:

            c_id = int(answers[0][2:-1])

        except:
            await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time!")
            return

        channel = self.client.get_channel(c_id)

        time = self.convert(answers[1])
        if time == -1:
            await ctx.send(f"You didn't answer the time with a proper unit. Use `s|m|h|d` next time!")
            return
        elif time == -2:
            await ctx.send(f"The time must be an integer.")
            return
        prize = answers[2].capitalize()
        days = int(time//86400)
        hours = int((time - days*86400)//3600)
        mins = int((time - days*86400 - hours*3600)//60)
        seconds = int(time - days*86400 - hours*3600 - mins*60)

        if days > 7:
            await ctx.send(f"The Giveaway can't last more than a week. Please mention a time that is less than 7 days.")
            return

        await ctx.send(f"Success! The Giveaway will be in {channel.mention} and will last **{days} : {hours} : {mins} : {seconds}** seconds. The prize is **{prize}**")
        embed = discord.Embed(
            title="🎉Giveaway", description=f"Prize:\n{prize}", color=ctx.author.color)
        embed.add_field(name="Hosted by:", value=ctx.author.mention)
        embed.set_footer(text=f"Ends in {days} : {hours} : {mins} : {seconds}")
        my_msg = await channel.send(embed=embed)

        await my_msg.add_reaction("🎉")

        await asyncio.sleep(time)
        try:
            new_msg = await channel.fetch_message(my_msg.id)

            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(self.client.user))

            winner = random.choice(users)

            await channel.send(f"Congratulations! {winner.mention} won **{prize}**")
        except CommandInvokeError or IndexError:
            await channel.send("Unfortunately no-one reacted to the giveaway. So no one wins!")
            return


def setup(client):
    client.add_cog(pingpong(client))
