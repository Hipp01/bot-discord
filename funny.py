from discord.ext import commands
import discord
import random

class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def funny(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Commande invalide. Essayez `!funny slap`, `!funny roll_dice`, `!funny joke` ou `!funny commands`.')

    @funny.command()
    async def slap(self, ctx, member: discord.Member):
        await ctx.send(f'{ctx.author.mention} donne une gifle à {member.mention} ! Ouch !')

    @funny.command()
    async def roll_dice(self, ctx):
        dice_result = random.randint(1, 6)
        await ctx.send(f'{ctx.author.mention} lance un dé et obtient : {dice_result} !')

    @funny.command()
    async def joke(self, ctx):
        jokes = [
            "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
            "Quel est le comble pour un électricien ? De ne pas être au courant.",
            "Pourquoi les poissons n'aiment pas jouer au tennis ? Parce qu'ils ont peur des filets.",
            "Qu'est-ce qui est jaune et qui attend ? Jonathan."
        ]
        joke = random.choice(jokes)
        await ctx.send(joke)

    @funny.command()
    async def commands(self, ctx):
        command_list = '\n'.join([f"`{command.name}`" for command in self.bot.commands if command.parent == self.funny])
        await ctx.send(f"Les commandes disponibles sont :\n{command_list}")
