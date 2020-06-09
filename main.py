import discord
from discord.ext import commands
import importlib

bot = commands.Bot(command_prefix='!')
token = 'NzE5NzYzODAwNzM1MDg4NzY4.Xt8KoA.ufoKFOV8XNhYfbsxXAzDx78RuKE'

@bot.event
async def on_ready():
    print("Logged in as {0.user}")

@bot.command()
#gets info from cat-facts api and sends it to user
async def sendFact(ctx):
    await ctx.send("Fact sent!")

@bot.command()
#registers user to PostgreSQL database
async def subscribe(ctx):
    await ctx.send("Subscription successful! Enjoy your daily feed of cat facts!")
#runs the bot
bot.run(token)
