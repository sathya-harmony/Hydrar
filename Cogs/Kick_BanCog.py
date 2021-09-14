import os
import random
from typing import Optional
import discord
from discord.colour import Color
from discord.ext import commands

owner_perms = {611210739830620165}  # Sathya


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


def cop(ctx):
    if ctx.author.id in owner_perms:
        return True

    return False

# Owner Permissions.


async def op(ctx, msg=None):
    if ctx.author.id in owner_perms:
        # If any msg was given, send it.
        if msg is not None:
            await ctx.message.reply(msg)
        return True

    # If the user is not a bot owner.
    await ctx.message.reply("Only bot owner(s) can use this command.")
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


class kick_ban(commands.Cog):
    def __init__(self,  client):
        self.client = client

    # kick
    @commands.command()
    @owner_or_perm(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await user.kick(reason=reason)
        embed = discord.Embed(
            title=f"***🦶{user.name}#{user.discriminator} was kicked***")
        await ctx.message.reply(embed=embed)
    # ban

    @commands.command()
    @owner_or_perm(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        await user.ban(reason=reason)
        embed = discord.Embed(
            title=f"***💥{user.name}#{user.discriminator} was banned***")
        await ctx.message.reply(embed=embed)

    # unban
    @commands.command()
    @owner_or_perm(ban_members=True)
    async def unban(self, ctx, *, user: discord.User):

        for ban_entry in await ctx.guild.bans():
            if ban_entry.user.id == user.id:
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title=f"***😳{user.name}#{user.discriminator} was unbanned***")
                await ctx.message.reply(embed=embed)
                break
        else:
            await ctx.message.reply(f"The user {user.mention} is not already banned. Please ban them to unban them.")

    # @commands.Cog.listener()
    @commands.command()
    @owner_or_perm(manage_roles=True, manage_messages=True)
    async def on_guild_join(self, ctx):
        permissions = discord.Permissions(
            read_messages=True, send_messages=False, connect=False, send_tts_messages=False)

        mute_role = await ctx.guild.create_role(name="Muted", permissions=permissions)
        roles_list = []

        #count = 0
        for channels in ctx.guild.channels:

            await channels.set_permissions(target=mute_role, permissions=permissions)
            #count += 1
    '''@commands.command()
    @owner_or_perm(manage_roles = True, manage_messages = True)
    async def mute(self, ctx, member: discord.Member, time: Optional[int], *, reason: Optional[str] = "No reason provided"):
        pass'''


def setup(client):
    client.add_cog(kick_ban(client))
