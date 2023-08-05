from discord.ext import commands
import random


class Morpion(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
		self.players = {"player": "X", "bot": "O"}

	@commands.command()
	async def morpion(self, ctx):
		self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
		await ctx.send("Début de la partie !")
		await ctx.send("Vous êtes les 'X' et moi les 'O'.")
		await ctx.send("Pour jouer, utilisez la commande `!play <case>`.")
		await self.display_board(ctx)

	@commands.command()
	async def play(self, ctx, case):
		case = int(case)
		if self.board[case-1] != "-" or case > 9 or case < 1:
			await ctx.send("La case est déjà prise ou en dehors du plateau.\n Veuillez choisir une autre case")
			return False

		if "-" not in self.board:
			await ctx.send("Match nul !")
			return True

		self.board[case-1] = self.players["player"]
		await self.display_board(ctx)
		if self.check_winner(self.players["player"]):
			await ctx.send("Vous avez gagné !")
			self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
			return False

		await ctx.send("A mon tour : ")
		computer_move = self.get_computer_move()
		self.board[computer_move - 1] = self.players["bot"]
		await self.display_board(ctx)
		if self.check_winner(self.players["bot"]):
			await ctx.send("J'ai gagné !")
			return

		return False

	async def display_board(self, ctx):
		await ctx.send("```\n"
						f" {self.board[0]} | {self.board[1]} | {self.board[2]} \n"
						"---+---+---\n"
						f" {self.board[3]} | {self.board[4]} | {self.board[5]} \n"
						"---+---+---\n"
						f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n"
						"```")

	def check_winner(self, symbol):
		return (self.board[0] == self.board[1] == self.board[2] == symbol or
				self.board[3] == self.board[4] == self.board[5] == symbol or
				self.board[6] == self.board[7] == self.board[8] == symbol or
				self.board[0] == self.board[3] == self.board[6] == symbol or
				self.board[1] == self.board[4] == self.board[7] == symbol or
				self.board[2] == self.board[5] == self.board[8] == symbol or
				self.board[0] == self.board[4] == self.board[8] == symbol or
				self.board[2] == self.board[4] == self.board[6] == symbol)

	def get_computer_move(self):
		available_moves = [i for i, val in enumerate(self.board) if val == '-']
		return random.choice(available_moves) + 1
