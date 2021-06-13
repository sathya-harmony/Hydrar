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


class Music(commands.Cog):
    def __init__(self,  client):
        self.client = client

    @commands.command()
    async def play(self, ctx, url: str, channel: str):
        voiceChannel = discord.utils.get(
            ctx.guild.voice_channels, name=channel)
        voice = discord.utils.get(commands.voice_client, guild=ctx.guild)
        await voiceChannel.connect()


def setup(client):
    client.add_cog(Music(client))
