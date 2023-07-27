from discord.ext import commands

def ajout_points(name, points):
	try:
		fichier = open("score/" + name, 'r')
		scores = fichier.read()
		scores += points
		fichier.close()
		fichier = open("score/" + name, 'w')
		fichier.write(scores)
		fichier.close()
	except FileNotFoundError:
		fichier = open("score/" + name, 'w')
		fichier.write(points)
		fichier.close()

class Score(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def score(self, ctx):
		name = ctx.author.name
		try:
			fichier = open("score/" + name, 'r')
			scores = fichier.read()
			await ctx.send(f"Le score de {ctx.author.mention} est de {scores} !")
			fichier.close()
		except FileNotFoundError:
			fichier = open("score/" + name, 'w')
			fichier.write("0")
			fichier.close()
			await ctx.send(f"Le score de {ctx.author.mention} est de 0 !")