import discord, random, json
from discord.ext import commands
from morpion import Morpion
from pendu import Pendu

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready !")
    await bot.add_cog(Morpion(bot))
    await bot.add_cog(Pendu(bot))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong !")

with open('config.json', 'r') as f:
    config = json.load(f)

token = config['TOKEN_BOT']

bot.run(token)
