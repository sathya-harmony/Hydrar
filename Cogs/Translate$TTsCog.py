import os
import random
import discord
from discord.ext import commands
import math


class TTs(commands.Cog):
    def __init__(self,  client):
           self.client = client
