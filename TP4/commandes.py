import discord
from log import Logs
from discord.ext import commands



# Classe pour gérer les commandes, appelées en message
class CustomCommands(commands.Cog):
	def __init__(self, bot) -> None:
		super().__init__()
		self.bot = bot


	# Fonction dédiée à la commande !ping
	@commands.command()
	async def ping(self, ctx):
		message = f"{ctx.message.author.name} says " + str(ctx.message.content)
		Logs.infoLog(message)
		await ctx.send("pong!")


	# 
	@commands.command()
	async def help(self, ctx):
		message = f"{ctx.message.author.name} says " + str(ctx.message.content)
		Logs.infoLog(message)

		help_embed = discord.Embed(
			title = "Page d'aide",
			description = "Liste des commandes de ce bot :",
		)

		help_embed.add_field(name="Help", value="Elle permet d'accéder à l'aide sur les autres commandes.\n```!help```", inline=False)
		help_embed.add_field(name="Ping", value="Elle permet de mesurer le temps mis, pour recevoir une réponse.\n```!ping```", inline=False)
		help_embed.set_footer(text="Requête de: {}".format(ctx.author.display_name))
		await ctx.send(embed=help_embed)

