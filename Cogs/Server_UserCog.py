import os
import random
import discord
from discord.ext import commands
from typing import Optional
from discord import Member
from datetime import datetime


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


class Server_User(commands.Cog):
    def __init__(self,  client):
        self.client = client
    # server stats

    @commands.command()
    async def server(self, ctx):
        name = str(ctx.guild.name)
        description = str(" ")

        owner = f"{ctx.guild.owner.mention}```"
        id = f"```{ctx.guild.id}```"
        region = f'```{ctx.guild.region}```'
        memberCount = f"```{ctx.guild.member_count}```"

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name,
            description=description,
            color=discord.Color.purple()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner:", value=owner, inline=True)
        embed.add_field(name="Server ID:", value=id, inline=False)
        embed.add_field(name="Region:", value=region, inline=True)
        embed.add_field(name="Member Count:", value=memberCount, inline=False)

        await ctx.message.reply(embed=embed)

    # user info

    @commands.command(aliases=["user", "about"])
    async def userinfo(self, ctx, target: Optional[Member]):
        target = target or ctx.author
        embed = discord.Embed(
            title="About User",
            colour=target.colour,
            timestamp=datetime.utcnow())
        embed.set_thumbnail(url=target.avatar_url)
        fields = [("Name:", target.mention, False),
                  ("ID:", target.id, False),
                  ("Bot:", target.bot, False),
                  ("Top Role:", target.top_role.mention, False),
                  ("Status:", str(target.status).title(), False),
                  ("Created at:", target.created_at.strftime(
                      "%d/%m/%Y, Time: %H:%M:%S"), False)
                  ]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.message.reply(embed=embed)


def setup(client):
    client.add_cog(Server_User(client))
