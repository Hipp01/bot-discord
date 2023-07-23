from discord.ext import commands
import random

class DevineLeNombre(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def devine_le_nombre(self, ctx):
		self.nombre_bot = random.randint(0, 1000)
		await ctx.send("Début de la partie !")
		await ctx.send("J'ai choisis un nombre entre 1 et 1000 !")
		await ctx.send("Pour jouer tu peux utiliser la commande `!devine <nombre>`.")

	@commands.command()
	async def devine(self, ctx, nombre):
		try:
			nombre = int(nombre)
			if nombre == self.nombre_bot:
				await ctx.send("Bravo, tu as gagné !")
				await ctx.send("Le nombre était : " + str(self.nombre_bot))
			elif nombre > 1000 or nombre <= 0:
				await ctx.send("Oups ! Mon nombre n'est compris qu'entre 1 et 1000 !")
			elif nombre > self.nombre_bot:
				await ctx.send("Mon nombre est plus petit !")
			elif nombre < self.nombre_bot:
				await ctx.send("Mon nombre est plus grand !")
		except:
			await ctx.send("Oups ! Ceci n'est pas un nombre !")