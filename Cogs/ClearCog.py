import os
import random
import discord
from discord.ext import commands
import math

owner_perms = {611210739830620165}  # Sathya
               


def cop(ctx):
    if ctx.author.id in owner_perms:
        return True

    return False

# Owner Permissions.
async def op(ctx, msg=None):
    if ctx.author.id in owner_perms:
        # If any msg was given, send it.
        if msg is not None:
            await ctx.send(msg)
        return True

    # If the user is not a bot owner.
    await ctx.send("Only bot owner(s) can use this command.")
    return False


# Check if the command's author is guild owner, bot owner, or has the specified guild_permissions.
def owner_or_perm(**perms):
    original = commands.has_guild_permissions(**perms).predicate

    async def extended_check(ctx):
        if ctx.guild is None:
            return False

        is_bot_owner = cop(ctx)

        return (ctx.guild.owner_id == ctx.author.id or is_bot_owner) or await original(ctx)

    return commands.check(extended_check)




class clear(commands.Cog):
    def __init__(self,  client):
           self.client = client

    # Clear 
    @commands.command(aliases=["delete", "purge"])
    @owner_or_perm(manage_messages=True)
    async def clear(self, ctx, amount):    
        if amount.lower() == "all":       
            await ctx.send(f"{len(await ctx.channel.purge(limit=math.inf))-1} message(s) was/were cleared.", delete_after=3)
        else:       
            try:           
                await ctx.send(f"{len(await ctx.channel.purge(limit=int(amount)+1))-1} message(s) was/were  cleared.", delete_after=3)
            except ValueError:           
                raise commands.UserInputError


def setup(client):
    client.add_cog(clear(client))                        