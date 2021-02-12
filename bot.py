import discord
from discord.ext import commands

import json



with open("./configs/discord_conf.json") as discord_conf:
    token = json.load(discord_conf)["token"]