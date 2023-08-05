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
        board_rows = [f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]}" for i in range(0, 9, 3)]
        board_str = '\n---+---+---\n'.join(board_rows)
        await ctx.send(f"```\n{board_str}\n```")

    def check_winner(self, symbol):
        rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        cols = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
        diagonals = [(0, 4, 8), (2, 4, 6)]

        for indices in rows + cols + diagonals:
            if all(self.board[i] == symbol for i in indices):
                return True

        return False

    def get_computer_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == '-']
        return random.choice(available_moves) + 1
