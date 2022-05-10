import random
import discord
intents = discord.Intents.default()
intents.members = True

from discord.ext import commands
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("The bot is ready")

@bot.command(pass_context = True)
async def newcode(ctx):
    global x 
    x = random.randint(1000,9999)
    await ctx.send('New Code generated!')
    await ctx.message.author.send("New Code: " + str(x))

@bot.command(pass_context = True)
async def lastcode(ctx):
    await ctx.message.author.send("Last Code: " + str(x))

@bot.command(pass_context = True)
async def newlocker(ctx):
    if ctx.guild.owner == ctx.message.author:
      global y 
      y = random.randint(1000,9999)
      await ctx.guild.owner.send(y)

@bot.command(pass_context=True)
async def lastlocker(ctx):
  await ctx.guild.owner.send(ctx.message.author.name + " has asked for the locker's code")
  await ctx.message.author.send("Locker Code: " + str(y))

bot.run('OTczNjEwOTYxNzYyMTI3ODky.GHJvwr.-GsVGHkpWLB52dF9L7AD79M3mr3vHJE9fq558A')

