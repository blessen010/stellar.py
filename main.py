import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

import random

load_dotenv()

token = os.environ.get("TOKEN")

client = commands.Bot(command_prefix = "s!", intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    print("bot is ready")

@client.tree.command(name = "test", description = "test est test")
async def test(interaction):
    await interaction.response.send_message("test successfull ✅")

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)

    await ctx.reply(f"the bots latency is **{latency}**ms")

@client.command(aliases = ["8ball", "8b"])
async def eightball(ctx, *, question):
    responses = ["As I see it, yes.", "Ask again later", "Better not tell you now", 
                 "Cannot predict now", "Concentrate and ask again.", "Don't count on it", 
                 "It is certain", "It is decidedly so.", "Most likely.", "My reply is no.",
                 "My sources say no.", "Outlook not so good", "Reply hazy, try again.", 
                 "Signs point to yes.", "Very doubtful", "Without a doubt.", "Yes.", "N0.o",
                 "Yes definitely.", "You may rely on it.", "Never.", "50/50", "In your dreams."]
    
    final_response = random.choice(responses)

    await ctx.reply(f"**Question**: {question}\n**Answer:** {final_response}")

@client.command()
async def math(ctx, num1, operator, num2):
    if operator == "+":
        sum = int(num1) + int(num2)

        await ctx.reply(f"**{num1}** + **{num2}** = **{sum}**")

    if operator == "-":
        sum = int(num1) - int(num2)

        await ctx.reply(f"**{num1}** - **{num2}** = **{sum}**")

    if operator == "x":
        sum = int(num1) * int(num2)

        await ctx.reply(f"**{num1}** x **{num2}** = **{sum}**")

    if operator == "/":
        sum = int(num1) + int(num2)

        await ctx.reply(f"**{num1}** ÷ **{num2}** = **{sum}**")

    if operator not in ["+", "-", "*", "/"]:
        await ctx.send(""":x: You have used the command in wrong syntax, here are the operations :x:
                       \n**Additon**: **+**
                       \n**Subtraction**: **-**
                       \n**Multiplication**: **x**
                       \n**Divison**: **/**""")


client.run(token)


# @client.event
# async def on_message(message):
#     if message.content == "hello".lower():
#         await message.channel.send("as salam walikum")