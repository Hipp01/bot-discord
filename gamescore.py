from discord.ext import commands

def ajout_points(name, points):
	try:
		fichier = open("score/" + name, 'r')
		scores = fichier.read()
		scores = str(int(scores)+int(points))
		fichier.close()
		fichier = open("score/" + name, 'w')
		fichier.write(scores)
		fichier.close()
		return scores
	except FileNotFoundError:
		fichier = open("score/" + name, 'w')
		fichier.write(points)
		fichier.close()
		return points

class Score(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def score(self, ctx):
		name = ctx.author.name
		score = ajout_points(name, "0")
		await ctx.send(f"{ctx.author.mention} à {score} points !")