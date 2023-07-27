from discord.ext import commands

class Score(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def score(self, ctx):
		name = ctx.author.name
		try:
			fichier = open(name, 'r')
			scores = fichier.read()
			await ctx.send(f"Le score de {ctx.author.mention} est de {scores} !")
			fichier.close()
		except FileNotFoundError:
			fichier = open(name, 'w')
			fichier.write("0")
			fichier.close()
			await ctx.send(f"Le score de {ctx.author.mention} est de 0 !")