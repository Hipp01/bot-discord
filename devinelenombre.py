from discord.ext import commands
import random
from gamescore import ajout_points


class DevineLeNombre(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.niveaux = None

	@commands.command()
	async def test(self, ctx, points):
		auteur = ctx.author.mention
		ajout_points(auteur, points)

	@commands.command()
	async def dln(self, ctx):
		await ctx.send("Début de la partie !")
		await ctx.send("Pour choisir le niveau tu peux utiliser les commandes:")
		await ctx.send("`!niveau facile` pour chercher un nombre entre 1 et 500 (+1 point)")
		await ctx.send("`!niveau normal` pour chercher un nombre entre 1 et 1000 (+2 points)")
		await ctx.send("`!niveau difficile` pour chercher un nombre entre 1 et 5000 (+4 points)")

	@commands.command()
	async def niveau(self, ctx, niveaux):
		self.niveaux = niveaux
		if niveaux == "facile":
			self.nombre_bot = random.randint(1, 500)
			await ctx.send("C'est bon ! J'ai choisis un nombre entre 1 et 500 !")
			await ctx.send("Pour jouer tu peux utiliser la commande `!devine <nombre>`.")
		elif niveaux == "normal":
			self.nombre_bot = random.randint(1, 1000)
			await ctx.send("C'est bon ! J'ai choisis un nombre entre 1 et 1000 !")
			await ctx.send("Pour jouer tu peux utiliser la commande `!devine <nombre>`.")
		elif niveaux == "difficile":
			self.nombre_bot = random.randint(1, 5000)
			await ctx.send("C'est bon ! J'ai choisis un nombre entre 1 et 5000 !")
			await ctx.send("Pour jouer tu peux utiliser la commande `!devine <nombre>`.")
		else:
			await ctx.send("Oups! Cette commande est incorrecte :/")

	@commands.command()
	async def devine(self, ctx, nombre):
		name = ctx.author.name
		try:
			nombre = int(nombre)
			if nombre == self.nombre_bot:
				await ctx.send("Bravo, tu as gagné !")
				await ctx.send("Le nombre était : " + str(self.nombre_bot))
				if self.niveaux == "facile":
					try:
						fichier = open("score/" + name, 'r')
						scores = fichier.read()
						fichier.close()
						scores = str(int(scores) + 1)
						fichier = open("score/" + name, 'w')
						fichier.write(scores)
						fichier.close()
					except FileNotFoundError:
						fichier = open("score/" + name, 'w')
						fichier.write("1")
						fichier.close()
				if self.niveaux == "normal":
					try:
						fichier = open("score/" + name, 'r')
						scores = fichier.read()
						fichier.close()
						scores = str(int(scores) + 2)
						fichier = open("score/" + name, 'w')
						fichier.write(scores)
						fichier.close()
					except FileNotFoundError:
						fichier = open("score/" + name, 'w')
						fichier.write("2")
						fichier.close()
				if self.niveaux == "difficile":
					try:
						fichier = open("score/" + name, 'r')
						scores = fichier.read()
						fichier.close()
						scores = str(int(scores) + 4)
						fichier = open("score/" + name, 'w')
						fichier.write(scores)
						fichier.close()
					except FileNotFoundError:
						fichier = open("score/" + name, 'w')
						fichier.write("4")
						fichier.close()
				return
			elif self.niveaux == "facile":
				if nombre > 500 or nombre <= 0:
					await ctx.send("Oups ! Mon nombre n'est compris qu'entre 1 et 500 !")
				elif nombre > self.nombre_bot:
					await ctx.send("Mon nombre est plus petit !")
				elif nombre < self.nombre_bot:
					await ctx.send("Mon nombre est plus grand !")
			elif self.niveaux == "normal":
				if nombre > 1000 or nombre <= 0:
					await ctx.send("Oups ! Mon nombre n'est compris qu'entre 1 et 1000 !")
				elif nombre > self.nombre_bot:
					await ctx.send("Mon nombre est plus petit !")
				elif nombre < self.nombre_bot:
					await ctx.send("Mon nombre est plus grand !")
			elif self.niveaux == "difficile":
				if nombre > 5000 or nombre <= 0:
					await ctx.send("Oups ! Mon nombre n'est compris qu'entre 1 et 5000 !")
				elif nombre > self.nombre_bot:
					await ctx.send("Mon nombre est plus petit !")
				elif nombre < self.nombre_bot:
					await ctx.send("Mon nombre est plus grand !")
		except ValueError:
			await ctx.send("Oups ! Ceci n'est pas un nombre !")
