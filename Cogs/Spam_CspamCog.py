import os
import random
import discord
from discord.ext import commands

owner_perms = {611210739830620165}  # Sathya

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

class Spam_Cspam(commands.Cog):
    def __init__(self,  client):
           self.client = client


    #Spam
    @commands.command()
    async def spam(self, ctx, amount: int, *, text):
    
        if await op(ctx):
            for _ in range(amount):
                await ctx.send(text)    

    @commands.command(aliases=['clear_spam', 'clearspam'])
    async def cspam(self, ctx, amount: int, *, text):
    
        if await op(ctx):            
            await ctx.message.delete()
            spammed_msgs = []

            for _ in range(amount):               
                spammed_msgs.append(await ctx.send(text))

            for msg in spammed_msgs:
                
                try:
                    await msg.delete()
                except Exception:                   
                    pass        


def setup(client):
    client.add_cog(Spam_Cspam(client))



                    
                           