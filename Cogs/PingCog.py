import os
import random
import discord
from discord.ext import commands


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

class pingpong(commands.Cog):
    def __init__(self,  client):
           self.client = client
            
    @commands.command()
    async def ping(self,ctx):    
    
      await ctx.send(f"Pong! {int(self.client.latency*1000)}ms")

def setup(client):
    client.add_cog(pingpong(client))
    
