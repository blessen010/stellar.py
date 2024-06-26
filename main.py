import discord
from discord.ext import commands

from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    print(f"ID: {client.user.id}")
    print(f"Guilds: {len(client.guilds)}")

client.run(TOKEN)