import asyncio
import os
import random
from typing import Optional
import discord
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import command
from discord.ext.commands.errors import CommandInvokeError
from discord_components.dpy_overrides import send_message
import time

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
    '''@commands.command()
    @owner_or_perm(manage_roles=True, manage_messages=True)
    async def on_guild_join(self, ctx):
        perms_dict = {"read_messages": True, "send_messages": False,
                      "connect": False, "send_tts_messages": False}
        perms = discord.Permissions(**perms_dict)

        mute_role = await ctx.guild.create_role(name="Muted", permissions=perms)
        roles_list = []

        #count = 0
        for channels in ctx.guild.text_channels:

            await channels.set_permissions(target=mute_role, permissions=perms_dict)'''
    '''@commands.command()
    @owner_or_perm(manage_roles = True, manage_messages = True)
    async def mute(self, ctx, member: discord.Member, time: Optional[int], *, reason: Optional[str] = "No reason provided"):
        pass'''

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        try:
            if (not ctx.author.guild_permissions.manage_messages):
                await ctx.message.reply("You don't have the permissions to execute this command")
                return

            guild = ctx.guild
            muteRole = discord.utils.get(guild.roles, name="Muted")
            guild_roles = list(ctx.guild.roles)

            if not muteRole:
                muteRole = await guild.create_role(name="Muted")
                message = await ctx.message.reply("Muted role not Found. Creating one")
                await asyncio.sleep(2)
                await message.edit('Muted role not Found. Creating one.')
                await asyncio.sleep(2)
                await message.edit('Muted role not Found. Creating one..')
                await asyncio.sleep(2)
                await message.edit('Muted role not Found. Creating one...')
                for channels in ctx.guild.text_channels:
                    await channels.set_permissions(muteRole, speak=False, send_messages=False, read_messages=True)
                for voice_channels in ctx.guild.voice_channels:
                    await voice_channels.set_permissions(muteRole, connect=False)
                await member.add_roles(muteRole, reason=reason)
                embed = discord.Embed(
                    title=f"🔇Muted {member.display_name} | Reason: {reason}")
                await ctx.message.reply(embed=embed)
                await member.send(f"You have been muted from **{guild.name}** | Reason: **{reason}**")
            else:
                embed = discord.Embed(
                    title=f"🔇Muted {member.display_name} | Reason: {reason}")
                await ctx.message.reply(embed=embed)
                await member.send(f"You have been muted from **{guild.name}** | Reason: **{reason}**")

                await member.add_roles(muteRole, reason=reason)
        except CommandInvokeError:
            await ctx.send("Cannot DM this user.")

    @commands.command()
    async def unmute(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        try:
            if (not ctx.author.guild_permissions.manage_messages):
                await ctx.message.reply("You don't have the permissions to execute this command")
                return

            guild = ctx.guild
            muteRole = discord.utils.get(guild.roles, name="Muted")
            guild_roles = list(ctx.guild.roles)

            if not muteRole:
                pass

            await member.remove_roles(muteRole, reason=reason)
            embed = discord.Embed(
                title=f"🔊Unmuted {member.display_name} | Reason: {reason}")
            await ctx.message.reply(embed=embed)
            await member.send(f"You have been unmuted from **{guild.name}** | Reason: **{reason}**")
        except CommandInvokeError:
            await ctx.author.send("Cannot DM this user.")


def setup(client):
    client.add_cog(kick_ban(client))
