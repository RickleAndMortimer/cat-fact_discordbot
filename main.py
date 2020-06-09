import discord
from discord.ext import commands
import importlib
cat_facts = importlib.import_module('cat_facts')
database = importlib.import_module('database')

bot = commands.Bot(command_prefix='!')
token = 'NzE5NzYzODAwNzM1MDg4NzY4.Xt8KoA.ufoKFOV8XNhYfbsxXAzDx78RuKE'

##events
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

##functions
#sends fact to user
async def sendfact(ctx):
    await ctx.send(cat_facts.reqFact())
#makes sure the command is from a user
def validateCommand(ctx):
    if (ctx.author.bot is discord.User.bot):
        return -1
    else:
        return 1
##commands
@bot.command()
#registers user to PostgreSQL database
async def subscribe(ctx):
    if (validateCommand(ctx) == 1): 
        userID = ctx.author.id
        if (database.addUser(userID) == 1):
            await ctx.send("Subscription successful! Enjoy your daily feed of cat facts at 12:00 PM!")
        else:
            await ctx.send("ERROR: You're already subscribed to Crazy Cat Facts!")
@bot.command()
#unsubscribes user in PostgreSQL database
async def unsubscribe(ctx):
    if (validateCommand(ctx) == 1):
        if (database.removeUser(userID) == 1):
            await ctx.send("You have unsubscribed from Crazy Cat Facts :(.")
        else:
            await ctx.send("ERROR: You are not subscribed to Crazy Cat Facts.")        
##runs the bot
bot.run(token)
