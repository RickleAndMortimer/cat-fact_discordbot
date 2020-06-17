import discord
import asyncio
import logging
import importlib
import os
from discord.ext import commands
cat_facts = importlib.import_module('cat_facts')
database = importlib.import_module('database')
##constant stuff
token = os.environ['BOT_TOKEN']
delivery_interval = 60
##bot setup
bot = commands.Bot(command_prefix='!')
##logger setup
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
##events/background tasks
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
#bot sends message to every subscribed users
async def deliverFacts():
    await bot.wait_until_ready()
    print("Message Delivery Activated")
    while (not bot.is_closed()):     
        await asyncio.sleep(delivery_interval)
        facts = cat_facts.requestFacts()
        users = database.listUsers()
        for userID in users:
            user = bot.get_user(userID[0])
            await user.send("**<TODAYS CAT FACT>**" + cat_facts.pickFact(facts))
##functions
#makes sure the command is from a user
def validateCommand(ctx):
    if (ctx.author.bot is discord.User.bot):
        return -1
    else:
        return 1

##commands
@bot.command()
async def list(ctx):
    await ctx.send(database.listUsers())
@bot.command()
#registers user to PostgreSQL database
async def subscribe(ctx):
    if (validateCommand(ctx) == 1):
        user = ctx.author
        if (database.addUser(user.id) == 1):
            await user.send("Subscription successful! Enjoy your daily feed of cat facts at 4:00 PM!")
        else:
            await ctx.send("ERROR: You're already subscribed to Crazy Cat Facts!")
@bot.command()
#unsubscribes user in PostgreSQL database
async def unsubscribe(ctx):
    if (validateCommand(ctx) == 1):
        user = ctx.author
        if (ctx.guild is None):
            if (database.deleteUser(user.id) == 1):
                await user.send("You have unsubscribed from Crazy Cat Facts :(.")
            else:
                await user.send("ERROR: You are not subscribed to Crazy Cat Facts.")
        else:
            await ctx.send("Please unsubscribe through DM'ing the bot.")
##runs the bot
bot.loop.create_task(deliverFacts())
bot.run(token)


