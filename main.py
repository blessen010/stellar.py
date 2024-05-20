import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get("TOKEN")

client = commands.Bot(command_prefix = "s!", intents = discord.Intents.all())

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

client.run(token)