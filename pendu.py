from discord.ext import commands
import random


def get_words_with_special_characters():
    with open("liste_francais.txt", 'r') as file:
        lines = file.readlines()
    return lines


mots = get_words_with_special_characters()


class Pendu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mot = ""
        self.lettres = []
        self.deja_proposees = []

    @commands.command()
    async def pendu(self, ctx):
        self.mot = random.choice(mots)[:-1]
        self.deja_proposees = []
        await ctx.send("Le mot à trouver contient " + str(len(self.mot)) + " lettres.")
        self.lettres = ['_'] * len(self.mot)
        await ctx.send(' '.join(self.lettres))

    @commands.command()
    async def pendu_play(self, ctx, lettre):
        lettre = lettre.lower()
        if lettre in self.deja_proposees:
            await ctx.send("Vous avez déjà proposé cette lettre.")
        elif len(lettre) != 1 or not lettre.isalpha():
            await ctx.send("Le caractère fourni n'est pas une lettre valide.")
        elif lettre in self.mot:
            self.deja_proposees.append(lettre)
            await ctx.send("Lettre trouvée")
            for i in range(len(self.mot)):
                if self.mot[i] == lettre:
                    self.lettres[i] = lettre
            if "_" not in self.lettres:
                await ctx.send("Vous avez gagné !")
                await ctx.send("Le mot était : " + self.mot)
                return
            else:
                await ctx.send(' '.join(self.lettres))
        else:
            self.deja_proposees.append(lettre)
            await ctx.send("Lettre non trouvée")
